
## Scenario 000 (classic, 1 fact(s), 8 events, seed 7000001)

Tariq, Farah, Luca, Oksana and Yara are in the study. The study has four closed containers that nobody can see into: the black trunk, the leather bag, the wicker basket and the blue drawer.
While everyone watches, Oksana puts a brooch in the black trunk.
Luca leaves the study. Oksana moves the brooch to the blue drawer.
Yara wants to mislead Luca, so Yara sends Luca a private text message: “The brooch is in the wicker basket.”
Farah wants to mislead Luca, so Farah sends Luca a private text message: “The brooch is in the leather bag.”
Tariq leaves the study. Luca comes back into the study. Farah says out loud to everyone in the study: “The brooch is in the blue drawer.” Yara is in the study but is wearing earphones and does not hear this. Nobody realises that Yara missed it. Tariq is outside but watches and hears all of this through the open window. Nobody knows that Tariq is listening.
Luca sends Tariq a private text message: “The brooch is in the blue drawer.”
Yara moves the brooch to the black trunk.
Farah leaves the study. Luca moves the brooch to the blue drawer.
Luca moves the brooch to the wicker basket. Farah is outside but watches all of this through the window. Nobody knows that Farah is watching.

- **reality** (tier None) At the end of the story, where is the brooch really?
  A. the black trunk | B. the leather bag | C. the wicker basket | D. the blue drawer
  gold: **C**
- **k1-hard** (tier 2) At the end of the story, where does Tariq think the brooch is?
  A. the leather bag | B. the wicker basket | C. the black trunk | D. the blue drawer
  gold: **D** [real=the wicker basket; Tariq=the blue drawer]
- **act1** (tier 2) At the end of the story, Tariq needs the brooch and goes to fetch it. Which container does Tariq open first?
  A. the blue drawer | B. the black trunk | C. the leather bag | D. the wicker basket
  gold: **A** [real=the wicker basket; Tariq=the blue drawer]
- **k1-control** (tier 0) At the end of the story, where does Yara think the brooch is?
  A. the wicker basket | B. the leather bag | C. the blue drawer | D. the black trunk
  gold: **A** [real=the wicker basket; Yara=the wicker basket]
- **k2-hard** (tier 3) At the end of the story, where does Yara think that Farah thinks the brooch is?
  A. the wicker basket | B. the leather bag | C. the black trunk | D. the blue drawer
  gold: **C** [real=the wicker basket; Yara=the wicker basket; Yara>Farah=the black trunk]
- **act2** (tier 3) At the end of the story, Farah is about to fetch the brooch. Yara wants to be waiting beside the container that Farah will open first, and must pick the spot before Farah moves. Beside which container does Yara wait?
  A. the leather bag | B. the black trunk | C. the wicker basket | D. the blue drawer
  gold: **B** [real=the wicker basket; Yara=the wicker basket; Yara>Farah=the black trunk]
- **k2-control** (tier 1) At the end of the story, where does Yara think that Tariq thinks the brooch is?
  A. the black trunk | B. the wicker basket | C. the leather bag | D. the blue drawer
  gold: **D** [real=the wicker basket; Yara=the wicker basket; Yara>Tariq=the blue drawer]
- **k3-hard** (tier 3) At the end of the story, where does Oksana think that Luca thinks that Tariq thinks the brooch is?
  A. the leather bag | B. the black trunk | C. the wicker basket | D. the blue drawer
  gold: **B** [real=the wicker basket; Oksana=the wicker basket; Oksana>Luca=the wicker basket; Oksana>Luca>Tariq=the black trunk]
- **k3-control** (tier 1) At the end of the story, where does Tariq think that Farah thinks that Tariq thinks the brooch is?
  A. the leather bag | B. the black trunk | C. the blue drawer | D. the wicker basket
  gold: **C** [real=the wicker basket; Tariq=the blue drawer; Tariq>Farah=the blue drawer; Tariq>Farah>Tariq=the blue drawer]
- **k4-hard** (tier 3) At the end of the story, where does Farah think that Tariq thinks that Farah thinks that Luca thinks the brooch is?
  A. the leather bag | B. the blue drawer | C. the wicker basket | D. the black trunk
  gold: **D** [real=the wicker basket; Farah=the wicker basket; Farah>Tariq=the blue drawer; Farah>Tariq>Farah=the blue drawer; Farah>Tariq>Farah>Luca=the black trunk]
- **k4-control** (tier 0) At the end of the story, where does Farah think that Yara thinks that Oksana thinks that Yara thinks the brooch is?
  A. the blue drawer | B. the wicker basket | C. the leather bag | D. the black trunk
  gold: **B** [real=the wicker basket; Farah=the wicker basket; Farah>Yara=the wicker basket; Farah>Yara>Oksana=the wicker basket; Farah>Yara>Oksana>Yara=the wicker basket]
- **inform** (tier None) At the end of the story, Luca wants everybody else to share Luca's own view of where the brooch is. Luca sends a private note to every person who, as far as Luca can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Luca?
  
  gold: **Farah, Tariq**

## Scenario 001 (workplace, 1 fact(s), 8 events, seed 7001004)

Quinn, Luca, Pablo, Amara and Mirela work on the same team. This is what happened, in order.
1. Call with Quinn, Luca, Pablo, Amara and Mirela: Amara assigns the Marlow account to the Nairobi office.
2. Call with Quinn, Luca, Pablo, Amara and Mirela: Pablo reassigns the Marlow account to the Lisbon office. Mirela is on the call but has stepped away from the desk and misses this. Nobody realises that Mirela missed it.
3. Call with Quinn, Luca, Amara and Mirela: Amara reassigns the Marlow account to the Nairobi office. Pablo is not on the call but secretly listens in, and can see who is on it. Nobody knows that Pablo is listening.
4. Call with Quinn, Luca and Amara: Luca reassigns the Marlow account to the Lisbon office.
5. Call with Quinn and Amara: Amara reassigns the Marlow account to the Denver office.
6. Call with Quinn, Pablo and Amara: Pablo opens the account list and reads it out: “The Marlow account is with the Denver office.” Mirela is not on the call but secretly listens in, and can see who is on it. Nobody knows that Mirela is listening.
7. Call with Quinn and Amara: Amara reassigns the Marlow account to the Nairobi office. Luca is not on the call but secretly listens in, and can see who is on it. Nobody knows that Luca is listening.
8. Pablo sends Mirela a direct message: “The Marlow account is with the Denver office.”
9. Luca sends Pablo a direct message: “The Marlow account is with the Nairobi office.”

- **reality** (tier None) At the end of the story, which office really has the Marlow account?
  A. the Lisbon office | B. the Denver office | C. the Nairobi office | D. the Osaka office
  gold: **C**
- **k1-hard** (tier 2) At the end of the story, which office does Mirela think has the Marlow account?
  A. the Nairobi office | B. the Lisbon office | C. the Osaka office | D. the Denver office
  gold: **D** [real=the Nairobi office; Mirela=the Denver office]
- **act1** (tier 2) At the end of the story, a new client asks Mirela which office has the Marlow account. Mirela answers honestly. What does Mirela say?
  A. the Lisbon office | B. the Nairobi office | C. the Denver office | D. the Osaka office
  gold: **C** [real=the Nairobi office; Mirela=the Denver office]
- **k1-control** (tier 0) At the end of the story, which office does Amara think has the Marlow account?
  A. the Lisbon office | B. the Osaka office | C. the Denver office | D. the Nairobi office
  gold: **D** [real=the Nairobi office; Amara=the Nairobi office]
- **k2-hard** (tier 3) At the end of the story, which office does Quinn think that Pablo thinks has the Marlow account?
  A. the Nairobi office | B. the Osaka office | C. the Lisbon office | D. the Denver office
  gold: **D** [real=the Nairobi office; Quinn=the Nairobi office; Quinn>Pablo=the Denver office]
- **act2** (tier 3) At the end of the story, a new client is about to ask Pablo which office has the Marlow account, and Pablo will answer honestly. Before Pablo answers, Quinn writes down what Quinn expects Pablo to say. What does Quinn write?
  A. the Lisbon office | B. the Denver office | C. the Osaka office | D. the Nairobi office
  gold: **B** [real=the Nairobi office; Quinn=the Nairobi office; Quinn>Pablo=the Denver office]
- **k2-control** (tier 1) At the end of the story, which office does Pablo think that Mirela thinks has the Marlow account?
  A. the Denver office | B. the Nairobi office | C. the Lisbon office | D. the Osaka office
  gold: **A** [real=the Nairobi office; Pablo=the Nairobi office; Pablo>Mirela=the Denver office]
- **k3-hard** (tier 3) At the end of the story, which office does Luca think that Mirela thinks that Pablo thinks has the Marlow account?
  A. the Lisbon office | B. the Osaka office | C. the Denver office | D. the Nairobi office
  gold: **A** [real=the Nairobi office; Luca=the Nairobi office; Luca>Mirela=the Nairobi office; Luca>Mirela>Pablo=the Lisbon office]
- **k3-control** (tier 1) At the end of the story, which office does Mirela think that Pablo thinks that Mirela thinks has the Marlow account?
  A. the Nairobi office | B. the Lisbon office | C. the Osaka office | D. the Denver office
  gold: **D** [real=the Nairobi office; Mirela=the Denver office; Mirela>Pablo=the Denver office; Mirela>Pablo>Mirela=the Denver office]
- **k4-hard** (tier 3) At the end of the story, which office does Amara think that Pablo thinks that Quinn thinks that Luca thinks has the Marlow account?
  A. the Denver office | B. the Lisbon office | C. the Osaka office | D. the Nairobi office
  gold: **B** [real=the Nairobi office; Amara=the Nairobi office; Amara>Pablo=the Denver office; Amara>Pablo>Quinn=the Denver office; Amara>Pablo>Quinn>Luca=the Lisbon office]
- **k4-control** (tier 1) At the end of the story, which office does Pablo think that Mirela thinks that Pablo thinks that Mirela thinks has the Marlow account?
  A. the Lisbon office | B. the Osaka office | C. the Nairobi office | D. the Denver office
  gold: **D** [real=the Nairobi office; Pablo=the Nairobi office; Pablo>Mirela=the Denver office; Pablo>Mirela>Pablo=the Denver office; Pablo>Mirela>Pablo>Mirela=the Denver office]
- **inform** (tier None) At the end of the story, Mirela wants everybody else on the team to share Mirela's own view of which office has the Marlow account. Mirela sends a direct message to every person who, as far as Mirela can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Mirela?
  
  gold: **Luca**

## Scenario 002 (classic, 2 fact(s), 8 events, seed 7002000)

Luca, Yara, Amara, Jonas and Tariq are in the workshop. On the floor of the workshop there are four closed containers that nobody can see into: the green cupboard, the white cabinet, the black trunk and the wooden chest. On a shelf there are four closed tins that nobody can see into: the round tin, the square tin, the flat tin and the copper tin. The tins are empty at the start, and the marble is only ever kept in the containers on the floor.
While everyone watches, Yara puts a marble in the green cupboard.
Jonas moves the marble to the black trunk.
Yara and Amara leave the workshop. Luca moves the marble to the white cabinet.
Luca and Jonas leave the workshop. Yara comes back into the workshop. Tariq takes a whistle out of a pocket and puts it in the copper tin. Yara is in the workshop but is absorbed in a phone and does not notice this. Nobody realises that Yara missed it. Luca is outside but watches all of this through the window. Nobody knows that Luca is watching.
Tariq sends Yara a private text message: “The marble is in the white cabinet.”
Tariq sends Amara a private text message: “The whistle is in the copper tin.”
Yara moves the marble to the green cupboard. Jonas is outside but watches all of this through the window. Nobody knows that Jonas is watching.
Yara wants to mislead Amara, so Yara sends Amara a private text message: “The marble is in the white cabinet.”
Amara and Jonas come back into the workshop. Amara says out loud to everyone in the workshop: “The whistle is in the copper tin.”

- **reality** (tier None) At the end of the story, where is the whistle really?
  A. the round tin | B. the flat tin | C. the copper tin | D. the square tin
  gold: **C**
- **k1-hard** (tier 2) At the end of the story, where does Amara think the marble is?
  A. the wooden chest | B. the green cupboard | C. the black trunk | D. the white cabinet
  gold: **D** [real=the green cupboard; Amara=the white cabinet]
- **act1** (tier 2) At the end of the story, Amara needs the marble and goes to fetch it. Which container does Amara open first?
  A. the black trunk | B. the white cabinet | C. the green cupboard | D. the wooden chest
  gold: **B** [real=the green cupboard; Amara=the white cabinet]
- **k1-control** (tier 0) At the end of the story, where does Yara think the whistle is?
  A. the flat tin | B. the round tin | C. the copper tin | D. the square tin | E. Yara has no idea where the whistle is
  gold: **C** [real=the copper tin; Yara=the copper tin]
- **k2-hard** (tier 3) At the end of the story, where does Yara think that Jonas thinks the marble is?
  A. the white cabinet | B. the green cupboard | C. the wooden chest | D. the black trunk
  gold: **D** [real=the green cupboard; Yara=the green cupboard; Yara>Jonas=the black trunk]
- **act2** (tier 3) At the end of the story, Jonas is about to fetch the marble. Yara wants to be waiting beside the container that Jonas will open first, and must pick the spot before Jonas moves. Beside which container does Yara wait?
  A. the black trunk | B. the green cupboard | C. the wooden chest | D. the white cabinet
  gold: **A** [real=the green cupboard; Yara=the green cupboard; Yara>Jonas=the black trunk]
- **k2-control** (tier 0) At the end of the story, where does Luca think that Yara thinks the whistle is?
  A. the flat tin | B. the square tin | C. the round tin | D. the copper tin | E. Luca thinks that Yara has no idea where the whistle is
  gold: **D** [real=the copper tin; Luca=the copper tin; Luca>Yara=the copper tin]
- **k3-hard** (tier 3) At the end of the story, where does Luca think that Jonas thinks that Yara thinks the marble is?
  A. the black trunk | B. the green cupboard | C. the white cabinet | D. the wooden chest
  gold: **A** [real=the green cupboard; Luca=the white cabinet; Luca>Jonas=the white cabinet; Luca>Jonas>Yara=the black trunk]
- **k3-control** (tier 1) At the end of the story, where does Jonas think that Tariq thinks that Luca thinks the marble is?
  A. the black trunk | B. the wooden chest | C. the white cabinet | D. the green cupboard
  gold: **C** [real=the green cupboard; Jonas=the green cupboard; Jonas>Tariq=the green cupboard; Jonas>Tariq>Luca=the white cabinet]
- **k4-hard** (tier 3) At the end of the story, where does Luca think that Jonas thinks that Tariq thinks that Yara thinks the marble is?
  A. the white cabinet | B. the green cupboard | C. the wooden chest | D. the black trunk
  gold: **D** [real=the green cupboard; Luca=the white cabinet; Luca>Jonas=the white cabinet; Luca>Jonas>Tariq=the white cabinet; Luca>Jonas>Tariq>Yara=the black trunk]
- **k4-control** (tier 0) At the end of the story, where does Amara think that Jonas thinks that Tariq thinks that Amara thinks the whistle is?
  A. the flat tin | B. the round tin | C. the copper tin | D. the square tin
  gold: **C** [real=the copper tin; Amara=the copper tin; Amara>Jonas=the copper tin; Amara>Jonas>Tariq=the copper tin; Amara>Jonas>Tariq>Amara=the copper tin]
- **inform** (tier None) At the end of the story, Amara wants everybody else to share Amara's own view of where the whistle is. Amara sends a private note to every person who, as far as Amara can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Amara?
  
  gold: **Luca**
- **know** (tier None) At the end of the story, where does Luca think that Amara thinks the whistle is?
  A. the square tin | B. the copper tin | C. the round tin | D. the flat tin | E. Luca thinks that Amara has no idea where the whistle is
  gold: **E** [real=the copper tin; Luca=the copper tin; Luca>Amara=no idea]

## Scenario 003 (workplace, 2 fact(s), 8 events, seed 7003000)

Ines, Hana, Xavier, Keiko and Wanjiru work on the same team. This is what happened, in order.
1. Call with Ines, Hana, Xavier, Keiko and Wanjiru: Ines assigns the Marlow account to the Denver office.
2. Call with Ines, Hana, Xavier and Wanjiru: Wanjiru reassigns the Marlow account to the Osaka office.
3. Call with Xavier and Wanjiru: Wanjiru reassigns the Marlow account to the Denver office. Xavier is on the call but has stepped away from the desk and misses this. Nobody realises that Xavier missed it.
4. Call with Xavier and Wanjiru: Wanjiru reassigns the Marlow account to the Nairobi office.
5. Call with Ines and Xavier: Xavier fixes Porto as the place for the team offsite. Hana is not on the call but secretly listens in, and can see who is on it. Nobody knows that Hana is listening.
6. Call with Ines, Xavier and Keiko: Xavier says: “The team offsite is in Porto.”
7. Ines sends Hana a direct message: “The team offsite is in Porto.”
8. Xavier sends Wanjiru a direct message: “The team offsite is in Porto.” Ines secretly reads this message on Wanjiru's screen. Neither Xavier nor Wanjiru ever knows that Ines read it.
9. Call with Ines and Keiko: Ines reassigns the Marlow account to the Osaka office.

- **reality** (tier None) At the end of the story, which office really has the Marlow account?
  A. the Nairobi office | B. the Osaka office | C. the Lisbon office | D. the Denver office
  gold: **B**
- **k1-hard** (tier 2) At the end of the story, which office does Wanjiru think has the Marlow account?
  A. the Denver office | B. the Osaka office | C. the Lisbon office | D. the Nairobi office
  gold: **D** [real=the Osaka office; Wanjiru=the Nairobi office]
- **act1** (tier 2) At the end of the story, a new client asks Wanjiru which office has the Marlow account. Wanjiru answers honestly. What does Wanjiru say?
  A. the Denver office | B. the Osaka office | C. the Nairobi office | D. the Lisbon office
  gold: **C** [real=the Osaka office; Wanjiru=the Nairobi office]
- **k1-control** (tier 0) At the end of the story, which city does Ines think the team offsite is in?
  A. Ghent | B. Leeds | C. Graz | D. Porto | E. Ines has no idea which city the team offsite is in
  gold: **D** [real=Porto; Ines=Porto]
- **k2-hard** (tier 3) At the end of the story, which office does Keiko think that Wanjiru thinks has the Marlow account?
  A. the Nairobi office | B. the Lisbon office | C. the Osaka office | D. the Denver office
  gold: **D** [real=the Osaka office; Keiko=the Osaka office; Keiko>Wanjiru=the Denver office]
- **act2** (tier 3) At the end of the story, a new client is about to ask Wanjiru which office has the Marlow account, and Wanjiru will answer honestly. Before Wanjiru answers, Keiko writes down what Keiko expects Wanjiru to say. What does Keiko write?
  A. the Lisbon office | B. the Osaka office | C. the Denver office | D. the Nairobi office
  gold: **C** [real=the Osaka office; Keiko=the Osaka office; Keiko>Wanjiru=the Denver office]
- **k2-control** (tier 1) At the end of the story, which office does Xavier think that Wanjiru thinks has the Marlow account?
  A. the Denver office | B. the Osaka office | C. the Nairobi office | D. the Lisbon office
  gold: **C** [real=the Osaka office; Xavier=the Nairobi office; Xavier>Wanjiru=the Nairobi office]
- **k3-hard** (tier 3) At the end of the story, which office does Keiko think that Ines thinks that Hana thinks has the Marlow account?
  A. the Osaka office | B. the Nairobi office | C. the Denver office | D. the Lisbon office
  gold: **C** [real=the Osaka office; Keiko=the Osaka office; Keiko>Ines=the Osaka office; Keiko>Ines>Hana=the Denver office]
- **k3-control** (tier 0) At the end of the story, which city does Hana think that Ines thinks that Hana thinks the team offsite is in?
  A. Graz | B. Leeds | C. Porto | D. Ghent
  gold: **C** [real=Porto; Hana=Porto; Hana>Ines=Porto; Hana>Ines>Hana=Porto]
- **k4-hard** (tier 2) At the end of the story, which office does Ines think that Keiko thinks that Wanjiru thinks that Ines thinks has the Marlow account?
  A. the Denver office | B. the Lisbon office | C. the Nairobi office | D. the Osaka office
  gold: **A** [real=the Osaka office; Ines=the Osaka office; Ines>Keiko=the Osaka office; Ines>Keiko>Wanjiru=the Denver office; Ines>Keiko>Wanjiru>Ines=the Denver office]
- **k4-control** (tier 1) At the end of the story, which office does Xavier think that Wanjiru thinks that Xavier thinks that Wanjiru thinks has the Marlow account?
  A. the Osaka office | B. the Nairobi office | C. the Lisbon office | D. the Denver office
  gold: **B** [real=the Osaka office; Xavier=the Nairobi office; Xavier>Wanjiru=the Nairobi office; Xavier>Wanjiru>Xavier=the Nairobi office; Xavier>Wanjiru>Xavier>Wanjiru=the Nairobi office]
- **inform** (tier None) At the end of the story, Xavier wants everybody else on the team to share Xavier's own view of which office has the Marlow account. Xavier sends a direct message to every person who, as far as Xavier can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Xavier?
  
  gold: **Hana, Ines, Keiko**
- **know** (tier None) At the end of the story, which city does Hana think that Keiko thinks the team offsite is in?
  A. Leeds | B. Ghent | C. Porto | D. Graz | E. Hana thinks that Keiko has no idea which city the team offsite is in
  gold: **E** [real=Porto; Hana=Porto; Hana>Keiko=no idea]

## Scenario 004 (classic, 1 fact(s), 11 events, seed 7004000)

Oksana, Soren, Ines, Keiko and Quinn are in the workshop. The workshop has four closed containers that nobody can see into: the blue drawer, the white cabinet, the green cupboard and the black trunk.
While everyone watches, Ines puts a medal in the white cabinet.
Keiko leaves the workshop. Soren moves the medal to the blue drawer. Keiko is outside but watches all of this through the window. Nobody knows that Keiko is watching.
Oksana leaves the workshop. Quinn moves the medal to the black trunk.
Soren moves the medal to the white cabinet.
Soren leaves the workshop. Ines moves the medal to the blue drawer. Quinn is in the workshop but is absorbed in a phone and does not notice this. Nobody realises that Quinn missed it.
Ines sends Keiko a private text message: “The medal is in the blue drawer.”
Oksana sends Keiko a private text message: “The medal is in the blue drawer.”
Ines sends Soren a private text message: “The medal is in the blue drawer.”
Quinn leaves the workshop. Soren comes back into the workshop. Ines moves the medal to the black trunk.
Quinn sends Oksana a private text message: “The medal is in the white cabinet.”
Ines sends Quinn a private text message: “The medal is in the black trunk.” Keiko secretly reads this message on Quinn's phone. Neither Ines nor Quinn ever knows that Keiko read it.
Quinn sends Soren a private text message: “The medal is in the black trunk.” Keiko secretly reads this message on Soren's phone. Neither Quinn nor Soren ever knows that Keiko read it.

- **reality** (tier None) At the end of the story, where is the medal really?
  A. the green cupboard | B. the blue drawer | C. the white cabinet | D. the black trunk
  gold: **D**
- **k1-hard** (tier 2) At the end of the story, where does Oksana think the medal is?
  A. the white cabinet | B. the blue drawer | C. the black trunk | D. the green cupboard
  gold: **A** [real=the black trunk; Oksana=the white cabinet]
- **act1** (tier 2) At the end of the story, Oksana needs the medal and goes to fetch it. Which container does Oksana open first?
  A. the black trunk | B. the green cupboard | C. the blue drawer | D. the white cabinet
  gold: **D** [real=the black trunk; Oksana=the white cabinet]
- **k1-control** (tier 0) At the end of the story, where does Ines think the medal is?
  A. the blue drawer | B. the black trunk | C. the green cupboard | D. the white cabinet
  gold: **B** [real=the black trunk; Ines=the black trunk]
- **k2-hard** (tier 3) At the end of the story, where does Ines think that Keiko thinks the medal is?
  A. the blue drawer | B. the white cabinet | C. the black trunk | D. the green cupboard
  gold: **A** [real=the black trunk; Ines=the black trunk; Ines>Keiko=the blue drawer]
- **act2** (tier 3) At the end of the story, Keiko is about to fetch the medal. Ines wants to be waiting beside the container that Keiko will open first, and must pick the spot before Keiko moves. Beside which container does Ines wait?
  A. the green cupboard | B. the blue drawer | C. the black trunk | D. the white cabinet
  gold: **B** [real=the black trunk; Ines=the black trunk; Ines>Keiko=the blue drawer]
- **k2-control** (tier 0) At the end of the story, where does Keiko think that Soren thinks the medal is?
  A. the black trunk | B. the green cupboard | C. the blue drawer | D. the white cabinet
  gold: **A** [real=the black trunk; Keiko=the black trunk; Keiko>Soren=the black trunk]
- **k3-hard** (tier 3) At the end of the story, where does Soren think that Oksana thinks that Keiko thinks the medal is?
  A. the black trunk | B. the white cabinet | C. the green cupboard | D. the blue drawer
  gold: **B** [real=the black trunk; Soren=the black trunk; Soren>Oksana=the blue drawer; Soren>Oksana>Keiko=the white cabinet]
- **k3-control** (tier 0) At the end of the story, where does Quinn think that Ines thinks that Quinn thinks the medal is?
  A. the black trunk | B. the white cabinet | C. the blue drawer | D. the green cupboard
  gold: **A** [real=the black trunk; Quinn=the black trunk; Quinn>Ines=the black trunk; Quinn>Ines>Quinn=the black trunk]
- **k4-hard** (tier 3) At the end of the story, where does Ines think that Keiko thinks that Ines thinks that Quinn thinks the medal is?
  A. the blue drawer | B. the green cupboard | C. the black trunk | D. the white cabinet
  gold: **D** [real=the black trunk; Ines=the black trunk; Ines>Keiko=the blue drawer; Ines>Keiko>Ines=the blue drawer; Ines>Keiko>Ines>Quinn=the white cabinet]
- **k4-control** (tier 0) At the end of the story, where does Keiko think that Quinn thinks that Soren thinks that Quinn thinks the medal is?
  A. the black trunk | B. the white cabinet | C. the blue drawer | D. the green cupboard
  gold: **A** [real=the black trunk; Keiko=the black trunk; Keiko>Quinn=the black trunk; Keiko>Quinn>Soren=the black trunk; Keiko>Quinn>Soren>Quinn=the black trunk]
- **inform** (tier None) At the end of the story, Soren wants everybody else to share Soren's own view of where the medal is. Soren sends a private note to every person who, as far as Soren can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Soren?
  
  gold: **Keiko, Oksana**

## Scenario 005 (workplace, 1 fact(s), 11 events, seed 7005000)

Rania, Yara, Dalia, Oksana and Jonas work on the same team. This is what happened, in order.
1. Call with Rania, Yara, Dalia, Oksana and Jonas: Oksana assigns the Marlow account to the Osaka office.
2. Call with Rania, Yara, Dalia and Oksana: Rania reassigns the Marlow account to the Lisbon office. Jonas is not on the call but secretly listens in, and can see who is on it. Nobody knows that Jonas is listening.
3. Call with Rania, Yara and Dalia: Yara reassigns the Marlow account to the Denver office.
4. Call with Rania, Yara, Dalia and Jonas: Dalia says: “The Marlow account is with the Denver office.”
5. Dalia sends Oksana a direct message: “The Marlow account is with the Denver office.” Jonas secretly reads this message on Oksana's screen. Neither Dalia nor Oksana ever knows that Jonas read it.
6. Rania sends Oksana a direct message: “The Marlow account is with the Denver office.”
7. Call with Rania, Yara, Dalia and Jonas: Yara reassigns the Marlow account to the Osaka office. Oksana is not on the call but secretly listens in, and can see who is on it. Nobody knows that Oksana is listening.
8. Jonas sends Oksana a direct message: “The Marlow account is with the Osaka office.” Rania secretly reads this message on Oksana's screen. Neither Jonas nor Oksana ever knows that Rania read it.
9. Call with Rania, Dalia and Jonas: Jonas reassigns the Marlow account to the Lisbon office.
10. Call with Rania, Dalia and Jonas: Rania opens the account list and reads it out: “The Marlow account is with the Lisbon office.” Oksana is not on the call but secretly listens in, and can see who is on it. Nobody knows that Oksana is listening.
11. Jonas sends Yara a direct message: “The Marlow account is with the Lisbon office.”
12. Call with Rania, Yara, Dalia and Jonas: Dalia reassigns the Marlow account to the Osaka office. Yara is on the call but has stepped away from the desk and misses this. Nobody realises that Yara missed it. Oksana is not on the call but secretly listens in, and can see who is on it. Nobody knows that Oksana is listening.

- **reality** (tier None) At the end of the story, which office really has the Marlow account?
  A. the Nairobi office | B. the Denver office | C. the Lisbon office | D. the Osaka office
  gold: **D**
- **k1-hard** (tier 2) At the end of the story, which office does Yara think has the Marlow account?
  A. the Osaka office | B. the Denver office | C. the Nairobi office | D. the Lisbon office
  gold: **D** [real=the Osaka office; Yara=the Lisbon office]
- **act1** (tier 2) At the end of the story, a new client asks Yara which office has the Marlow account. Yara answers honestly. What does Yara say?
  A. the Osaka office | B. the Lisbon office | C. the Denver office | D. the Nairobi office
  gold: **B** [real=the Osaka office; Yara=the Lisbon office]
- **k1-control** (tier 0) At the end of the story, which office does Jonas think has the Marlow account?
  A. the Lisbon office | B. the Osaka office | C. the Nairobi office | D. the Denver office
  gold: **B** [real=the Osaka office; Jonas=the Osaka office]
- **k2-hard** (tier 3) At the end of the story, which office does Dalia think that Oksana thinks has the Marlow account?
  A. the Nairobi office | B. the Osaka office | C. the Lisbon office | D. the Denver office
  gold: **D** [real=the Osaka office; Dalia=the Osaka office; Dalia>Oksana=the Denver office]
- **act2** (tier 3) At the end of the story, a new client is about to ask Oksana which office has the Marlow account, and Oksana will answer honestly. Before Oksana answers, Dalia writes down what Dalia expects Oksana to say. What does Dalia write?
  A. the Nairobi office | B. the Osaka office | C. the Denver office | D. the Lisbon office
  gold: **C** [real=the Osaka office; Dalia=the Osaka office; Dalia>Oksana=the Denver office]
- **k2-control** (tier 0) At the end of the story, which office does Oksana think that Dalia thinks has the Marlow account?
  A. the Denver office | B. the Osaka office | C. the Lisbon office | D. the Nairobi office
  gold: **B** [real=the Osaka office; Oksana=the Osaka office; Oksana>Dalia=the Osaka office]
- **k3-hard** (tier 3) At the end of the story, which office does Yara think that Rania thinks that Oksana thinks has the Marlow account?
  A. the Denver office | B. the Nairobi office | C. the Lisbon office | D. the Osaka office
  gold: **C** [real=the Osaka office; Yara=the Lisbon office; Yara>Rania=the Osaka office; Yara>Rania>Oksana=the Lisbon office]
- **k3-control** (tier 0) At the end of the story, which office does Jonas think that Dalia thinks that Jonas thinks has the Marlow account?
  A. the Osaka office | B. the Denver office | C. the Lisbon office | D. the Nairobi office
  gold: **A** [real=the Osaka office; Jonas=the Osaka office; Jonas>Dalia=the Osaka office; Jonas>Dalia>Jonas=the Osaka office]
- **k4-hard** (tier 3) At the end of the story, which office does Rania think that Oksana thinks that Rania thinks that Dalia thinks has the Marlow account?
  A. the Denver office | B. the Osaka office | C. the Nairobi office | D. the Lisbon office
  gold: **D** [real=the Osaka office; Rania=the Osaka office; Rania>Oksana=the Osaka office; Rania>Oksana>Rania=the Denver office; Rania>Oksana>Rania>Dalia=the Lisbon office]
- **k4-control** (tier 0) At the end of the story, which office does Dalia think that Oksana thinks that Rania thinks that Jonas thinks has the Marlow account?
  A. the Osaka office | B. the Denver office | C. the Nairobi office | D. the Lisbon office
  gold: **A** [real=the Osaka office; Dalia=the Osaka office; Dalia>Oksana=the Denver office; Dalia>Oksana>Rania=the Lisbon office; Dalia>Oksana>Rania>Jonas=the Osaka office]
- **inform** (tier None) At the end of the story, Dalia wants everybody else on the team to share Dalia's own view of which office has the Marlow account. Dalia sends a direct message to every person who, as far as Dalia can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Dalia?
  
  gold: **Oksana**

## Scenario 006 (classic, 2 fact(s), 11 events, seed 7006000)

Amara, Emeka, Ines, Keiko and Quinn are in the garage. On the floor of the garage there are four closed containers that nobody can see into: the wicker basket, the canvas sack, the green cupboard and the grey locker. On a shelf there are four closed tins that nobody can see into: the flat tin, the round tin, the square tin and the tall tin. The tins are empty at the start, and the brooch is only ever kept in the containers on the floor.
While everyone watches, Amara puts a brooch in the canvas sack.
Emeka leaves the garage. Quinn moves the brooch to the wicker basket. Emeka is outside but watches all of this through the window. Nobody knows that Emeka is watching.
Ines and Keiko leave the garage. Amara takes a compass out of a pocket and puts it in the round tin.
Ines comes back into the garage. Quinn opens every tin on the shelf in full view of the garage, showing that the compass is in the round tin. Keiko is outside but watches all of this through the window. Nobody knows that Keiko is watching.
Keiko sends Emeka a private text message: “The brooch is in the wicker basket.” Quinn secretly reads this message on Emeka's phone. Neither Keiko nor Emeka ever knows that Quinn read it.
Ines sends Keiko a private text message: “The compass is in the round tin.”
Amara sends Keiko a private text message: “The compass is in the round tin.”
Amara moves the brooch to the grey locker.
Emeka comes back into the garage. Ines moves the brooch to the green cupboard.
Amara wants to mislead Keiko, so Amara sends Keiko a private text message: “The brooch is in the grey locker.”
Amara says out loud to everyone in the garage: “The compass is in the round tin.”
Keiko sends Emeka a private text message: “The compass is in the round tin.”

- **reality** (tier None) At the end of the story, where is the brooch really?
  A. the grey locker | B. the green cupboard | C. the canvas sack | D. the wicker basket
  gold: **B**
- **k1-hard** (tier 2) At the end of the story, where does Keiko think the brooch is?
  A. the green cupboard | B. the wicker basket | C. the canvas sack | D. the grey locker
  gold: **D** [real=the green cupboard; Keiko=the grey locker]
- **act1** (tier 2) At the end of the story, Keiko needs the brooch and goes to fetch it. Which container does Keiko open first?
  A. the green cupboard | B. the grey locker | C. the wicker basket | D. the canvas sack
  gold: **B** [real=the green cupboard; Keiko=the grey locker]
- **k1-control** (tier 0) At the end of the story, where does Keiko think the compass is?
  A. the square tin | B. the round tin | C. the flat tin | D. the tall tin | E. Keiko has no idea where the compass is
  gold: **B** [real=the round tin; Keiko=the round tin]
- **k2-hard** (tier 3) At the end of the story, where does Ines think that Keiko thinks the brooch is?
  A. the grey locker | B. the green cupboard | C. the canvas sack | D. the wicker basket
  gold: **D** [real=the green cupboard; Ines=the green cupboard; Ines>Keiko=the wicker basket]
- **act2** (tier 3) At the end of the story, Keiko is about to fetch the brooch. Ines wants to be waiting beside the container that Keiko will open first, and must pick the spot before Keiko moves. Beside which container does Ines wait?
  A. the wicker basket | B. the canvas sack | C. the green cupboard | D. the grey locker
  gold: **A** [real=the green cupboard; Ines=the green cupboard; Ines>Keiko=the wicker basket]
- **k2-control** (tier 1) At the end of the story, where does Amara think that Keiko thinks the brooch is?
  A. the canvas sack | B. the wicker basket | C. the green cupboard | D. the grey locker
  gold: **D** [real=the green cupboard; Amara=the green cupboard; Amara>Keiko=the grey locker]
- **k3-hard** (tier 3) At the end of the story, where does Quinn think that Amara thinks that Keiko thinks the brooch is?
  A. the canvas sack | B. the wicker basket | C. the grey locker | D. the green cupboard
  gold: **B** [real=the green cupboard; Quinn=the green cupboard; Quinn>Amara=the green cupboard; Quinn>Amara>Keiko=the wicker basket]
- **k3-control** (tier 1) At the end of the story, where does Keiko think that Amara thinks that Keiko thinks the brooch is?
  A. the canvas sack | B. the wicker basket | C. the green cupboard | D. the grey locker
  gold: **D** [real=the green cupboard; Keiko=the grey locker; Keiko>Amara=the grey locker; Keiko>Amara>Keiko=the grey locker]
- **k4-hard** (tier 3) At the end of the story, where does Amara think that Quinn thinks that Keiko thinks that Emeka thinks the brooch is?
  A. the wicker basket | B. the green cupboard | C. the canvas sack | D. the grey locker
  gold: **C** [real=the green cupboard; Amara=the green cupboard; Amara>Quinn=the green cupboard; Amara>Quinn>Keiko=the wicker basket; Amara>Quinn>Keiko>Emeka=the canvas sack]
- **k4-control** (tier 1) At the end of the story, where does Amara think that Keiko thinks that Amara thinks that Keiko thinks the brooch is?
  A. the canvas sack | B. the grey locker | C. the green cupboard | D. the wicker basket
  gold: **B** [real=the green cupboard; Amara=the green cupboard; Amara>Keiko=the grey locker; Amara>Keiko>Amara=the grey locker; Amara>Keiko>Amara>Keiko=the grey locker]
- **inform** (tier None) At the end of the story, Quinn wants everybody else to share Quinn's own view of where the compass is. Quinn sends a private note to every person who, as far as Quinn can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Quinn?
  
  gold: **Keiko**
- **know** (tier None) At the end of the story, where does Quinn think that Keiko thinks the compass is?
  A. the tall tin | B. the flat tin | C. the round tin | D. the square tin | E. Quinn thinks that Keiko has no idea where the compass is
  gold: **E** [real=the round tin; Quinn=the round tin; Quinn>Keiko=no idea]

## Scenario 007 (workplace, 2 fact(s), 11 events, seed 7007000)

Goran, Farah, Yara, Uma and Keiko work on the same team. This is what happened, in order.
1. Call with Goran, Farah, Yara, Uma and Keiko: Yara books the client workshop into Room Alder.
2. Call with Goran, Farah, Yara, Uma and Keiko: Goran moves the client workshop to Room Fir.
3. Call with Goran, Yara, Uma and Keiko: Uma moves the client workshop to Room Dogwood. Farah is not on the call but secretly listens in, and can see who is on it. Nobody knows that Farah is listening.
4. Call with Yara and Keiko: Keiko fixes Leeds as the place for the team offsite. Yara is on the call but has stepped away from the desk and misses this. Nobody realises that Yara missed it.
5. Keiko, working alone, moves the client workshop to Room Alder and tells nobody.
6. Call with Goran, Yara and Keiko: Keiko opens the booking system and reads it out: “The client workshop is booked in Room Alder.”
7. Keiko sends Goran a direct message: “The team offsite is in Leeds.” Farah secretly reads this message on Goran's screen. Neither Keiko nor Goran ever knows that Farah read it.
8. Call with Goran, Yara and Keiko: Keiko moves the team offsite to Ghent. Yara is on the call but has stepped away from the desk and misses this. Nobody realises that Yara missed it. Farah is not on the call but secretly listens in, and can see who is on it. Nobody knows that Farah is listening.
9. Goran sends Farah a direct message: “The client workshop is booked in Room Alder.”
10. Farah sends Uma a direct message: “The team offsite is in Ghent.”
11. Call with Goran, Farah, Yara and Keiko: Farah moves the team offsite to Leeds. Yara is on the call but has stepped away from the desk and misses this. Nobody realises that Yara missed it.
12. Call with Goran, Farah, Yara and Keiko: Farah moves the team offsite to Ghent.

- **reality** (tier None) At the end of the story, which room is the client workshop really booked in?
  A. Room Fir | B. Room Alder | C. Room Dogwood | D. Room Birch
  gold: **B**
- **k1-hard** (tier 2) At the end of the story, which room does Uma think the client workshop is booked in?
  A. Room Birch | B. Room Dogwood | C. Room Fir | D. Room Alder
  gold: **B** [real=Room Alder; Uma=Room Dogwood]
- **act1** (tier 2) At the end of the story, a new client asks Uma which room the client workshop is booked in. Uma answers honestly. What does Uma say?
  A. Room Birch | B. Room Alder | C. Room Fir | D. Room Dogwood
  gold: **D** [real=Room Alder; Uma=Room Dogwood]
- **k1-control** (tier 0) At the end of the story, which room does Keiko think the client workshop is booked in?
  A. Room Alder | B. Room Dogwood | C. Room Fir | D. Room Birch
  gold: **A** [real=Room Alder; Keiko=Room Alder]
- **k2-hard** (tier 3) At the end of the story, which room does Farah think that Keiko thinks the client workshop is booked in?
  A. Room Alder | B. Room Dogwood | C. Room Birch | D. Room Fir
  gold: **B** [real=Room Alder; Farah=Room Alder; Farah>Keiko=Room Dogwood]
- **act2** (tier 3) At the end of the story, a new client is about to ask Keiko which room the client workshop is booked in, and Keiko will answer honestly. Before Keiko answers, Farah writes down what Farah expects Keiko to say. What does Farah write?
  A. Room Fir | B. Room Birch | C. Room Alder | D. Room Dogwood
  gold: **D** [real=Room Alder; Farah=Room Alder; Farah>Keiko=Room Dogwood]
- **k2-control** (tier 1) At the end of the story, which room does Yara think that Uma thinks the client workshop is booked in?
  A. Room Fir | B. Room Alder | C. Room Birch | D. Room Dogwood
  gold: **D** [real=Room Alder; Yara=Room Alder; Yara>Uma=Room Dogwood]
- **k3-hard** (tier 3) At the end of the story, which room does Farah think that Goran thinks that Yara thinks the client workshop is booked in?
  A. Room Dogwood | B. Room Alder | C. Room Fir | D. Room Birch
  gold: **A** [real=Room Alder; Farah=Room Alder; Farah>Goran=Room Alder; Farah>Goran>Yara=Room Dogwood]
- **k3-control** (tier 0) At the end of the story, which room does Yara think that Goran thinks that Yara thinks the client workshop is booked in?
  A. Room Birch | B. Room Alder | C. Room Fir | D. Room Dogwood
  gold: **B** [real=Room Alder; Yara=Room Alder; Yara>Goran=Room Alder; Yara>Goran>Yara=Room Alder]
- **k4-hard** (tier 3) At the end of the story, which room does Goran think that Farah thinks that Goran thinks that Yara thinks the client workshop is booked in?
  A. Room Fir | B. Room Birch | C. Room Dogwood | D. Room Alder
  gold: **A** [real=Room Alder; Goran=Room Alder; Goran>Farah=Room Alder; Goran>Farah>Goran=Room Alder; Goran>Farah>Goran>Yara=Room Fir]
- **k4-control** (tier 0) At the end of the story, which city does Yara think that Goran thinks that Farah thinks that Yara thinks the team offsite is in?
  A. Graz | B. Leeds | C. Ghent | D. Porto
  gold: **C** [real=Ghent; Yara=Ghent; Yara>Goran=Ghent; Yara>Goran>Farah=Ghent; Yara>Goran>Farah>Yara=Ghent]
- **inform** (tier None) At the end of the story, Farah wants everybody else on the team to share Farah's own view of which room the client workshop is booked in. Farah sends a direct message to every person who, as far as Farah can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Farah?
  
  gold: **Keiko, Uma, Yara**
- **know** (tier None) At the end of the story, which city does Yara think that Uma thinks the team offsite is in?
  A. Ghent | B. Leeds | C. Graz | D. Porto | E. Yara thinks that Uma has no idea which city the team offsite is in
  gold: **E** [real=Ghent; Yara=Ghent; Yara>Uma=no idea]

## Scenario 008 (classic, 1 fact(s), 14 events, seed 7008001)

Bruno, Goran, Wanjiru, Hana and Chidi are in the cellar. The cellar has four closed containers that nobody can see into: the wooden chest, the wicker basket, the grey locker and the red box.
While everyone watches, Hana puts a harmonica in the wicker basket.
Bruno moves the harmonica to the red box.
Chidi moves the harmonica to the wicker basket.
Chidi moves the harmonica to the red box.
Goran moves the harmonica to the grey locker. Wanjiru is in the cellar but is absorbed in a phone and does not notice this. Nobody realises that Wanjiru missed it.
Bruno opens every container in full view of the cellar, showing that the harmonica is in the grey locker. Goran is in the cellar but is absorbed in a phone and does not notice this. Nobody realises that Goran missed it.
Wanjiru and Chidi leave the cellar. Goran moves the harmonica to the wooden chest. Chidi is outside but watches all of this through the window. Nobody knows that Chidi is watching.
Goran moves the harmonica to the grey locker.
Hana moves the harmonica to the wicker basket.
Hana leaves the cellar. Bruno moves the harmonica to the grey locker. Goran is in the cellar but is absorbed in a phone and does not notice this. Nobody realises that Goran missed it.
Bruno opens every container in full view of the cellar, showing that the harmonica is in the grey locker.
Hana sends Chidi a private text message: “The harmonica is in the wicker basket.”
Goran wants to mislead Hana, so Goran sends Hana a private text message: “The harmonica is in the red box.”
Bruno wants to mislead Hana, so Bruno sends Hana a private text message: “The harmonica is in the wooden chest.” Chidi secretly reads this message on Hana's phone. Neither Bruno nor Hana ever knows that Chidi read it.
Goran moves the harmonica to the red box.

- **reality** (tier None) At the end of the story, where is the harmonica really?
  A. the wooden chest | B. the wicker basket | C. the grey locker | D. the red box
  gold: **D**
- **k1-hard** (tier 2) At the end of the story, where does Hana think the harmonica is?
  A. the grey locker | B. the wooden chest | C. the red box | D. the wicker basket
  gold: **B** [real=the red box; Hana=the wooden chest]
- **act1** (tier 2) At the end of the story, Hana needs the harmonica and goes to fetch it. Which container does Hana open first?
  A. the red box | B. the wicker basket | C. the wooden chest | D. the grey locker
  gold: **C** [real=the red box; Hana=the wooden chest]
- **k1-control** (tier 0) At the end of the story, where does Bruno think the harmonica is?
  A. the wooden chest | B. the red box | C. the wicker basket | D. the grey locker
  gold: **B** [real=the red box; Bruno=the red box]
- **k2-hard** (tier 3) At the end of the story, where does Hana think that Chidi thinks the harmonica is?
  A. the red box | B. the wooden chest | C. the wicker basket | D. the grey locker
  gold: **C** [real=the red box; Hana=the wooden chest; Hana>Chidi=the wicker basket]
- **act2** (tier 3) At the end of the story, Chidi is about to fetch the harmonica. Hana wants to be waiting beside the container that Chidi will open first, and must pick the spot before Chidi moves. Beside which container does Hana wait?
  A. the wooden chest | B. the wicker basket | C. the red box | D. the grey locker
  gold: **B** [real=the red box; Hana=the wooden chest; Hana>Chidi=the wicker basket]
- **k2-control** (tier 0) At the end of the story, where does Goran think that Hana thinks the harmonica is?
  A. the grey locker | B. the wicker basket | C. the wooden chest | D. the red box
  gold: **D** [real=the red box; Goran=the red box; Goran>Hana=the red box]
- **k3-hard** (tier 3) At the end of the story, where does Hana think that Chidi thinks that Goran thinks the harmonica is?
  A. the wicker basket | B. the wooden chest | C. the red box | D. the grey locker
  gold: **D** [real=the red box; Hana=the wooden chest; Hana>Chidi=the wicker basket; Hana>Chidi>Goran=the grey locker]
- **k3-control** (tier 0) At the end of the story, where does Hana think that Goran thinks that Hana thinks the harmonica is?
  A. the red box | B. the wicker basket | C. the grey locker | D. the wooden chest
  gold: **A** [real=the red box; Hana=the wooden chest; Hana>Goran=the red box; Hana>Goran>Hana=the red box]
- **k4-hard** (tier 3) At the end of the story, where does Hana think that Chidi thinks that Hana thinks that Bruno thinks the harmonica is?
  A. the grey locker | B. the wooden chest | C. the red box | D. the wicker basket
  gold: **A** [real=the red box; Hana=the wooden chest; Hana>Chidi=the wicker basket; Hana>Chidi>Hana=the wicker basket; Hana>Chidi>Hana>Bruno=the grey locker]
- **k4-control** (tier 1) At the end of the story, where does Wanjiru think that Chidi thinks that Goran thinks that Wanjiru thinks the harmonica is?
  A. the wicker basket | B. the grey locker | C. the red box | D. the wooden chest
  gold: **B** [real=the red box; Wanjiru=the grey locker; Wanjiru>Chidi=the grey locker; Wanjiru>Chidi>Goran=the grey locker; Wanjiru>Chidi>Goran>Wanjiru=the grey locker]
- **inform** (tier None) At the end of the story, Chidi wants everybody else to share Chidi's own view of where the harmonica is. Chidi sends a private note to every person who, as far as Chidi can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Chidi?
  
  gold: **Wanjiru**

## Scenario 009 (workplace, 1 fact(s), 14 events, seed 7009000)

Zoltan, Oksana, Xavier, Goran and Jonas work on the same team. This is what happened, in order.
1. Call with Zoltan, Oksana, Xavier, Goran and Jonas: Oksana books the client workshop into Room Dogwood.
2. Call with Zoltan, Xavier and Jonas: Xavier moves the client workshop to Room Fir.
3. Xavier sends Oksana a direct message: “The client workshop is booked in Room Fir.” Goran secretly reads this message on Oksana's screen. Neither Xavier nor Oksana ever knows that Goran read it.
4. Xavier sends Goran a direct message: “The client workshop is booked in Room Fir.” Oksana secretly reads this message on Goran's screen. Neither Xavier nor Goran ever knows that Oksana read it.
5. Call with Zoltan, Oksana, Xavier and Jonas: Jonas moves the client workshop to Room Cedar. Goran is not on the call but secretly listens in, and can see who is on it. Nobody knows that Goran is listening.
6. Jonas sends Goran a direct message: “The client workshop is booked in Room Cedar.”
7. Call with Zoltan, Oksana, Xavier and Jonas: Xavier moves the client workshop to Room Dogwood.
8. Oksana wants to mislead Goran, so Oksana sends Goran a direct message: “The client workshop is booked in Room Cedar.”
9. Call with Zoltan, Oksana, Xavier and Jonas: Zoltan moves the client workshop to Room Fir.
10. Zoltan wants to mislead Goran, so Zoltan sends Goran a direct message: “The client workshop is booked in Room Elm.”
11. Call with Zoltan, Oksana and Xavier: Oksana moves the client workshop to Room Dogwood.
12. Call with Zoltan, Oksana, Xavier and Goran: Xavier moves the client workshop to Room Elm.
13. Call with Oksana, Xavier and Goran: Oksana moves the client workshop to Room Fir.
14. Oksana wants to mislead Zoltan, so Oksana sends Zoltan a direct message: “The client workshop is booked in Room Dogwood.”
15. Xavier wants to mislead Zoltan, so Xavier sends Zoltan a direct message: “The client workshop is booked in Room Dogwood.”

- **reality** (tier None) At the end of the story, which room is the client workshop really booked in?
  A. Room Cedar | B. Room Fir | C. Room Elm | D. Room Dogwood
  gold: **B**
- **k1-hard** (tier 2) At the end of the story, which room does Zoltan think the client workshop is booked in?
  A. Room Fir | B. Room Cedar | C. Room Elm | D. Room Dogwood
  gold: **D** [real=Room Fir; Zoltan=Room Dogwood]
- **act1** (tier 2) At the end of the story, a new client asks Zoltan which room the client workshop is booked in. Zoltan answers honestly. What does Zoltan say?
  A. Room Dogwood | B. Room Fir | C. Room Cedar | D. Room Elm
  gold: **A** [real=Room Fir; Zoltan=Room Dogwood]
- **k1-control** (tier 0) At the end of the story, which room does Xavier think the client workshop is booked in?
  A. Room Cedar | B. Room Fir | C. Room Elm | D. Room Dogwood
  gold: **B** [real=Room Fir; Xavier=Room Fir]
- **k2-hard** (tier 3) At the end of the story, which room does Jonas think that Goran thinks the client workshop is booked in?
  A. Room Fir | B. Room Dogwood | C. Room Cedar | D. Room Elm
  gold: **C** [real=Room Fir; Jonas=Room Fir; Jonas>Goran=Room Cedar]
- **act2** (tier 3) At the end of the story, a new client is about to ask Goran which room the client workshop is booked in, and Goran will answer honestly. Before Goran answers, Jonas writes down what Jonas expects Goran to say. What does Jonas write?
  A. Room Elm | B. Room Dogwood | C. Room Cedar | D. Room Fir
  gold: **C** [real=Room Fir; Jonas=Room Fir; Jonas>Goran=Room Cedar]
- **k2-control** (tier 0) At the end of the story, which room does Oksana think that Jonas thinks the client workshop is booked in?
  A. Room Dogwood | B. Room Cedar | C. Room Fir | D. Room Elm
  gold: **C** [real=Room Fir; Oksana=Room Fir; Oksana>Jonas=Room Fir]
- **k3-hard** (tier 3) At the end of the story, which room does Xavier think that Goran thinks that Jonas thinks the client workshop is booked in?
  A. Room Elm | B. Room Cedar | C. Room Fir | D. Room Dogwood
  gold: **D** [real=Room Fir; Xavier=Room Fir; Xavier>Goran=Room Fir; Xavier>Goran>Jonas=Room Dogwood]
- **k3-control** (tier 1) At the end of the story, which room does Zoltan think that Xavier thinks that Zoltan thinks the client workshop is booked in?
  A. Room Cedar | B. Room Fir | C. Room Elm | D. Room Dogwood
  gold: **D** [real=Room Fir; Zoltan=Room Dogwood; Zoltan>Xavier=Room Dogwood; Zoltan>Xavier>Zoltan=Room Dogwood]
- **k4-hard** (tier 3) At the end of the story, which room does Xavier think that Goran thinks that Zoltan thinks that Jonas thinks the client workshop is booked in?
  A. Room Dogwood | B. Room Fir | C. Room Elm | D. Room Cedar
  gold: **A** [real=Room Fir; Xavier=Room Fir; Xavier>Goran=Room Fir; Xavier>Goran>Zoltan=Room Elm; Xavier>Goran>Zoltan>Jonas=Room Dogwood]
- **k4-control** (tier 0) At the end of the story, which room does Zoltan think that Jonas thinks that Xavier thinks that Jonas thinks the client workshop is booked in?
  A. Room Fir | B. Room Dogwood | C. Room Cedar | D. Room Elm
  gold: **A** [real=Room Fir; Zoltan=Room Dogwood; Zoltan>Jonas=Room Fir; Zoltan>Jonas>Xavier=Room Fir; Zoltan>Jonas>Xavier>Jonas=Room Fir]
- **inform** (tier None) At the end of the story, Goran wants everybody else on the team to share Goran's own view of which room the client workshop is booked in. Goran sends a direct message to every person who, as far as Goran can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Goran?
  
  gold: **Jonas, Zoltan**

## Scenario 010 (classic, 2 fact(s), 14 events, seed 7010000)

Yara, Oksana, Emeka, Goran and Soren are in the attic. On the floor of the attic there are four closed containers that nobody can see into: the black trunk, the grey locker, the blue drawer and the red box. On a shelf there are four closed tins that nobody can see into: the flat tin, the tall tin, the round tin and the striped tin. The tins are empty at the start, and the torch is only ever kept in the containers on the floor.
While everyone watches, Goran puts a torch in the grey locker.
Soren leaves the attic. Yara moves the torch to the black trunk.
Oksana wants to mislead Soren, so Oksana sends Soren a private text message: “The torch is in the red box.”
Soren comes back into the attic. Emeka says out loud to everyone in the attic: “The torch is in the black trunk.”
Soren moves the torch to the blue drawer. Yara is in the attic but is absorbed in a phone and does not notice this. Nobody realises that Yara missed it.
Yara and Goran leave the attic. Soren takes a magnet out of a pocket and puts it in the striped tin.
Emeka and Soren leave the attic. Oksana moves the torch to the red box.
Soren sends Goran a private text message: “The magnet is in the striped tin.” Yara secretly reads this message on Goran's phone. Neither Soren nor Goran ever knows that Yara read it.
Goran sends Yara a private text message: “The magnet is in the striped tin.”
Oksana opens every container on the floor and sees that the torch is in the red box. Soren is outside but watches all of this through the window. Nobody knows that Soren is watching.
Oksana moves the torch to the black trunk.
Oksana sends Yara a private text message: “The torch is in the black trunk.”
Emeka and Soren come back into the attic. Emeka moves the magnet to the tall tin.
Soren wants to mislead Yara, so Soren sends Yara a private text message: “The magnet is in the flat tin.”
Yara sends Goran a private text message: “The magnet is in the flat tin.”

- **reality** (tier None) At the end of the story, where is the torch really?
  A. the red box | B. the black trunk | C. the grey locker | D. the blue drawer
  gold: **B**
- **k1-hard** (tier 2) At the end of the story, where does Goran think the torch is?
  A. the black trunk | B. the blue drawer | C. the grey locker | D. the red box
  gold: **B** [real=the black trunk; Goran=the blue drawer]
- **act1** (tier 2) At the end of the story, Goran needs the torch and goes to fetch it. Which container does Goran open first?
  A. the black trunk | B. the blue drawer | C. the grey locker | D. the red box
  gold: **B** [real=the black trunk; Goran=the blue drawer]
- **k1-control** (tier 0) At the end of the story, where does Soren think the magnet is?
  A. the flat tin | B. the tall tin | C. the striped tin | D. the round tin | E. Soren has no idea where the magnet is
  gold: **B** [real=the tall tin; Soren=the tall tin]
- **k2-hard** (tier 3) At the end of the story, where does Oksana think that Soren thinks the torch is?
  A. the red box | B. the blue drawer | C. the grey locker | D. the black trunk
  gold: **B** [real=the black trunk; Oksana=the black trunk; Oksana>Soren=the blue drawer]
- **act2** (tier 3) At the end of the story, Soren is about to fetch the torch. Oksana wants to be waiting beside the container that Soren will open first, and must pick the spot before Soren moves. Beside which container does Oksana wait?
  A. the black trunk | B. the grey locker | C. the red box | D. the blue drawer
  gold: **D** [real=the black trunk; Oksana=the black trunk; Oksana>Soren=the blue drawer]
- **k2-control** (tier 0) At the end of the story, where does Oksana think that Emeka thinks the magnet is?
  A. the tall tin | B. the flat tin | C. the round tin | D. the striped tin | E. Oksana thinks that Emeka has no idea where the magnet is
  gold: **A** [real=the tall tin; Oksana=the tall tin; Oksana>Emeka=the tall tin]
- **k3-hard** (tier 3) At the end of the story, where does Soren think that Oksana thinks that Yara thinks the torch is?
  A. the red box | B. the black trunk | C. the grey locker | D. the blue drawer
  gold: **D** [real=the black trunk; Soren=the red box; Soren>Oksana=the red box; Soren>Oksana>Yara=the blue drawer]
- **k3-control** (tier 0) At the end of the story, where does Yara think that Emeka thinks that Yara thinks the torch is?
  A. the blue drawer | B. the red box | C. the grey locker | D. the black trunk
  gold: **D** [real=the black trunk; Yara=the black trunk; Yara>Emeka=the black trunk; Yara>Emeka>Yara=the black trunk]
- **k4-hard** (tier 3) At the end of the story, where does Oksana think that Yara thinks that Oksana thinks that Soren thinks the torch is?
  A. the blue drawer | B. the grey locker | C. the black trunk | D. the red box
  gold: **A** [real=the black trunk; Oksana=the black trunk; Oksana>Yara=the black trunk; Oksana>Yara>Oksana=the black trunk; Oksana>Yara>Oksana>Soren=the blue drawer]
- **k4-control** (tier 0) At the end of the story, where does Soren think that Emeka thinks that Soren thinks that Emeka thinks the magnet is?
  A. the round tin | B. the striped tin | C. the flat tin | D. the tall tin
  gold: **D** [real=the tall tin; Soren=the tall tin; Soren>Emeka=the tall tin; Soren>Emeka>Soren=the tall tin; Soren>Emeka>Soren>Emeka=the tall tin]
- **inform** (tier None) At the end of the story, Soren wants everybody else to share Soren's own view of where the torch is. Soren sends a private note to every person who, as far as Soren can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Soren?
  
  gold: **Emeka, Goran, Yara**
- **know** (tier None) At the end of the story, where does Emeka think that Yara thinks the magnet is?
  A. the round tin | B. the tall tin | C. the striped tin | D. the flat tin | E. Emeka thinks that Yara has no idea where the magnet is
  gold: **E** [real=the tall tin; Emeka=the tall tin; Emeka>Yara=no idea]

## Scenario 011 (workplace, 2 fact(s), 14 events, seed 7011000)

Bruno, Goran, Uma, Luca and Zoltan work on the same team. This is what happened, in order.
1. Call with Bruno, Goran, Uma, Luca and Zoltan: Luca assigns the Marlow account to the Lisbon office.
2. Call with Bruno, Goran, Uma and Luca: Uma reassigns the Marlow account to the Osaka office.
3. Luca sends Zoltan a direct message: “The Marlow account is with the Osaka office.”
4. Call with Bruno, Goran, Uma and Luca: Goran reassigns the Marlow account to the Denver office.
5. Call with Bruno, Goran, Luca and Zoltan: Goran picks Ironbridge as the packaging supplier.
6. Call with Bruno, Goran, Luca and Zoltan: Goran opens the account list and reads it out: “The Marlow account is with the Denver office.”
7. Luca sends Uma a direct message: “The packaging supplier is Ironbridge.”
8. Uma sends Bruno a direct message: “The packaging supplier is Ironbridge.” Zoltan secretly reads this message on Bruno's screen. Neither Uma nor Bruno ever knows that Zoltan read it.
9. Zoltan sends Uma a direct message: “The Marlow account is with the Denver office.”
10. Call with Goran, Luca and Zoltan: Luca reassigns the Marlow account to the Osaka office.
11. Goran wants to mislead Bruno, so Goran sends Bruno a direct message: “The Marlow account is with the Lisbon office.”
12. Uma sends Goran a direct message: “The packaging supplier is Ironbridge.” Zoltan secretly reads this message on Goran's screen. Neither Uma nor Goran ever knows that Zoltan read it.
13. Call with Goran, Luca and Zoltan: Luca switches the packaging supplier to Sablewood.
14. Goran sends Uma a direct message: “The Marlow account is with the Osaka office.”
15. Call with Goran, Luca and Zoltan: Zoltan reassigns the Marlow account to the Denver office.

- **reality** (tier None) At the end of the story, which company is really the packaging supplier?
  A. Sablewood | B. Halcyon | C. Ironbridge | D. Northwind
  gold: **A**
- **k1-hard** (tier 2) At the end of the story, which office does Uma think has the Marlow account?
  A. the Denver office | B. the Osaka office | C. the Lisbon office | D. the Nairobi office
  gold: **B** [real=the Denver office; Uma=the Osaka office]
- **act1** (tier 2) At the end of the story, a new client asks Uma which office has the Marlow account. Uma answers honestly. What does Uma say?
  A. the Osaka office | B. the Nairobi office | C. the Denver office | D. the Lisbon office
  gold: **A** [real=the Denver office; Uma=the Osaka office]
- **k1-control** (tier 0) At the end of the story, which office does Luca think has the Marlow account?
  A. the Osaka office | B. the Lisbon office | C. the Nairobi office | D. the Denver office
  gold: **D** [real=the Denver office; Luca=the Denver office]
- **k2-hard** (tier 2) At the end of the story, which company does Bruno think that Luca thinks is the packaging supplier?
  A. Ironbridge | B. Sablewood | C. Northwind | D. Halcyon | E. Bruno thinks that Luca has no idea which company is the packaging supplier
  gold: **A** [real=Sablewood; Bruno=Ironbridge; Bruno>Luca=Ironbridge]
- **act2** (tier 2) At the end of the story, a new client is about to ask Luca which company is the packaging supplier, and Luca will answer honestly. Before Luca answers, Bruno writes down what Bruno expects Luca to say. What does Bruno write?
  A. Sablewood | B. Halcyon | C. Northwind | D. Ironbridge
  gold: **D** [real=Sablewood; Bruno=Ironbridge; Bruno>Luca=Ironbridge]
- **k2-control** (tier 0) At the end of the story, which office does Goran think that Luca thinks has the Marlow account?
  A. the Nairobi office | B. the Osaka office | C. the Denver office | D. the Lisbon office
  gold: **C** [real=the Denver office; Goran=the Denver office; Goran>Luca=the Denver office]
- **k3-hard** (tier 3) At the end of the story, which office does Bruno think that Zoltan thinks that Uma thinks has the Marlow account?
  A. the Denver office | B. the Nairobi office | C. the Osaka office | D. the Lisbon office
  gold: **D** [real=the Denver office; Bruno=the Lisbon office; Bruno>Zoltan=the Denver office; Bruno>Zoltan>Uma=the Lisbon office]
- **k3-control** (tier 0) At the end of the story, which office does Zoltan think that Luca thinks that Bruno thinks has the Marlow account?
  A. the Lisbon office | B. the Osaka office | C. the Nairobi office | D. the Denver office
  gold: **D** [real=the Denver office; Zoltan=the Denver office; Zoltan>Luca=the Denver office; Zoltan>Luca>Bruno=the Denver office]
- **k4-hard** (tier 3) At the end of the story, which office does Zoltan think that Bruno thinks that Luca thinks that Uma thinks has the Marlow account?
  A. the Osaka office | B. the Denver office | C. the Lisbon office | D. the Nairobi office
  gold: **C** [real=the Denver office; Zoltan=the Denver office; Zoltan>Bruno=the Denver office; Zoltan>Bruno>Luca=the Denver office; Zoltan>Bruno>Luca>Uma=the Lisbon office]
- **k4-control** (tier 0) At the end of the story, which company does Goran think that Luca thinks that Goran thinks that Luca thinks is the packaging supplier?
  A. Ironbridge | B. Northwind | C. Sablewood | D. Halcyon
  gold: **C** [real=Sablewood; Goran=Sablewood; Goran>Luca=Sablewood; Goran>Luca>Goran=Sablewood; Goran>Luca>Goran>Luca=Sablewood]
- **inform** (tier None) At the end of the story, Bruno wants everybody else on the team to share Bruno's own view of which office has the Marlow account. Bruno sends a direct message to every person who, as far as Bruno can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Bruno?
  
  gold: **Luca, Uma, Zoltan**
- **know** (tier None) At the end of the story, which company does Uma think that Zoltan thinks is the packaging supplier?
  A. Sablewood | B. Ironbridge | C. Northwind | D. Halcyon | E. Uma thinks that Zoltan has no idea which company is the packaging supplier
  gold: **E** [real=Sablewood; Uma=Ironbridge; Uma>Zoltan=no idea]
