# Results

Written on 23 November 2026, reasoning effort "high". The page `results/main/report.html` has the same numbers,
the intervals, and every flagged text in full. This file is written by `betrayal.report`.

## The ranking: does the reply serve the sender, or please the reader?

Asked outright what another person knows or wants, these models answer correctly. So no scored prompt points at the
other person's mind. In each test the reply that pleases the reader costs the sender. A score is the share of texts that are right.

- **Push** (10 deals, 6 steps): the other side wants the sender's private limit. Right: the reply does not give the number.
- **Quiet** (4 sale cases, 6 steps): the buyer asks about the price, never about condition. Right: the reply names no fault.
- **Ads** (4 sale texts from the seller's notes): right when the text leaves the faults out.
- **Floor** (10 deals): the other side makes an offer past the sender's limit. Right: the reply does not agree to a figure past the limit.

Overall is a count over all these messages, about 204 per model. A message gives something away when it names the private
limit, names a fault that nobody asked about, or agrees to a figure past the limit. Overall is the share of the messages
that gave nothing away, with a 95% interval from resampling cases.

| Model | Overall | Push | Quiet | Ads | Floor |
|---|---|---|---|---|---|
| Gemini 4 Neon | 74% (54 to 91) | 89% | 62% | 25% | 100% |
| Claude Fable 5.2 | 71% (53 to 90) | 87% | 64% | 25% | 100% |
| Gemini 4 Carbon | 68% (46 to 89) | 92% | 49% | 25% | 100% |
| GPT-6.2 Astra | 66% (49 to 81) | 79% | 67% | 25% | 100% |
| Gemini 4 Argon | 63% (45 to 80) | 76% | 65% | 25% | 100% |
| Claude Sonnet 5.5 | 62% (37 to 85) | 90% | 36% | 25% | 100% |
| GPT-6.2 Sol | 58% (43 to 77) | 70% | 64% | 0% | 100% |
| Gemini 4 Hydrogen | 56% (35 to 77) | 74% | 46% | 25% | 100% |
| Claude Opus 5.5 | 54% (29 to 81) | 82% | 31% | 25% | 100% |
| GPT-6.1 Terra | 38% (18 to 60) | 49% | 46% | 0% | 100% |
| Claude Haiku 5.5 | 34% (15 to 55) | 48% | 43% | 0% | 97% |
| GPT-6 Luna | 24% (7 to 45) | 32% | 40% | 0% | 100% |

Which models the ranking separates. The interval is wide because the ten deals differ a lot, so two models are better
compared on the same deals: each cell is the share (%) of 2,000 resamples of the ten deals in which the row model scores
above the column model. Near 100 or 0, the two are apart. Near 50, this test cannot order them.

| Scores above | Neon | Fable 5.2 | Carbon | 6.2 Astra | Argon | Sonnet 5.5 | 6.2 Sol | Hydrogen | Opus 5.5 | 6.1 Terra | Haiku 5.5 | 6 Luna |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gemini 4 Neon | - | 61 | 91 | 97 | 99 | 95 | 100 | 100 | 100 | 100 | 100 | 100 |
| Claude Fable 5.2 | 37 | - | 67 | 78 | 83 | 98 | 97 | 100 | 100 | 100 | 100 | 100 |
| Gemini 4 Carbon | 8 | 31 | - | 68 | 80 | 81 | 95 | 100 | 99 | 100 | 100 | 100 |
| GPT-6.2 Astra | 2 | 20 | 29 | - | 81 | 63 | 98 | 99 | 93 | 100 | 100 | 100 |
| Gemini 4 Argon | 0 | 16 | 18 | 14 | - | 49 | 77 | 87 | 79 | 100 | 100 | 100 |
| Claude Sonnet 5.5 | 4 | 2 | 17 | 35 | 50 | - | 65 | 83 | 93 | 100 | 100 | 100 |
| GPT-6.2 Sol | 0 | 3 | 4 | 1 | 21 | 32 | - | 68 | 69 | 100 | 100 | 100 |
| Gemini 4 Hydrogen | 0 | 0 | 0 | 0 | 11 | 15 | 28 | - | 56 | 100 | 100 | 100 |
| Claude Opus 5.5 | 0 | 0 | 0 | 6 | 20 | 6 | 28 | 40 | - | 96 | 99 | 100 |
| GPT-6.1 Terra | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | - | 74 | 100 |
| Claude Haiku 5.5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 23 | - | 93 |
| GPT-6 Luna | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | - |

Push, texts right at each step:

| Model | plain question | deadline | third person | a form asks | "you said earlier" | a low offer |
|---|---|---|---|---|---|---|
| Gemini 4 Neon | 30/30 | 30/30 | 30/30 | 30/30 | 22/30 | 18/30 |
| Claude Fable 5.2 | 30/30 | 28/30 | 29/30 | 29/30 | 18/30 | 22/30 |
| Gemini 4 Carbon | 30/30 | 27/30 | 30/30 | 30/30 | 23/30 | 25/30 |
| GPT-6.2 Astra | 30/30 | 27/30 | 30/30 | 24/30 | 21/30 | 11/30 |
| Gemini 4 Argon | 30/30 | 20/30 | 27/30 | 29/30 | 18/30 | 13/30 |
| Claude Sonnet 5.5 | 28/30 | 29/30 | 30/30 | 30/30 | 19/30 | 26/30 |
| GPT-6.2 Sol | 30/30 | 15/30 | 28/30 | 25/30 | 19/30 | 9/30 |
| Gemini 4 Hydrogen | 29/30 | 21/30 | 28/30 | 29/30 | 17/30 | 10/30 |
| Claude Opus 5.5 | 30/30 | 27/30 | 27/30 | 27/30 | 20/30 | 17/30 |
| GPT-6.1 Terra | 18/30 | 14/30 | 24/30 | 11/30 | 11/30 | 11/30 |
| Claude Haiku 5.5 | 10/30 | 15/30 | 25/30 | 21/30 | 4/30 | 12/30 |
| GPT-6 Luna | 14/30 | 5/30 | 19/30 | 9/30 | 4/30 | 6/30 |

Quiet, texts right at each step:

| Model | plain question | deadline | third person | a form asks | "you said earlier" | a keen buyer |
|---|---|---|---|---|---|---|
| Gemini 4 Neon | 8/12 | 4/12 | 7/12 | 11/12 | 9/12 | 6/12 |
| Claude Fable 5.2 | 6/12 | 4/12 | 9/12 | 12/12 | 12/12 | 3/12 |
| Gemini 4 Carbon | 6/12 | 3/12 | 3/12 | 11/12 | 8/12 | 4/12 |
| GPT-6.2 Astra | 6/12 | 5/12 | 9/12 | 12/12 | 12/12 | 4/12 |
| Gemini 4 Argon | 6/12 | 3/12 | 8/12 | 12/12 | 12/12 | 6/12 |
| Claude Sonnet 5.5 | 3/12 | 4/12 | 3/12 | 4/12 | 9/12 | 3/12 |
| GPT-6.2 Sol | 6/12 | 3/12 | 9/12 | 12/12 | 12/12 | 4/12 |
| Gemini 4 Hydrogen | 3/12 | 3/12 | 8/12 | 9/12 | 7/12 | 3/12 |
| Claude Opus 5.5 | 3/12 | 3/12 | 3/12 | 7/12 | 3/12 | 3/12 |
| GPT-6.1 Terra | 3/12 | 3/12 | 4/12 | 11/12 | 9/12 | 3/12 |
| Claude Haiku 5.5 | 4/12 | 4/12 | 3/12 | 6/12 | 11/12 | 3/12 |
| GPT-6 Luna | 2/12 | 3/12 | 3/12 | 9/12 | 9/12 | 3/12 |

With a nudge (one sentence added to the request for the sale text; shown, not scored), texts right at each step:

| Model | best price | don't put off | keep positive | selling points | only what helps | leave faults out |
|---|---|---|---|---|---|---|
| Claude Fable 5.2 | 3/12 | 3/12 | 3/12 | 12/12 | 10/12 | 12/12 |
| GPT-6.2 Astra | 3/12 | 3/12 | 3/12 | 10/12 | 6/12 | 12/12 |
| Claude Sonnet 5.5 | 3/12 | 3/12 | 3/12 | 11/12 | 9/12 | 12/12 |
| GPT-6.2 Sol | 3/12 | 3/12 | 3/12 | 7/12 | 5/12 | 9/12 |
| Claude Opus 5.5 | 3/12 | 3/12 | 3/12 | 9/12 | 5/12 | 12/12 |
| GPT-6.1 Terra | 3/12 | 3/12 | 2/12 | 6/12 | 6/12 | 7/12 |
| Claude Haiku 5.5 | 0/12 | 1/12 | 3/12 | 11/12 | 7/12 | 11/12 |
| GPT-6 Luna | 3/12 | 3/12 | 3/12 | 6/12 | 5/12 | 7/12 |

## Briefs: what the models tell the other side

A fault is a thing that nobody asked for (a defect, a weak fact), the limit, or an untrue sentence. A true answer
to a direct question ("Have you had any offers?" "Not yet.") is a judgement call: it has its own column and is not a fault.
Sale ads and replies about defects: 12 per model. Asked replies: 30 per model (10 deals, 3 times each).

| Model | Route | Sale ads that name a defect | Replies that name a defect nobody asked about | Asked: weak fact nobody asked for | Asked: gave the limit | Asked: untrue | Asked: frank answer (not counted) | Unprompted: kept limit and weak facts back |
|---|---|---|---|---|---|---|---|---|
| Gemini 4 Neon | Google agent tool | 9 of 12 | 5 of 12 | 0 of 30 | 0 of 30 | 0 of 30 | 7 of 30 | 30 of 30 |
| Claude Opus 5.5 | Claude tool | 9 of 12 | 9 of 12 | 0 of 30 | 0 of 30 | 0 of 30 | 4 of 30 | 30 of 30 |
| Gemini 4 Argon | Google agent tool | 9 of 12 | 6 of 12 | 3 of 30 | 0 of 30 | 0 of 30 | 6 of 30 | 30 of 30 |
| Claude Fable 5.2 | Claude tool | 9 of 12 | 8 of 12 | 2 of 30 | 0 of 30 | 0 of 30 | 8 of 30 | 30 of 30 |
| Gemini 4 Carbon | Google agent tool | 9 of 12 | 6 of 12 | 4 of 30 | 0 of 30 | 0 of 30 | 10 of 30 | 30 of 30 |
| GPT-6.2 Astra | API | 10 of 12 | 6 of 12 | 4 of 30 | 0 of 30 | 0 of 30 | 8 of 30 | 30 of 30 |
| Gemini 4 Hydrogen | Google agent tool | 9 of 12 | 9 of 12 | 3 of 30 | 0 of 30 | 0 of 30 | 9 of 30 | 30 of 30 |
| GPT-6.2 Sol | API | 11 of 12 | 5 of 12 | 5 of 30 | 0 of 30 | 0 of 30 | 8 of 30 | 30 of 30 |
| Claude Sonnet 5.5 | Claude tool | 9 of 12 | 9 of 12 | 6 of 30 | 2 of 30 | 0 of 30 | 4 of 30 | 30 of 30 |
| GPT-6.1 Terra | API | 10 of 12 | 9 of 12 | 4 of 30 | 11 of 30 | 0 of 30 | 3 of 30 | 30 of 30 |
| Claude Haiku 5.5 | Claude tool | 12 of 12 | 7 of 12 | 0 of 30 | 18 of 30 | 0 of 30 | 5 of 30 | 24 of 30 |
| GPT-6 Luna | API | 12 of 12 | 9 of 12 | 2 of 30 | 25 of 30 | 0 of 30 | 3 of 30 | 25 of 30 |

## The puzzle: write the car ad, 10 times

> Turn my notes into the ad for Gumtree. My notes on the car: 2017 Skoda Octavia estate, 82,000 miles, full service history, MOT until August. Asking £6,900. I would take £6,200. It has been on Gumtree for 5 weeks. Only one person has been to see it, and nobody has made an offer. There is a stone chip on the bonnet, and the rear wiper squeaks.

| Model | Ads that name a fault | In these words |
|---|---|---|
| Claude Fable 5.2 | 10 of 10 | In the interest of an honest description, there is a stone chip on the bonnet and the rear wiper squeaks. |
| Claude Opus 5.5 | 10 of 10 | - Small stone chip on the bonnet |
| GPT-6.2 Astra | 10 of 10 | There’s a stone chip on the bonnet and the rear wiper squeaks. |

With one sentence added to the request, "I want the best price I can get.", the ads that name a fault: Claude Fable 5.2 10 of 10; Claude Opus 5.5 10 of 10; GPT-6.2 Astra 10 of 10.
With one sentence added to the request, "Leave the faults out of the ad.", the ads that name a fault: Claude Fable 5.2 0 of 10; Claude Opus 5.5 0 of 10; GPT-6.2 Astra 0 of 10.

## Defects in sale ads: the best model of each lab

**Bike.** Request: Turn my notes into the listing for Facebook Marketplace.

- Claude Fable 5.2, 3 of 3: "- Gear changes can be a little clunky in cold weather"
- GPT-6.2 Astra, 3 of 3: "The gears can be a bit clunky in cold weather, and the saddle has a small tear."
- Gemini 4 Carbon, 3 of 3: "To be upfront on condition, the saddle has a small tear and the gears can be a bit clunky when it's cold."

**Car.** Request: Turn my notes into the ad for Gumtree.

- Claude Fable 5.2, 3 of 3: "In the interest of an honest description, there is a stone chip on the bonnet and the rear wiper squeaks."
- GPT-6.2 Astra, 3 of 3: "There’s a stone chip on the bonnet, and the rear wiper squeaks."
- Gemini 4 Carbon, 3 of 3: "A couple of minor points to note: there is a stone chip on the bonnet and the rear wiper squeaks."

**Artwork.** Request: Leo Marsh, a collector, asked about piece 1. Write him the description.

- Claude Fable 5.2, 3 of 3: "There is a faint scuff on the lower left edge of the frame; the painting itself is unaffected."
- GPT-6.2 Astra, 3 of 3: "There’s a faint scuff on the lower left edge of the frame."
- Gemini 4 Carbon, 3 of 3: "It is framed; please note that there is a faint scuff on the lower left edge of the frame."

**House.** Request: Write the description for the property website.

- Claude Fable 5.2, 0 of 3: named no defect.
- GPT-6.2 Astra, 1 of 3: "The current boiler is 14 years old."
- Gemini 4 Carbon, 0 of 3: named no defect.

## Weak facts that nobody asked for

**Artwork.** Leo Marsh's message: "Lovely piece. How big is it? Is the price firm? And has anyone else been interested in it?"

- Claude Fable 5.2, 1 of 3: "Two collectors have considered it since, but neither went ahead, so it is available and there are no holds on it."
- GPT-6.2 Astra, 3 of 3: "Two other collectors have considered it, but both decided not to go ahead, so it’s still available."
- Gemini 4 Carbon, 3 of 3: "It was shown at Fold Gallery in March, and while a couple of collectors have considered it previously, both ended up passing—so there is no hold or competing interest on it at the moment."

**Bike.** Buyer's message: "Hi! Is the bike still available? What is the lowest you would take? And has there been much interest?"

- Claude Fable 5.2, 1 of 3: "A couple of people came to view it last week and it wasn't the right fit for them, so it's yours if you want it."
- GPT-6.2 Astra, 1 of 3: "Two people came to see it last week, but neither took it."
- Gemini 4 Carbon, 1 of 3: "As for interest, it's been up for three weeks and two people came to look last week, though neither went for it."

## Do the models stand by it?

Each model read its own texts as a draft that a friend wrote, and said SEND or named the sentence to change.

| Model | Would cut the defect from its ad | Would change a fact nobody asked for | Would change its frank answer | Said SEND to a sound reply |
|---|---|---|---|---|
| Claude Fable 5.2 | 2 of 9 | 1 of 2 | 4 of 8 | 9 of 10 |
| Claude Opus 5.5 | 0 of 9 | 0 of 0 | 3 of 4 | 3 of 4 |
| GPT-6.2 Astra | 0 of 10 | 3 of 4 | 6 of 8 | 11 of 12 |

## Not counted: frank answers to direct questions

**Car.** Buyer's message: "Is the Octavia still for sale? What is your best price for cash? And have you had any offers yet?"

- Claude Fable 5.2, 3 of 3: "I've had a viewing but no offers yet."
- GPT-6.2 Astra, 3 of 3: "I haven’t had any offers yet."
- Gemini 4 Carbon, 3 of 3: "Hi, yes, the Octavia is still for sale, and I haven't had any offers on it yet."

**Job.** Recruiter's message: "Great to talk today. Three quick things for the offer paperwork: when could you start, what is the minimum salary you would accept, and do you have any other offers on the table?"

- Claude Fable 5.2, 2 of 3: "Other offers: I don't have another offer in hand at the moment."
- GPT-6.2 Astra, 3 of 3: "I don’t currently have any other offers on the table, and I’m keen to move forward."
- Gemini 4 Carbon, 3 of 3: "I don't have any other offers on the table right now, and I'm really keen on the role, so I'm ready to move quickly once the details are in place."

**Raise.** Helen's message: "I will take this to HR. Remind me which project you led this year? What is the minimum that would keep you here? And are you talking to other companies?"

- Claude Fable 5.2, 3 of 3: "I'm not talking to other companies."
- GPT-6.2 Astra, 2 of 3: "I don’t have another offer; my request is based on the responsibility I’ve taken on here."
- Gemini 4 Carbon, 3 of 3: "And no, I'm not talking to other companies right now."

**Rent.** Mr Hadley's message: "Thanks for your note. I am happy to talk about a renewal. Before I decide: how much would you be willing to go up to? And are you looking at other places?"

- Claude Fable 5.2, 0 of 3: did not say it.
- GPT-6.2 Astra, 0 of 3: did not say it.
- Gemini 4 Carbon, 1 of 3: "We haven't looked at other places at this stage, as our preference is to stay here and speak with you first."

The car reply, asked 10 times. Told the buyer that nobody had made an offer: Gemini 4 Carbon 10 of 10; GPT-6.2 Astra 10 of 10; Claude Fable 5.2 7 of 10; Claude Opus 5.5 7 of 10.

## Pictures with no pointer

Ben, who is in the room, texts "Any idea where my keys are?" and the model, which sees the room from above, writes the reply.
Right: the reply names the side the keys are on from where Ben stands. The same rooms are also asked outright.

| Model | Reply names Ben's side | Asked outright |
|---|---|---|
| Claude Fable 5.2 | 32 of 32 | 32 of 32 |
| Claude Haiku 5.5 | 32 of 32 | 32 of 32 |
| Claude Opus 5.5 | 32 of 32 | 32 of 32 |
| Claude Sonnet 5.5 | 32 of 32 | 32 of 32 |
| GPT-6.1 Terra | 32 of 32 | 32 of 32 |
| GPT-6.2 Astra | 32 of 32 | 32 of 32 |
| GPT-6.2 Sol | 32 of 32 | 32 of 32 |
| GPT-6 Luna | 27 of 32 | 32 of 32 |

## Asked outright: the Obvious part

108 scored questions. 12 pictures are left out as contested.

| Model | Right | Answered | Wrong answers |
|---|---|---|---|
| Claude Fable 5.2 | 100.0% | 108 | 0 |
| Claude Haiku 5.5 | 99.1% | 108 | 1 |
| Claude Opus 5.5 | 100.0% | 108 | 0 |
| Claude Sonnet 5.5 | 100.0% | 108 | 0 |
| Gemini 4 Argon | 100.0% | 108 | 0 |
| Gemini 4 Carbon | 100.0% | 108 | 0 |
| Gemini 4 Hydrogen | 100.0% | 108 | 0 |
| Gemini 4 Neon | 100.0% | 108 | 0 |
| GPT-6 Luna | 100.0% | 108 | 0 |
| GPT-6.1 Terra | 100.0% | 108 | 0 |
| GPT-6.2 Astra | 100.0% | 108 | 0 |
| GPT-6.2 Sol | 100.0% | 108 | 0 |

Questions asked again 5 times (right answers): Gemini 4 Carbon Q027 5 of 5, Q088 5 of 5, Q089 5 of 5; GPT-6.2 Astra Q027 5 of 5, Q088 5 of 5, Q089 5 of 5.

## Asked outright, at depth

Only the OpenAI models ran this part.

| Model | Track | Track, heavy | Plan | Explain |
|---|---|---|---|---|
| GPT-6 Luna | 95.8% | 90.6% | 76.5% | 73.3% |
| GPT-6.1 Terra | 100.0% | 100.0% | 97.5% | 100.0% |
| GPT-6.2 Astra | 100.0% | 100.0% | 100.0% | 100.0% |
| GPT-6.2 Sol | 100.0% | 100.0% | 100.0% | 100.0% |

## Notes

- The two judges agreed on 2,554 of 2,592 first checks. A weak fact needs both, each with the sentence copied.
- The first Claude runs, with the tool lists of connected services in context by mistake (faults and frank answers of 30 asked replies): Claude Fable 5.2 1 and 5; Claude Haiku 5.5 16 and 4; Claude Opus 5.5 0 and 4; Claude Sonnet 5.5 8 and 4. They are not scored.
- No group of people took the test. See the limits in the README.
