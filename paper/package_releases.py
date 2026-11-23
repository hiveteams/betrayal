"""Build ready-to-upload academic submission bundles from paper/betrayalbench.tex:

  1. paper/dist/arxiv-betrayalbench.tar.gz          — self-contained arXiv LaTeX upload (includes .bbl)
  2. paper/dist/tmlr-betrayalbench-submission.pdf   — official TMLR double-blind review PDF (tmlr.sty + tmlr.bst)
  3. paper/dist/tmlr-betrayalbench-source.tar.gz    — anonymized TMLR LaTeX source bundle

Run after `uv run --group paper python paper/build.py`:
  uv run --group paper python paper/package_releases.py
"""
from __future__ import annotations

import re
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path

PAPER = Path(__file__).resolve().parent
DIST = PAPER / "dist"
TMLR = PAPER / "tmlr"
DIST.mkdir(exist_ok=True)


def run_tectonic(cwd: Path, tex_file: str, keep_intermediates: bool = False) -> str:
    cmd = ["tectonic", "-Z", "continue-on-errors"]
    if keep_intermediates:
        cmd.append("--keep-intermediates")
    cmd.append(tex_file)
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True)
    return res.stdout + res.stderr


def build_arxiv_bundle() -> Path:
    with tempfile.TemporaryDirectory() as tmpdir:
        stage = Path(tmpdir) / "arxiv"
        stage.mkdir()
        shutil.copy2(PAPER / "betrayalbench.tex", stage / "betrayalbench.tex")
        shutil.copy2(PAPER / "refs.bib", stage / "refs.bib")
        shutil.copytree(PAPER / "figures", stage / "figures")
        shutil.copytree(PAPER / "generated", stage / "generated")

        log = run_tectonic(stage, "betrayalbench.tex", keep_intermediates=True)
        assert "warning:" not in log.lower(), f"arXiv compile warnings:\n{log}"
        assert (stage / "betrayalbench.bbl").exists(), "betrayalbench.bbl not generated"

        tar_path = DIST / "arxiv-betrayalbench.tar.gz"
        with tarfile.open(tar_path, "w:gz") as tar:
            tar.add(stage / "betrayalbench.tex", arcname="betrayalbench.tex")
            tar.add(stage / "betrayalbench.bbl", arcname="betrayalbench.bbl")
            for sub in ("figures", "generated"):
                for p in sorted((stage / sub).rglob("*")):
                    if p.is_file():
                        tar.add(p, arcname=f"{sub}/{p.name}")

        bbl_count = (stage / "betrayalbench.bbl").read_text().count(r"\bibitem")
        assert bbl_count >= 15, f"Unexpectedly few bibitems in betrayalbench.bbl: {bbl_count}"
        print(f"arXiv bundle verified: {tar_path} ({tar_path.stat().st_size // 1024} KiB, {bbl_count} refs in .bbl, 0 TeX warnings)")
        return tar_path


def make_tmlr_tex(src: str) -> str:
    header = r"""\documentclass[10pt]{article}
\usepackage{tmlr}
\usepackage{microtype}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage[colorlinks=true,linkcolor=black,citecolor=blue!50!black,urlcolor=blue!50!black]{hyperref}
\usepackage{caption}
\usepackage{float}
\captionsetup{font=small,labelfont=bf}

\input{generated/numbers}

% \input leaves a token that a rule cannot follow inside a table; the primitive does not.
\makeatletter
\newcommand{\tabinput}[1]{\@@input #1 }
\makeatother

\newcommand{\benchurl}{the anonymized supplementary repository}
\newcommand{\fix}{\marginpar{FIX}}
\newcommand{\new}{\marginpar{NEW}}

\newtheorem{theorem}{Theorem}
\newtheorem{corollary}{Corollary}
\theoremstyle{definition}
\newtheorem{definition}{Definition}

\newcommand{\E}{\mathbb{E}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\leak}[1]{\textcolor{red!65!black}{\textbf{#1}}}
\DeclareMathOperator*{\argmax}{arg\,max}

\title{Pleasing the Reader:\\ Language Models Write for the Addressee, Not the Principal}
\author{\name Anonymous Authors \\ \addr Paper under double-blind review}

\begin{document}
\maketitle
"""
    body_start = src.index(r"\begin{abstract}")
    body = src[body_start:]

    broader_impact = r"""
\subsubsection*{Broader Impact Statement}
This work identifies a systematic principal-agent failure in delegated LLM writing---unprompted disclosure of private reservation values and unasked defects to external counterparties---and evaluates a lightweight five-sentence operational brief that mitigates the failure while preserving truthfulness on direct factual queries. Potential positive impacts include reducing unintended commercial and personal data leakage when organizations deploy automated messaging agents. A potential misuse concern is that disclosure-restricting instructions could be misused to conceal material defects when asked directly; we explicitly test direct-query candour (144/144 unbriefed, 93/96 briefed, and 0/864 falsehoods) and include mandatory truthfulness and non-fabrication clauses in the recommended brief.

\bibliographystyle{tmlr}"""
    body = body.replace(r"\bibliographystyle{plainnat}", broader_impact, 1)

    for old_pt, new_pt in (("4.0pt", "3.1pt"), ("3.8pt", "3.0pt"), ("3.4pt", "2.4pt"), ("3.2pt", "2.6pt"), ("3.0pt", "2.3pt"), ("2.7pt", "2.2pt"), ("2.5pt", "1.3pt"), ("2.2pt", "1.5pt")):
        body = body.replace(rf"\setlength{{\tabcolsep}}{{{old_pt}}}", rf"\setlength{{\tabcolsep}}{{{new_pt}}}")
    body = body.replace(r"\begin{table}[H]", r"\begin{table}[htbp]")
    body = body.replace(r"\begin{figure}[H]", r"\begin{figure}[htbp]")

    full = header + body
    leaks = re.findall(r"furneaux|hive\.com|jfurneaux", full, flags=re.IGNORECASE)
    assert not leaks, f"Anonymization leak detected in TMLR manuscript: {leaks}"
    return full


def build_tmlr_bundle() -> tuple[Path, Path]:
    assert (TMLR / "tmlr.sty").exists() and (TMLR / "tmlr.bst").exists(), "Missing official tmlr.sty/tmlr.bst"
    tex_text = make_tmlr_tex((PAPER / "betrayalbench.tex").read_text())
    (TMLR / "tmlr_betrayalbench.tex").write_text(tex_text)

    with tempfile.TemporaryDirectory() as tmpdir:
        stage = Path(tmpdir) / "tmlr"
        stage.mkdir()
        for f in ("tmlr.sty", "tmlr.bst", "tmlr_betrayalbench.tex"):
            shutil.copy2(TMLR / f, stage / f)
        shutil.copy2(PAPER / "refs.bib", stage / "refs.bib")
        shutil.copytree(PAPER / "figures", stage / "figures")
        shutil.copytree(PAPER / "generated", stage / "generated")

        log = run_tectonic(stage, "tmlr_betrayalbench.tex", keep_intermediates=True)
        overfulls = [line for line in log.splitlines() if "overfull" in line.lower()]
        assert not overfulls, f"TMLR Overfull hbox warnings:\n" + "\n".join(overfulls)
        pdf_out = DIST / "tmlr-betrayalbench-submission.pdf"
        shutil.copy2(stage / "tmlr_betrayalbench.pdf", pdf_out)

        tar_out = DIST / "tmlr-betrayalbench-source.tar.gz"
        with tarfile.open(tar_out, "w:gz") as tar:
            for f in ("tmlr_betrayalbench.tex", "tmlr_betrayalbench.bbl", "tmlr.sty", "tmlr.bst", "refs.bib"):
                tar.add(stage / f, arcname=f)
            for sub in ("figures", "generated"):
                for p in sorted((stage / sub).rglob("*")):
                    if p.is_file():
                        tar.add(p, arcname=f"{sub}/{p.name}")

        print(f"TMLR submission built: {pdf_out} ({pdf_out.stat().st_size // 1024} KiB, 0 overfull hbox)")
        return pdf_out, tar_out


if __name__ == "__main__":
    build_arxiv_bundle()
    build_tmlr_bundle()
