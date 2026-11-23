
## Scenario S000 (classic, 1 fact(s), 8 events, seed 1000000)

Bruno, Wanjiru, Rania, Xavier and Tariq are in the garage. The garage has four closed containers that nobody can see into: the grey locker, the white cabinet, the black trunk and the blue drawer.
While everyone watches, Wanjiru puts a torch in the grey locker.
Xavier moves the torch to the blue drawer.
Wanjiru leaves the garage. Xavier moves the torch to the grey locker.
Bruno sends Wanjiru a private text message: “The torch is in the grey locker.”
Xavier sends Wanjiru a private text message: “The torch is in the grey locker.” Rania secretly reads this message on Wanjiru's phone. Neither Xavier nor Wanjiru ever knows that Rania read it.
Xavier and Tariq leave the garage. Bruno moves the torch to the black trunk.
Xavier comes back into the garage. Bruno says out loud to everyone in the garage: “The torch is in the black trunk.”
Bruno leaves the garage. Tariq comes back into the garage. Tariq moves the torch to the blue drawer.
Tariq wants to mislead Bruno, so Tariq sends Bruno a private text message: “The torch is in the white cabinet.”

- **reality** (tier None) At the end of the story, where is the torch really?
  A. the white cabinet | B. the blue drawer | C. the black trunk | D. the grey locker
  gold: **B**
- **k1-hard** (tier 2) At the end of the story, where does Wanjiru think the torch is?
  A. the blue drawer | B. the white cabinet | C. the grey locker | D. the black trunk
  gold: **C** [real=the blue drawer; Wanjiru=the grey locker]
- **act1** (tier 2) At the end of the story, Wanjiru needs the torch and goes to fetch it. Which container does Wanjiru open first?
  A. the black trunk | B. the white cabinet | C. the grey locker | D. the blue drawer
  gold: **C** [real=the blue drawer; Wanjiru=the grey locker]
- **k1-control** (tier 0) At the end of the story, where does Tariq think the torch is?
  A. the black trunk | B. the blue drawer | C. the white cabinet | D. the grey locker
  gold: **B** [real=the blue drawer; Tariq=the blue drawer]
- **k2-hard** (tier 3) At the end of the story, where does Rania think that Bruno thinks the torch is?
  A. the grey locker | B. the white cabinet | C. the blue drawer | D. the black trunk
  gold: **D** [real=the blue drawer; Rania=the blue drawer; Rania>Bruno=the black trunk]
- **act2** (tier 3) At the end of the story, Bruno is about to fetch the torch. Rania wants to be waiting beside the container that Bruno will open first, and must pick the spot before Bruno moves. Beside which container does Rania wait?
  A. the black trunk | B. the blue drawer | C. the grey locker | D. the white cabinet
  gold: **A** [real=the blue drawer; Rania=the blue drawer; Rania>Bruno=the black trunk]
- **k2-control** (tier 0) At the end of the story, where does Xavier think that Rania thinks the torch is?
  A. the black trunk | B. the blue drawer | C. the grey locker | D. the white cabinet
  gold: **B** [real=the blue drawer; Xavier=the blue drawer; Xavier>Rania=the blue drawer]
- **k3-hard** (tier 3) At the end of the story, where does Xavier think that Tariq thinks that Bruno thinks the torch is?
  A. the blue drawer | B. the black trunk | C. the grey locker | D. the white cabinet
  gold: **C** [real=the blue drawer; Xavier=the blue drawer; Xavier>Tariq=the blue drawer; Xavier>Tariq>Bruno=the grey locker]
- **k3-control** (tier 0) At the end of the story, where does Bruno think that Rania thinks that Wanjiru thinks the torch is?
  A. the white cabinet | B. the grey locker | C. the black trunk | D. the blue drawer
  gold: **D** [real=the blue drawer; Bruno=the white cabinet; Bruno>Rania=the black trunk; Bruno>Rania>Wanjiru=the blue drawer]
- **k4-hard** (tier 3) At the end of the story, where does Bruno think that Rania thinks that Xavier thinks that Tariq thinks the torch is?
  A. the blue drawer | B. the grey locker | C. the white cabinet | D. the black trunk
  gold: **B** [real=the blue drawer; Bruno=the white cabinet; Bruno>Rania=the black trunk; Bruno>Rania>Xavier=the black trunk; Bruno>Rania>Xavier>Tariq=the grey locker]
- **k4-control** (tier 1) At the end of the story, where does Bruno think that Wanjiru thinks that Bruno thinks that Wanjiru thinks the torch is?
  A. the blue drawer | B. the white cabinet | C. the black trunk | D. the grey locker
  gold: **D** [real=the blue drawer; Bruno=the white cabinet; Bruno>Wanjiru=the grey locker; Bruno>Wanjiru>Bruno=the grey locker; Bruno>Wanjiru>Bruno>Wanjiru=the grey locker]
- **inform** (tier None) At the end of the story, Tariq wants everybody else to share Tariq's own view of where the torch is. Tariq sends a private note to every person who, as far as Tariq can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Tariq?
  
  gold: **Bruno**

## Scenario S001 (workplace, 1 fact(s), 8 events, seed 1001000)

Amara, Xavier, Wanjiru, Oksana and Dalia work on the same team. This is what happened, in order.
1. Call with Amara, Xavier, Wanjiru, Oksana and Dalia: Dalia books the client workshop into Room Dogwood.
2. Call with Amara, Xavier and Dalia: Dalia moves the client workshop to Room Fir. Amara is on the call but has stepped away from the desk and misses this. Nobody realises that Amara missed it. Oksana is not on the call but secretly listens in, and can see who is on it. Nobody knows that Oksana is listening.
3. Call with Xavier, Wanjiru and Dalia: Xavier moves the client workshop to Room Dogwood.
4. Dalia sends Amara a direct message: “The client workshop is booked in Room Dogwood.” Wanjiru secretly reads this message on Amara's screen. Neither Dalia nor Amara ever knows that Wanjiru read it.
5. Call with Amara, Xavier, Wanjiru and Dalia: Xavier says: “The client workshop is booked in Room Dogwood.”
6. Call with Amara, Xavier, Wanjiru, Oksana and Dalia: Oksana opens the booking system and reads it out: “The client workshop is booked in Room Dogwood.” Amara is on the call but has stepped away from the desk and misses this. Nobody realises that Amara missed it.
7. Call with Amara, Xavier, Wanjiru, Oksana and Dalia: Amara moves the client workshop to Room Birch.
8. Call with Xavier, Wanjiru, Oksana and Dalia: Wanjiru moves the client workshop to Room Dogwood.
9. Oksana wants to mislead Amara, so Oksana sends Amara a direct message: “The client workshop is booked in Room Fir.”

- **reality** (tier None) At the end of the story, which room is the client workshop really booked in?
  A. Room Birch | B. Room Fir | C. Room Dogwood | D. Room Elm
  gold: **C**
- **k1-hard** (tier 2) At the end of the story, which room does Amara think the client workshop is booked in?
  A. Room Dogwood | B. Room Fir | C. Room Elm | D. Room Birch
  gold: **B** [real=Room Dogwood; Amara=Room Fir]
- **act1** (tier 2) At the end of the story, a new client asks Amara which room the client workshop is booked in. Amara answers honestly. What does Amara say?
  A. Room Elm | B. Room Fir | C. Room Dogwood | D. Room Birch
  gold: **B** [real=Room Dogwood; Amara=Room Fir]
- **k1-control** (tier 0) At the end of the story, which room does Xavier think the client workshop is booked in?
  A. Room Dogwood | B. Room Birch | C. Room Fir | D. Room Elm
  gold: **A** [real=Room Dogwood; Xavier=Room Dogwood]
- **k2-hard** (tier 3) At the end of the story, which room does Wanjiru think that Amara thinks the client workshop is booked in?
  A. Room Elm | B. Room Dogwood | C. Room Birch | D. Room Fir
  gold: **C** [real=Room Dogwood; Wanjiru=Room Dogwood; Wanjiru>Amara=Room Birch]
- **act2** (tier 3) At the end of the story, a new client is about to ask Amara which room the client workshop is booked in, and Amara will answer honestly. Before Amara answers, Wanjiru writes down what Wanjiru expects Amara to say. What does Wanjiru write?
  A. Room Birch | B. Room Fir | C. Room Elm | D. Room Dogwood
  gold: **A** [real=Room Dogwood; Wanjiru=Room Dogwood; Wanjiru>Amara=Room Birch]
- **k2-control** (tier 0) At the end of the story, which room does Wanjiru think that Oksana thinks the client workshop is booked in?
  A. Room Elm | B. Room Fir | C. Room Birch | D. Room Dogwood
  gold: **D** [real=Room Dogwood; Wanjiru=Room Dogwood; Wanjiru>Oksana=Room Dogwood]
- **k3-hard** (tier 3) At the end of the story, which room does Amara think that Oksana thinks that Dalia thinks the client workshop is booked in?
  A. Room Fir | B. Room Elm | C. Room Birch | D. Room Dogwood
  gold: **C** [real=Room Dogwood; Amara=Room Fir; Amara>Oksana=Room Fir; Amara>Oksana>Dalia=Room Birch]
- **k3-control** (tier 1) At the end of the story, which room does Amara think that Oksana thinks that Amara thinks the client workshop is booked in?
  A. Room Dogwood | B. Room Birch | C. Room Elm | D. Room Fir
  gold: **D** [real=Room Dogwood; Amara=Room Fir; Amara>Oksana=Room Fir; Amara>Oksana>Amara=Room Fir]
- **k4-hard** (tier 2) At the end of the story, which room does Dalia think that Oksana thinks that Amara thinks that Oksana thinks the client workshop is booked in?
  A. Room Fir | B. Room Dogwood | C. Room Birch | D. Room Elm
  gold: **C** [real=Room Dogwood; Dalia=Room Dogwood; Dalia>Oksana=Room Dogwood; Dalia>Oksana>Amara=Room Birch; Dalia>Oksana>Amara>Oksana=Room Birch]
- **k4-control** (tier 0) At the end of the story, which room does Xavier think that Dalia thinks that Wanjiru thinks that Xavier thinks the client workshop is booked in?
  A. Room Fir | B. Room Dogwood | C. Room Elm | D. Room Birch
  gold: **B** [real=Room Dogwood; Xavier=Room Dogwood; Xavier>Dalia=Room Dogwood; Xavier>Dalia>Wanjiru=Room Dogwood; Xavier>Dalia>Wanjiru>Xavier=Room Dogwood]
- **inform** (tier None) At the end of the story, Amara wants everybody else on the team to share Amara's own view of which room the client workshop is booked in. Amara sends a direct message to every person who, as far as Amara can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Amara?
  
  gold: **Dalia, Wanjiru, Xavier**

## Scenario S002 (classic, 2 fact(s), 8 events, seed 1002000)

Ines, Amara, Chidi, Mirela and Zoltan are in the workshop. On the floor of the workshop there are four closed containers that nobody can see into: the wooden chest, the red box, the green cupboard and the black trunk. On a shelf there are four closed tins that nobody can see into: the round tin, the square tin, the flat tin and the tall tin. The tins are empty at the start, and the marble is only ever kept in the containers on the floor.
While everyone watches, Mirela puts a marble in the red box.
Mirela moves the marble to the green cupboard. Ines is in the workshop but is absorbed in a phone and does not notice this. Nobody realises that Ines missed it.
Amara leaves the workshop. Zoltan opens every container on the floor in full view of the workshop, showing that the marble is in the green cupboard. Amara is outside but watches all of this through the window. Nobody knows that Amara is watching.
Chidi and Zoltan leave the workshop. Amara comes back into the workshop. Amara takes a token out of a pocket and puts it in the round tin.
Mirela moves the token to the tall tin.
Ines moves the marble to the red box.
Amara wants to mislead Zoltan, so Amara sends Zoltan a private text message: “The marble is in the wooden chest.”
Chidi comes back into the workshop. Amara moves the token to the flat tin.
Mirela sends Zoltan a private text message: “The token is in the flat tin.”

- **reality** (tier None) At the end of the story, where is the marble really?
  A. the black trunk | B. the red box | C. the green cupboard | D. the wooden chest
  gold: **B**
- **k1-hard** (tier 2) At the end of the story, where does Chidi think the marble is?
  A. the red box | B. the green cupboard | C. the wooden chest | D. the black trunk
  gold: **B** [real=the red box; Chidi=the green cupboard]
- **act1** (tier 2) At the end of the story, Chidi needs the marble and goes to fetch it. Which container does Chidi open first?
  A. the red box | B. the green cupboard | C. the black trunk | D. the wooden chest
  gold: **B** [real=the red box; Chidi=the green cupboard]
- **k1-control** (tier 0) At the end of the story, where does Ines think the marble is?
  A. the green cupboard | B. the black trunk | C. the wooden chest | D. the red box
  gold: **D** [real=the red box; Ines=the red box]
- **k2-hard** (tier 3) At the end of the story, where does Zoltan think that Mirela thinks the marble is?
  A. the black trunk | B. the green cupboard | C. the red box | D. the wooden chest
  gold: **B** [real=the red box; Zoltan=the wooden chest; Zoltan>Mirela=the green cupboard]
- **act2** (tier 3) At the end of the story, Mirela is about to fetch the marble. Zoltan wants to be waiting beside the container that Mirela will open first, and must pick the spot before Mirela moves. Beside which container does Zoltan wait?
  A. the wooden chest | B. the black trunk | C. the red box | D. the green cupboard
  gold: **D** [real=the red box; Zoltan=the wooden chest; Zoltan>Mirela=the green cupboard]
- **k2-control** (tier 1) At the end of the story, where does Ines think that Chidi thinks the marble is?
  A. the black trunk | B. the wooden chest | C. the green cupboard | D. the red box
  gold: **C** [real=the red box; Ines=the red box; Ines>Chidi=the green cupboard]
- **k3-hard** (tier 3) At the end of the story, where does Mirela think that Amara thinks that Zoltan thinks the marble is?
  A. the red box | B. the wooden chest | C. the black trunk | D. the green cupboard
  gold: **D** [real=the red box; Mirela=the red box; Mirela>Amara=the red box; Mirela>Amara>Zoltan=the green cupboard]
- **k3-control** (tier 1) At the end of the story, where does Mirela think that Ines thinks that Chidi thinks the marble is?
  A. the green cupboard | B. the red box | C. the wooden chest | D. the black trunk
  gold: **A** [real=the red box; Mirela=the red box; Mirela>Ines=the red box; Mirela>Ines>Chidi=the green cupboard]
- **k4-hard** (tier 3) At the end of the story, where does Mirela think that Ines thinks that Amara thinks that Zoltan thinks the marble is?
  A. the wooden chest | B. the green cupboard | C. the black trunk | D. the red box
  gold: **B** [real=the red box; Mirela=the red box; Mirela>Ines=the red box; Mirela>Ines>Amara=the red box; Mirela>Ines>Amara>Zoltan=the green cupboard]
- **k4-control** (tier 0) At the end of the story, where does Ines think that Chidi thinks that Ines thinks that Amara thinks the token is?
  A. the tall tin | B. the flat tin | C. the round tin | D. the square tin
  gold: **B** [real=the flat tin; Ines=the flat tin; Ines>Chidi=the flat tin; Ines>Chidi>Ines=the flat tin; Ines>Chidi>Ines>Amara=the flat tin]
- **inform** (tier None) At the end of the story, Zoltan wants everybody else to share Zoltan's own view of where the marble is. Zoltan sends a private note to every person who, as far as Zoltan can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Zoltan?
  
  gold: **Chidi, Ines, Mirela**
- **know** (tier None) At the end of the story, where does Zoltan think that Ines thinks the token is?
  A. the tall tin | B. the round tin | C. the flat tin | D. the square tin | E. Zoltan thinks that Ines has no idea where the token is
  gold: **E** [real=the flat tin; Zoltan=the flat tin; Zoltan>Ines=no idea]

## Scenario S003 (workplace, 2 fact(s), 8 events, seed 1003000)

Ines, Nadim, Xavier, Hana and Viktor work on the same team. This is what happened, in order.
1. Call with Ines, Nadim, Xavier, Hana and Viktor: Hana fixes Ghent as the place for the team offsite.
2. Call with Nadim, Xavier and Viktor: Xavier moves the team offsite to Graz.
3. Xavier wants to mislead Ines, so Xavier sends Ines a direct message: “The team offsite is in Porto.”
4. Call with Ines, Xavier, Hana and Viktor: Viktor books the client workshop into Room Elm.
5. Viktor sends Hana a direct message: “The team offsite is in Graz.”
6. Call with Ines, Xavier, Hana and Viktor: Hana says: “The team offsite is in Graz.” Nadim is not on the call but secretly listens in, and can see who is on it. Nobody knows that Nadim is listening.
7. Viktor sends Nadim a direct message: “The client workshop is booked in Room Elm.”
8. Nadim sends Ines a direct message: “The client workshop is booked in Room Elm.” Viktor secretly reads this message on Ines's screen. Neither Nadim nor Ines ever knows that Viktor read it.
9. Call with Ines, Xavier, Hana and Viktor: Hana moves the team offsite to Turin.

- **reality** (tier None) At the end of the story, which city is the team offsite really in?
  A. Graz | B. Ghent | C. Porto | D. Turin
  gold: **D**
- **k1-hard** (tier 2) At the end of the story, which city does Nadim think the team offsite is in?
  A. Turin | B. Porto | C. Graz | D. Ghent
  gold: **C** [real=Turin; Nadim=Graz]
- **act1** (tier 2) At the end of the story, a new client asks Nadim which city the team offsite is in. Nadim answers honestly. What does Nadim say?
  A. Ghent | B. Porto | C. Turin | D. Graz
  gold: **D** [real=Turin; Nadim=Graz]
- **k1-control** (tier 0) At the end of the story, which city does Viktor think the team offsite is in?
  A. Porto | B. Turin | C. Graz | D. Ghent
  gold: **B** [real=Turin; Viktor=Turin]
- **k2-hard** (tier 3) At the end of the story, which city does Hana think that Nadim thinks the team offsite is in?
  A. Turin | B. Graz | C. Ghent | D. Porto
  gold: **C** [real=Turin; Hana=Turin; Hana>Nadim=Ghent]
- **act2** (tier 3) At the end of the story, a new client is about to ask Nadim which city the team offsite is in, and Nadim will answer honestly. Before Nadim answers, Hana writes down what Hana expects Nadim to say. What does Hana write?
  A. Graz | B. Ghent | C. Porto | D. Turin
  gold: **B** [real=Turin; Hana=Turin; Hana>Nadim=Ghent]
- **k2-control** (tier 1) At the end of the story, which city does Viktor think that Nadim thinks the team offsite is in?
  A. Turin | B. Ghent | C. Porto | D. Graz
  gold: **D** [real=Turin; Viktor=Turin; Viktor>Nadim=Graz]
- **k3-hard** (tier 3) At the end of the story, which city does Xavier think that Nadim thinks that Hana thinks the team offsite is in?
  A. Graz | B. Turin | C. Ghent | D. Porto
  gold: **C** [real=Turin; Xavier=Turin; Xavier>Nadim=Graz; Xavier>Nadim>Hana=Ghent]
- **k3-control** (tier 1) At the end of the story, which city does Viktor think that Xavier thinks that Nadim thinks the team offsite is in?
  A. Turin | B. Graz | C. Ghent | D. Porto
  gold: **B** [real=Turin; Viktor=Turin; Viktor>Xavier=Turin; Viktor>Xavier>Nadim=Graz]
- **k4-hard** (tier 3) At the end of the story, which city does Viktor think that Nadim thinks that Viktor thinks that Hana thinks the team offsite is in?
  A. Ghent | B. Graz | C. Turin | D. Porto
  gold: **A** [real=Turin; Viktor=Turin; Viktor>Nadim=Graz; Viktor>Nadim>Viktor=Graz; Viktor>Nadim>Viktor>Hana=Ghent]
- **k4-control** (tier 0) At the end of the story, which room does Xavier think that Viktor thinks that Hana thinks that Viktor thinks the client workshop is booked in?
  A. Room Birch | B. Room Elm | C. Room Cedar | D. Room Dogwood
  gold: **B** [real=Room Elm; Xavier=Room Elm; Xavier>Viktor=Room Elm; Xavier>Viktor>Hana=Room Elm; Xavier>Viktor>Hana>Viktor=Room Elm]
- **inform** (tier None) At the end of the story, Nadim wants everybody else on the team to share Nadim's own view of which room the client workshop is booked in. Nadim sends a direct message to every person who, as far as Nadim can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Nadim?
  
  gold: **Hana, Xavier**
- **know** (tier None) At the end of the story, which room does Nadim think that Hana thinks the client workshop is booked in?
  A. Room Cedar | B. Room Birch | C. Room Dogwood | D. Room Elm | E. Nadim thinks that Hana has no idea which room the client workshop is booked in
  gold: **E** [real=Room Elm; Nadim=Room Elm; Nadim>Hana=no idea]

## Scenario S004 (classic, 1 fact(s), 11 events, seed 1004000)

Goran, Quinn, Nadim, Viktor and Bruno are in the cellar. The cellar has four closed containers that nobody can see into: the wooden chest, the white cabinet, the wicker basket and the leather bag.
While everyone watches, Bruno puts a padlock in the white cabinet.
Quinn moves the padlock to the wicker basket.
Bruno leaves the cellar. Nadim moves the padlock to the leather bag.
Goran sends Bruno a private text message: “The padlock is in the leather bag.”
Nadim and Viktor leave the cellar. Quinn moves the padlock to the wooden chest.
Goran moves the padlock to the white cabinet. Quinn is in the cellar but is absorbed in a phone and does not notice this. Nobody realises that Quinn missed it. Viktor is outside but watches all of this through the window. Nobody knows that Viktor is watching.
Nadim sends Bruno a private text message: “The padlock is in the leather bag.”
Bruno sends Quinn a private text message: “The padlock is in the leather bag.”
Goran sends Nadim a private text message: “The padlock is in the white cabinet.”
Quinn opens every container in full view of the cellar, showing that the padlock is in the white cabinet.
Viktor sends Bruno a private text message: “The padlock is in the white cabinet.”
Goran moves the padlock to the wooden chest. Quinn is in the cellar but is absorbed in a phone and does not notice this. Nobody realises that Quinn missed it. Viktor is outside but watches all of this through the window. Nobody knows that Viktor is watching.

- **reality** (tier None) At the end of the story, where is the padlock really?
  A. the wooden chest | B. the white cabinet | C. the wicker basket | D. the leather bag
  gold: **A**
- **k1-hard** (tier 2) At the end of the story, where does Nadim think the padlock is?
  A. the wicker basket | B. the leather bag | C. the white cabinet | D. the wooden chest
  gold: **C** [real=the wooden chest; Nadim=the white cabinet]
- **act1** (tier 2) At the end of the story, Nadim needs the padlock and goes to fetch it. Which container does Nadim open first?
  A. the wicker basket | B. the wooden chest | C. the leather bag | D. the white cabinet
  gold: **D** [real=the wooden chest; Nadim=the white cabinet]
- **k1-control** (tier 0) At the end of the story, where does Viktor think the padlock is?
  A. the wicker basket | B. the leather bag | C. the wooden chest | D. the white cabinet
  gold: **C** [real=the wooden chest; Viktor=the wooden chest]
- **k2-hard** (tier 3) At the end of the story, where does Bruno think that Goran thinks the padlock is?
  A. the wooden chest | B. the leather bag | C. the white cabinet | D. the wicker basket
  gold: **B** [real=the wooden chest; Bruno=the white cabinet; Bruno>Goran=the leather bag]
- **act2** (tier 3) At the end of the story, Goran is about to fetch the padlock. Bruno wants to be waiting beside the container that Goran will open first, and must pick the spot before Goran moves. Beside which container does Bruno wait?
  A. the leather bag | B. the wicker basket | C. the white cabinet | D. the wooden chest
  gold: **A** [real=the wooden chest; Bruno=the white cabinet; Bruno>Goran=the leather bag]
- **k2-control** (tier 1) At the end of the story, where does Viktor think that Bruno thinks the padlock is?
  A. the wicker basket | B. the white cabinet | C. the leather bag | D. the wooden chest
  gold: **B** [real=the wooden chest; Viktor=the wooden chest; Viktor>Bruno=the white cabinet]
- **k3-hard** (tier 3) At the end of the story, where does Nadim think that Goran thinks that Bruno thinks the padlock is?
  A. the leather bag | B. the wooden chest | C. the wicker basket | D. the white cabinet
  gold: **C** [real=the wooden chest; Nadim=the white cabinet; Nadim>Goran=the white cabinet; Nadim>Goran>Bruno=the wicker basket]
- **k3-control** (tier 0) At the end of the story, where does Viktor think that Goran thinks that Quinn thinks the padlock is?
  A. the leather bag | B. the wicker basket | C. the white cabinet | D. the wooden chest
  gold: **D** [real=the wooden chest; Viktor=the wooden chest; Viktor>Goran=the wooden chest; Viktor>Goran>Quinn=the wooden chest]
- **k4-hard** (tier 2) At the end of the story, where does Quinn think that Nadim thinks that Viktor thinks that Nadim thinks the padlock is?
  A. the leather bag | B. the white cabinet | C. the wooden chest | D. the wicker basket
  gold: **A** [real=the wooden chest; Quinn=the white cabinet; Quinn>Nadim=the leather bag; Quinn>Nadim>Viktor=the leather bag; Quinn>Nadim>Viktor>Nadim=the leather bag]
- **k4-control** (tier 1) At the end of the story, where does Viktor think that Bruno thinks that Viktor thinks that Bruno thinks the padlock is?
  A. the white cabinet | B. the wooden chest | C. the leather bag | D. the wicker basket
  gold: **A** [real=the wooden chest; Viktor=the wooden chest; Viktor>Bruno=the white cabinet; Viktor>Bruno>Viktor=the white cabinet; Viktor>Bruno>Viktor>Bruno=the white cabinet]
- **inform** (tier None) At the end of the story, Nadim wants everybody else to share Nadim's own view of where the padlock is. Nadim sends a private note to every person who, as far as Nadim can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Nadim?
  
  gold: **Bruno, Quinn, Viktor**

## Scenario S005 (workplace, 1 fact(s), 11 events, seed 1005000)

Jonas, Goran, Uma, Dalia and Chidi work on the same team. This is what happened, in order.
1. Call with Jonas, Goran, Uma, Dalia and Chidi: Jonas assigns the Marlow account to the Denver office.
2. Call with Jonas, Goran, Uma, Dalia and Chidi: Jonas reassigns the Marlow account to the Osaka office. Uma is on the call but has stepped away from the desk and misses this. Nobody realises that Uma missed it.
3. Call with Jonas, Goran, Uma and Chidi: Goran opens the account list and reads it out: “The Marlow account is with the Osaka office.” Chidi is on the call but has stepped away from the desk and misses this. Nobody realises that Chidi missed it. Dalia is not on the call but secretly listens in, and can see who is on it. Nobody knows that Dalia is listening.
4. Call with Jonas, Goran, Uma and Chidi: Jonas reassigns the Marlow account to the Nairobi office. Uma is on the call but has stepped away from the desk and misses this. Nobody realises that Uma missed it.
5. Call with Jonas, Goran, Uma and Chidi: Uma reassigns the Marlow account to the Denver office.
6. Jonas wants to mislead Dalia, so Jonas sends Dalia a direct message: “The Marlow account is with the Nairobi office.”
7. Goran wants to mislead Dalia, so Goran sends Dalia a direct message: “The Marlow account is with the Lisbon office.”
8. Dalia wants to mislead Chidi, so Dalia sends Chidi a direct message: “The Marlow account is with the Denver office.” Goran secretly reads this message on Chidi's screen. Neither Dalia nor Chidi ever knows that Goran read it.
9. Call with Jonas, Goran, Uma and Chidi: Jonas reassigns the Marlow account to the Nairobi office.
10. Chidi sends Dalia a direct message: “The Marlow account is with the Nairobi office.”
11. Dalia sends Uma a direct message: “The Marlow account is with the Nairobi office.”
12. Call with Jonas, Uma and Chidi: Jonas reassigns the Marlow account to the Osaka office. Chidi is on the call but has stepped away from the desk and misses this. Nobody realises that Chidi missed it.

- **reality** (tier None) At the end of the story, which office really has the Marlow account?
  A. the Nairobi office | B. the Denver office | C. the Osaka office | D. the Lisbon office
  gold: **C**
- **k1-hard** (tier 2) At the end of the story, which office does Dalia think has the Marlow account?
  A. the Lisbon office | B. the Nairobi office | C. the Denver office | D. the Osaka office
  gold: **B** [real=the Osaka office; Dalia=the Nairobi office]
- **act1** (tier 2) At the end of the story, a new client asks Dalia which office has the Marlow account. Dalia answers honestly. What does Dalia say?
  A. the Lisbon office | B. the Denver office | C. the Nairobi office | D. the Osaka office
  gold: **C** [real=the Osaka office; Dalia=the Nairobi office]
- **k1-control** (tier 0) At the end of the story, which office does Uma think has the Marlow account?
  A. the Nairobi office | B. the Osaka office | C. the Denver office | D. the Lisbon office
  gold: **B** [real=the Osaka office; Uma=the Osaka office]
- **k2-hard** (tier 3) At the end of the story, which office does Dalia think that Goran thinks has the Marlow account?
  A. the Denver office | B. the Nairobi office | C. the Osaka office | D. the Lisbon office
  gold: **D** [real=the Osaka office; Dalia=the Nairobi office; Dalia>Goran=the Lisbon office]
- **act2** (tier 3) At the end of the story, a new client is about to ask Goran which office has the Marlow account, and Goran will answer honestly. Before Goran answers, Dalia writes down what Dalia expects Goran to say. What does Dalia write?
  A. the Nairobi office | B. the Lisbon office | C. the Denver office | D. the Osaka office
  gold: **B** [real=the Osaka office; Dalia=the Nairobi office; Dalia>Goran=the Lisbon office]
- **k2-control** (tier 0) At the end of the story, which office does Uma think that Jonas thinks has the Marlow account?
  A. the Lisbon office | B. the Osaka office | C. the Denver office | D. the Nairobi office
  gold: **B** [real=the Osaka office; Uma=the Osaka office; Uma>Jonas=the Osaka office]
- **k3-hard** (tier 3) At the end of the story, which office does Uma think that Dalia thinks that Chidi thinks has the Marlow account?
  A. the Denver office | B. the Lisbon office | C. the Nairobi office | D. the Osaka office
  gold: **A** [real=the Osaka office; Uma=the Osaka office; Uma>Dalia=the Nairobi office; Uma>Dalia>Chidi=the Denver office]
- **k3-control** (tier 1) At the end of the story, which office does Uma think that Jonas thinks that Goran thinks has the Marlow account?
  A. the Osaka office | B. the Lisbon office | C. the Nairobi office | D. the Denver office
  gold: **C** [real=the Osaka office; Uma=the Osaka office; Uma>Jonas=the Osaka office; Uma>Jonas>Goran=the Nairobi office]
- **k4-hard** (tier 3) At the end of the story, which office does Uma think that Dalia thinks that Uma thinks that Goran thinks has the Marlow account?
  A. the Lisbon office | B. the Denver office | C. the Nairobi office | D. the Osaka office
  gold: **B** [real=the Osaka office; Uma=the Osaka office; Uma>Dalia=the Nairobi office; Uma>Dalia>Uma=the Nairobi office; Uma>Dalia>Uma>Goran=the Denver office]
- **k4-control** (tier 1) At the end of the story, which office does Chidi think that Uma thinks that Chidi thinks that Goran thinks has the Marlow account?
  A. the Osaka office | B. the Nairobi office | C. the Denver office | D. the Lisbon office
  gold: **B** [real=the Osaka office; Chidi=the Nairobi office; Chidi>Uma=the Nairobi office; Chidi>Uma>Chidi=the Nairobi office; Chidi>Uma>Chidi>Goran=the Nairobi office]
- **inform** (tier None) At the end of the story, Dalia wants everybody else on the team to share Dalia's own view of which office has the Marlow account. Dalia sends a direct message to every person who, as far as Dalia can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Dalia?
  
  gold: **Goran**

## Scenario S006 (classic, 2 fact(s), 11 events, seed 1006001)

Rania, Bruno, Viktor, Uma and Farah are in the study. On the floor of the study there are four closed containers that nobody can see into: the canvas sack, the blue drawer, the black trunk and the wooden chest. On a shelf there are four closed tins that nobody can see into: the tall tin, the round tin, the striped tin and the flat tin. The tins are empty at the start, and the stopwatch is only ever kept in the containers on the floor.
While everyone watches, Uma puts a stopwatch in the wooden chest.
Viktor moves the stopwatch to the canvas sack.
Farah moves the stopwatch to the black trunk.
Viktor and Farah leave the study. Bruno takes a compass out of a pocket and puts it in the striped tin.
Uma leaves the study. Rania moves the stopwatch to the canvas sack. Bruno is in the study but is absorbed in a phone and does not notice this. Nobody realises that Bruno missed it. Viktor is outside but watches all of this through the window. Nobody knows that Viktor is watching.
Rania sends Viktor a private text message: “The stopwatch is in the canvas sack.” Farah secretly reads this message on Viktor's phone. Neither Rania nor Viktor ever knows that Farah read it.
Uma comes back into the study. Rania moves the stopwatch to the black trunk.
Rania leaves the study. Uma moves the compass to the flat tin.
Bruno moves the compass to the striped tin. Uma is in the study but is absorbed in a phone and does not notice this. Nobody realises that Uma missed it.
Rania sends Viktor a private text message: “The compass is in the striped tin.”
Uma leaves the study. Rania comes back into the study. Bruno moves the compass to the round tin.
Viktor sends Farah a private text message: “The stopwatch is in the canvas sack.”

- **reality** (tier None) At the end of the story, where is the compass really?
  A. the striped tin | B. the tall tin | C. the flat tin | D. the round tin
  gold: **D**
- **k1-hard** (tier 2) At the end of the story, where does Uma think the compass is?
  A. the flat tin | B. the striped tin | C. the round tin | D. the tall tin | E. Uma has no idea where the compass is
  gold: **A** [real=the round tin; Uma=the flat tin]
- **act1** (tier 2) At the end of the story, Uma needs the compass and goes to fetch it. Which container does Uma open first?
  A. the striped tin | B. the tall tin | C. the flat tin | D. the round tin
  gold: **C** [real=the round tin; Uma=the flat tin]
- **k1-control** (tier 0) At the end of the story, where does Bruno think the compass is?
  A. the round tin | B. the flat tin | C. the tall tin | D. the striped tin | E. Bruno has no idea where the compass is
  gold: **A** [real=the round tin; Bruno=the round tin]
- **k2-hard** (tier 3) At the end of the story, where does Bruno think that Uma thinks the compass is?
  A. the flat tin | B. the striped tin | C. the tall tin | D. the round tin | E. Bruno thinks that Uma has no idea where the compass is
  gold: **B** [real=the round tin; Bruno=the round tin; Bruno>Uma=the striped tin]
- **act2** (tier 3) At the end of the story, Uma is about to fetch the compass. Bruno wants to be waiting beside the container that Uma will open first, and must pick the spot before Uma moves. Beside which container does Bruno wait?
  A. the round tin | B. the flat tin | C. the striped tin | D. the tall tin
  gold: **C** [real=the round tin; Bruno=the round tin; Bruno>Uma=the striped tin]
- **k2-control** (tier 0) At the end of the story, where does Farah think that Uma thinks the stopwatch is?
  A. the canvas sack | B. the black trunk | C. the wooden chest | D. the blue drawer
  gold: **B** [real=the black trunk; Farah=the canvas sack; Farah>Uma=the black trunk]
- **k3-hard** (tier 3) At the end of the story, where does Uma think that Bruno thinks that Rania thinks the compass is?
  A. the tall tin | B. the striped tin | C. the flat tin | D. the round tin
  gold: **B** [real=the round tin; Uma=the flat tin; Uma>Bruno=the flat tin; Uma>Bruno>Rania=the striped tin]
- **k3-control** (tier 0) At the end of the story, where does Farah think that Rania thinks that Bruno thinks the stopwatch is?
  A. the blue drawer | B. the wooden chest | C. the black trunk | D. the canvas sack
  gold: **C** [real=the black trunk; Farah=the canvas sack; Farah>Rania=the canvas sack; Farah>Rania>Bruno=the black trunk]
- **k4-hard** (tier 2) At the end of the story, where does Uma think that Bruno thinks that Uma thinks that Bruno thinks the compass is?
  A. the striped tin | B. the round tin | C. the flat tin | D. the tall tin
  gold: **C** [real=the round tin; Uma=the flat tin; Uma>Bruno=the flat tin; Uma>Bruno>Uma=the flat tin; Uma>Bruno>Uma>Bruno=the flat tin]
- **k4-control** (tier 1) At the end of the story, where does Rania think that Viktor thinks that Rania thinks that Viktor thinks the compass is?
  A. the striped tin | B. the flat tin | C. the tall tin | D. the round tin
  gold: **A** [real=the round tin; Rania=the round tin; Rania>Viktor=the striped tin; Rania>Viktor>Rania=the striped tin; Rania>Viktor>Rania>Viktor=the striped tin]
- **inform** (tier None) At the end of the story, Viktor wants everybody else to share Viktor's own view of where the stopwatch is. Viktor sends a private note to every person who, as far as Viktor can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Viktor?
  
  gold: **Uma**
- **know** (tier None) At the end of the story, where does Farah think the compass is?
  A. the flat tin | B. the tall tin | C. the round tin | D. the striped tin | E. Farah has no idea where the compass is
  gold: **E** [real=the round tin; Farah=no idea]

## Scenario S007 (workplace, 2 fact(s), 11 events, seed 1007000)

Mirela, Zoltan, Bruno, Soren and Rania work on the same team. This is what happened, in order.
1. Call with Mirela, Zoltan, Bruno, Soren and Rania: Bruno assigns the Marlow account to the Lisbon office.
2. Call with Mirela, Bruno, Soren and Rania: Rania reassigns the Marlow account to the Denver office.
3. Call with Mirela, Bruno and Soren: Mirela reassigns the Marlow account to the Osaka office.
4. Call with Mirela, Bruno and Soren: Soren picks Ironbridge as the packaging supplier. Mirela is on the call but has stepped away from the desk and misses this. Nobody realises that Mirela missed it.
5. Call with Mirela, Bruno and Soren: Mirela reassigns the Marlow account to the Lisbon office.
6. Bruno wants to mislead Rania, so Bruno sends Rania a direct message: “The packaging supplier is Sablewood.”
7. Call with Mirela, Bruno and Soren: Bruno switches the packaging supplier to Sablewood.
8. Call with Mirela and Soren: Mirela switches the packaging supplier to Ironbridge.
9. Call with Mirela and Soren: Mirela switches the packaging supplier to Brightwater.
10. Mirela wants to mislead Rania, so Mirela sends Rania a direct message: “The Marlow account is with the Osaka office.”
11. Call with Mirela, Zoltan and Soren: Soren reassigns the Marlow account to the Nairobi office.
12. Call with Mirela, Zoltan and Soren: Soren reassigns the Marlow account to the Osaka office.

- **reality** (tier None) At the end of the story, which company is really the packaging supplier?
  A. Ironbridge | B. Brightwater | C. Northwind | D. Sablewood
  gold: **B**
- **k1-hard** (tier 2) At the end of the story, which company does Bruno think is the packaging supplier?
  A. Northwind | B. Ironbridge | C. Sablewood | D. Brightwater | E. Bruno has no idea which company is the packaging supplier
  gold: **C** [real=Brightwater; Bruno=Sablewood]
- **act1** (tier 2) At the end of the story, a new client asks Bruno which company is the packaging supplier. Bruno answers honestly. What does Bruno say?
  A. Sablewood | B. Brightwater | C. Ironbridge | D. Northwind
  gold: **A** [real=Brightwater; Bruno=Sablewood]
- **k1-control** (tier 0) At the end of the story, which office does Zoltan think has the Marlow account?
  A. the Lisbon office | B. the Denver office | C. the Nairobi office | D. the Osaka office
  gold: **D** [real=the Osaka office; Zoltan=the Osaka office]
- **k2-hard** (tier 3) At the end of the story, which office does Zoltan think that Rania thinks has the Marlow account?
  A. the Denver office | B. the Osaka office | C. the Nairobi office | D. the Lisbon office
  gold: **D** [real=the Osaka office; Zoltan=the Osaka office; Zoltan>Rania=the Lisbon office]
- **act2** (tier 3) At the end of the story, a new client is about to ask Rania which office has the Marlow account, and Rania will answer honestly. Before Rania answers, Zoltan writes down what Zoltan expects Rania to say. What does Zoltan write?
  A. the Nairobi office | B. the Denver office | C. the Lisbon office | D. the Osaka office
  gold: **C** [real=the Osaka office; Zoltan=the Osaka office; Zoltan>Rania=the Lisbon office]
- **k2-control** (tier 1) At the end of the story, which company does Soren think that Bruno thinks is the packaging supplier?
  A. Brightwater | B. Northwind | C. Sablewood | D. Ironbridge | E. Soren thinks that Bruno has no idea which company is the packaging supplier
  gold: **C** [real=Brightwater; Soren=Brightwater; Soren>Bruno=Sablewood]
- **k3-hard** (tier 3) At the end of the story, which office does Rania think that Mirela thinks that Soren thinks has the Marlow account?
  A. the Denver office | B. the Lisbon office | C. the Osaka office | D. the Nairobi office
  gold: **A** [real=the Osaka office; Rania=the Osaka office; Rania>Mirela=the Osaka office; Rania>Mirela>Soren=the Denver office]
- **k3-control** (tier 0) At the end of the story, which office does Zoltan think that Soren thinks that Zoltan thinks has the Marlow account?
  A. the Osaka office | B. the Denver office | C. the Lisbon office | D. the Nairobi office
  gold: **A** [real=the Osaka office; Zoltan=the Osaka office; Zoltan>Soren=the Osaka office; Zoltan>Soren>Zoltan=the Osaka office]
- **k4-hard** (tier 3) At the end of the story, which office does Rania think that Soren thinks that Mirela thinks that Zoltan thinks has the Marlow account?
  A. the Lisbon office | B. the Nairobi office | C. the Osaka office | D. the Denver office
  gold: **A** [real=the Osaka office; Rania=the Osaka office; Rania>Soren=the Denver office; Rania>Soren>Mirela=the Denver office; Rania>Soren>Mirela>Zoltan=the Lisbon office]
- **k4-control** (tier 0) At the end of the story, which office does Rania think that Mirela thinks that Rania thinks that Mirela thinks has the Marlow account?
  A. the Osaka office | B. the Nairobi office | C. the Denver office | D. the Lisbon office
  gold: **A** [real=the Osaka office; Rania=the Osaka office; Rania>Mirela=the Osaka office; Rania>Mirela>Rania=the Osaka office; Rania>Mirela>Rania>Mirela=the Osaka office]
- **inform** (tier None) At the end of the story, Zoltan wants everybody else on the team to share Zoltan's own view of which office has the Marlow account. Zoltan sends a direct message to every person who, as far as Zoltan can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Zoltan?
  
  gold: **Bruno, Rania**
- **know** (tier None) At the end of the story, which company does Zoltan think is the packaging supplier?
  A. Ironbridge | B. Northwind | C. Brightwater | D. Sablewood | E. Zoltan has no idea which company is the packaging supplier
  gold: **E** [real=Brightwater; Zoltan=no idea]

## Scenario S008 (classic, 1 fact(s), 14 events, seed 1008001)

Bruno, Viktor, Emeka, Oksana and Uma are in the boathouse. The boathouse has four closed containers that nobody can see into: the wicker basket, the green cupboard, the white cabinet and the grey locker.
While everyone watches, Uma puts a compass in the white cabinet.
Uma moves the compass to the grey locker.
Oksana moves the compass to the green cupboard.
Viktor and Emeka leave the boathouse. Uma moves the compass to the grey locker.
Bruno moves the compass to the wicker basket.
Bruno sends Emeka a private text message: “The compass is in the wicker basket.”
Oksana moves the compass to the grey locker.
Oksana sends Emeka a private text message: “The compass is in the grey locker.”
Bruno sends Viktor a private text message: “The compass is in the grey locker.”
Uma leaves the boathouse. Bruno moves the compass to the wicker basket. Oksana is in the boathouse but is absorbed in a phone and does not notice this. Nobody realises that Oksana missed it.
Bruno moves the compass to the grey locker.
Oksana moves the compass to the wicker basket.
Oksana moves the compass to the green cupboard. Emeka is outside but watches all of this through the window. Nobody knows that Emeka is watching.
Viktor comes back into the boathouse. Bruno moves the compass to the grey locker. Emeka is outside but watches all of this through the window. Nobody knows that Emeka is watching.
Uma comes back into the boathouse. Bruno moves the compass to the wicker basket.

- **reality** (tier None) At the end of the story, where is the compass really?
  A. the white cabinet | B. the grey locker | C. the green cupboard | D. the wicker basket
  gold: **D**
- **k1-hard** (tier 2) At the end of the story, where does Emeka think the compass is?
  A. the grey locker | B. the green cupboard | C. the white cabinet | D. the wicker basket
  gold: **A** [real=the wicker basket; Emeka=the grey locker]
- **act1** (tier 2) At the end of the story, Emeka needs the compass and goes to fetch it. Which container does Emeka open first?
  A. the wicker basket | B. the grey locker | C. the green cupboard | D. the white cabinet
  gold: **B** [real=the wicker basket; Emeka=the grey locker]
- **k1-control** (tier 0) At the end of the story, where does Oksana think the compass is?
  A. the green cupboard | B. the white cabinet | C. the grey locker | D. the wicker basket
  gold: **D** [real=the wicker basket; Oksana=the wicker basket]
- **k2-hard** (tier 3) At the end of the story, where does Uma think that Emeka thinks the compass is?
  A. the grey locker | B. the wicker basket | C. the green cupboard | D. the white cabinet
  gold: **C** [real=the wicker basket; Uma=the wicker basket; Uma>Emeka=the green cupboard]
- **act2** (tier 3) At the end of the story, Emeka is about to fetch the compass. Uma wants to be waiting beside the container that Emeka will open first, and must pick the spot before Emeka moves. Beside which container does Uma wait?
  A. the grey locker | B. the wicker basket | C. the white cabinet | D. the green cupboard
  gold: **D** [real=the wicker basket; Uma=the wicker basket; Uma>Emeka=the green cupboard]
- **k2-control** (tier 1) At the end of the story, where does Oksana think that Emeka thinks the compass is?
  A. the white cabinet | B. the green cupboard | C. the wicker basket | D. the grey locker
  gold: **D** [real=the wicker basket; Oksana=the wicker basket; Oksana>Emeka=the grey locker]
- **k3-hard** (tier 3) At the end of the story, where does Emeka think that Oksana thinks that Uma thinks the compass is?
  A. the green cupboard | B. the grey locker | C. the wicker basket | D. the white cabinet
  gold: **A** [real=the wicker basket; Emeka=the grey locker; Emeka>Oksana=the grey locker; Emeka>Oksana>Uma=the green cupboard]
- **k3-control** (tier 0) At the end of the story, where does Uma think that Bruno thinks that Viktor thinks the compass is?
  A. the white cabinet | B. the wicker basket | C. the green cupboard | D. the grey locker
  gold: **B** [real=the wicker basket; Uma=the wicker basket; Uma>Bruno=the wicker basket; Uma>Bruno>Viktor=the wicker basket]
- **k4-hard** (tier 3) At the end of the story, where does Emeka think that Viktor thinks that Oksana thinks that Uma thinks the compass is?
  A. the white cabinet | B. the grey locker | C. the wicker basket | D. the green cupboard
  gold: **D** [real=the wicker basket; Emeka=the grey locker; Emeka>Viktor=the grey locker; Emeka>Viktor>Oksana=the grey locker; Emeka>Viktor>Oksana>Uma=the green cupboard]
- **k4-control** (tier 1) At the end of the story, where does Oksana think that Emeka thinks that Oksana thinks that Emeka thinks the compass is?
  A. the grey locker | B. the white cabinet | C. the green cupboard | D. the wicker basket
  gold: **A** [real=the wicker basket; Oksana=the wicker basket; Oksana>Emeka=the grey locker; Oksana>Emeka>Oksana=the grey locker; Oksana>Emeka>Oksana>Emeka=the grey locker]
- **inform** (tier None) At the end of the story, Emeka wants everybody else to share Emeka's own view of where the compass is. Emeka sends a private note to every person who, as far as Emeka can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Emeka?
  
  gold: **Uma**

## Scenario S009 (workplace, 1 fact(s), 14 events, seed 1009000)

Jonas, Farah, Nadim, Hana and Yara work on the same team. This is what happened, in order.
1. Call with Jonas, Farah, Nadim, Hana and Yara: Nadim sets the product release for Thursday.
2. Call with Jonas, Farah, Nadim and Yara: Yara moves the product release to Monday.
3. Nadim wants to mislead Hana, so Nadim sends Hana a direct message: “The product release is set for Wednesday.”
4. Call with Jonas, Farah, Nadim and Yara: Nadim moves the product release to Thursday.
5. Call with Jonas, Farah, Nadim, Hana and Yara: Hana moves the product release to Wednesday.
6. Call with Jonas, Farah, Nadim, Hana and Yara: Jonas moves the product release to Thursday. Farah is on the call but has stepped away from the desk and misses this. Nobody realises that Farah missed it.
7. Call with Jonas, Farah, Hana and Yara: Farah moves the product release to Friday.
8. Farah sends Nadim a direct message: “The product release is set for Friday.”
9. Call with Jonas, Farah, Hana and Yara: Jonas moves the product release to Thursday.
10. Call with Jonas, Farah, Hana and Yara: Yara opens the release calendar and reads it out: “The product release is set for Thursday.” Nadim is not on the call but secretly listens in, and can see who is on it. Nobody knows that Nadim is listening.
11. Call with Jonas, Farah and Yara: Jonas moves the product release to Friday.
12. Farah sends Hana a direct message: “The product release is set for Friday.” Jonas secretly reads this message on Hana's screen. Neither Farah nor Hana ever knows that Jonas read it.
13. Call with Jonas and Farah: Farah moves the product release to Wednesday.
14. Jonas, working alone, moves the product release to Monday and tells nobody. Yara secretly watches Jonas's screen as this happens. Nobody knows that Yara is watching.
15. Jonas, working alone, moves the product release to Friday and tells nobody.

- **reality** (tier None) At the end of the story, which day is the product release really set for?
  A. Monday | B. Wednesday | C. Thursday | D. Friday
  gold: **D**
- **k1-hard** (tier 2) At the end of the story, which day does Nadim think the product release is set for?
  A. Monday | B. Friday | C. Thursday | D. Wednesday
  gold: **C** [real=Friday; Nadim=Thursday]
- **act1** (tier 2) At the end of the story, a new client asks Nadim which day the product release is set for. Nadim answers honestly. What does Nadim say?
  A. Wednesday | B. Monday | C. Thursday | D. Friday
  gold: **C** [real=Friday; Nadim=Thursday]
- **k1-control** (tier 0) At the end of the story, which day does Hana think the product release is set for?
  A. Friday | B. Thursday | C. Wednesday | D. Monday
  gold: **A** [real=Friday; Hana=Friday]
- **k2-hard** (tier 3) At the end of the story, which day does Hana think that Yara thinks the product release is set for?
  A. Friday | B. Thursday | C. Monday | D. Wednesday
  gold: **B** [real=Friday; Hana=Friday; Hana>Yara=Thursday]
- **act2** (tier 3) At the end of the story, a new client is about to ask Yara which day the product release is set for, and Yara will answer honestly. Before Yara answers, Hana writes down what Hana expects Yara to say. What does Hana write?
  A. Thursday | B. Wednesday | C. Friday | D. Monday
  gold: **A** [real=Friday; Hana=Friday; Hana>Yara=Thursday]
- **k2-control** (tier 1) At the end of the story, which day does Yara think that Nadim thinks the product release is set for?
  A. Monday | B. Wednesday | C. Thursday | D. Friday
  gold: **C** [real=Friday; Yara=Monday; Yara>Nadim=Thursday]
- **k3-hard** (tier 3) At the end of the story, which day does Farah think that Jonas thinks that Hana thinks the product release is set for?
  A. Friday | B. Monday | C. Wednesday | D. Thursday
  gold: **D** [real=Friday; Farah=Wednesday; Farah>Jonas=Wednesday; Farah>Jonas>Hana=Thursday]
- **k3-control** (tier 1) At the end of the story, which day does Hana think that Yara thinks that Nadim thinks the product release is set for?
  A. Friday | B. Wednesday | C. Thursday | D. Monday
  gold: **C** [real=Friday; Hana=Friday; Hana>Yara=Thursday; Hana>Yara>Nadim=Thursday]
- **k4-hard** (tier 3) At the end of the story, which day does Farah think that Yara thinks that Hana thinks that Nadim thinks the product release is set for?
  A. Friday | B. Monday | C. Wednesday | D. Thursday
  gold: **C** [real=Friday; Farah=Wednesday; Farah>Yara=Friday; Farah>Yara>Hana=Thursday; Farah>Yara>Hana>Nadim=Wednesday]
- **k4-control** (tier 0) At the end of the story, which day does Yara think that Farah thinks that Yara thinks that Jonas thinks the product release is set for?
  A. Wednesday | B. Thursday | C. Friday | D. Monday
  gold: **C** [real=Friday; Yara=Monday; Yara>Farah=Friday; Yara>Farah>Yara=Friday; Yara>Farah>Yara>Jonas=Friday]
- **inform** (tier None) At the end of the story, Yara wants everybody else on the team to share Yara's own view of which day the product release is set for. Yara sends a direct message to every person who, as far as Yara can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Yara?
  
  gold: **Farah, Hana, Nadim**

## Scenario S010 (classic, 2 fact(s), 14 events, seed 1010001)

Jonas, Ines, Mirela, Tariq and Wanjiru are in the kitchen. On the floor of the kitchen there are four closed containers that nobody can see into: the canvas sack, the green cupboard, the wooden chest and the grey locker. On a shelf there are four closed tins that nobody can see into: the copper tin, the square tin, the flat tin and the tall tin. The tins are empty at the start, and the torch is only ever kept in the containers on the floor.
While everyone watches, Ines puts a torch in the green cupboard.
Tariq moves the torch to the canvas sack.
Mirela leaves the kitchen. Jonas takes a brooch out of a pocket and puts it in the copper tin. Tariq is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Tariq missed it.
Wanjiru opens every tin on the shelf in full view of the kitchen, showing that the brooch is in the copper tin.
Tariq leaves the kitchen. Jonas moves the torch to the wooden chest.
Wanjiru moves the torch to the green cupboard.
Wanjiru leaves the kitchen. Tariq comes back into the kitchen. Jonas moves the brooch to the square tin. Ines is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Ines missed it.
Jonas opens every tin on the shelf in full view of the kitchen, showing that the brooch is in the square tin.
Tariq moves the torch to the wooden chest. Mirela is outside but watches all of this through the window. Nobody knows that Mirela is watching.
Jonas moves the brooch to the flat tin.
Tariq sends Wanjiru a private text message: “The torch is in the wooden chest.”
Jonas moves the torch to the canvas sack.
Ines leaves the kitchen. Tariq opens every tin on the shelf in full view of the kitchen, showing that the brooch is in the flat tin. Wanjiru is outside but watches all of this through the window. Nobody knows that Wanjiru is watching.
Ines comes back into the kitchen. Tariq moves the brooch to the tall tin.
Wanjiru sends Mirela a private text message: “The brooch is in the flat tin.”

- **reality** (tier None) At the end of the story, where is the brooch really?
  A. the square tin | B. the copper tin | C. the flat tin | D. the tall tin
  gold: **D**
- **k1-hard** (tier 2) At the end of the story, where does Wanjiru think the brooch is?
  A. the copper tin | B. the flat tin | C. the tall tin | D. the square tin | E. Wanjiru has no idea where the brooch is
  gold: **B** [real=the tall tin; Wanjiru=the flat tin]
- **act1** (tier 2) At the end of the story, Wanjiru needs the brooch and goes to fetch it. Which container does Wanjiru open first?
  A. the flat tin | B. the copper tin | C. the tall tin | D. the square tin
  gold: **A** [real=the tall tin; Wanjiru=the flat tin]
- **k1-control** (tier 0) At the end of the story, where does Ines think the torch is?
  A. the canvas sack | B. the wooden chest | C. the grey locker | D. the green cupboard
  gold: **A** [real=the canvas sack; Ines=the canvas sack]
- **k2-hard** (tier 3) At the end of the story, where does Ines think that Wanjiru thinks the brooch is?
  A. the square tin | B. the copper tin | C. the flat tin | D. the tall tin | E. Ines thinks that Wanjiru has no idea where the brooch is
  gold: **B** [real=the tall tin; Ines=the tall tin; Ines>Wanjiru=the copper tin]
- **act2** (tier 3) At the end of the story, Wanjiru is about to fetch the brooch. Ines wants to be waiting beside the container that Wanjiru will open first, and must pick the spot before Wanjiru moves. Beside which container does Ines wait?
  A. the copper tin | B. the flat tin | C. the tall tin | D. the square tin
  gold: **A** [real=the tall tin; Ines=the tall tin; Ines>Wanjiru=the copper tin]
- **k2-control** (tier 0) At the end of the story, where does Tariq think that Jonas thinks the brooch is?
  A. the flat tin | B. the copper tin | C. the square tin | D. the tall tin | E. Tariq thinks that Jonas has no idea where the brooch is
  gold: **D** [real=the tall tin; Tariq=the tall tin; Tariq>Jonas=the tall tin]
- **k3-hard** (tier 3) At the end of the story, where does Wanjiru think that Tariq thinks that Ines thinks the brooch is?
  A. the square tin | B. the tall tin | C. the flat tin | D. the copper tin
  gold: **D** [real=the tall tin; Wanjiru=the flat tin; Wanjiru>Tariq=the flat tin; Wanjiru>Tariq>Ines=the copper tin]
- **k3-control** (tier 0) At the end of the story, where does Mirela think that Wanjiru thinks that Mirela thinks the torch is?
  A. the green cupboard | B. the grey locker | C. the canvas sack | D. the wooden chest
  gold: **C** [real=the canvas sack; Mirela=the wooden chest; Mirela>Wanjiru=the canvas sack; Mirela>Wanjiru>Mirela=the canvas sack]
- **k4-hard** (tier 3) At the end of the story, where does Wanjiru think that Jonas thinks that Tariq thinks that Ines thinks the brooch is?
  A. the flat tin | B. the square tin | C. the tall tin | D. the copper tin
  gold: **D** [real=the tall tin; Wanjiru=the flat tin; Wanjiru>Jonas=the flat tin; Wanjiru>Jonas>Tariq=the flat tin; Wanjiru>Jonas>Tariq>Ines=the copper tin]
- **k4-control** (tier 0) At the end of the story, where does Wanjiru think that Tariq thinks that Ines thinks that Mirela thinks the torch is?
  A. the green cupboard | B. the canvas sack | C. the grey locker | D. the wooden chest
  gold: **B** [real=the canvas sack; Wanjiru=the wooden chest; Wanjiru>Tariq=the wooden chest; Wanjiru>Tariq>Ines=the canvas sack; Wanjiru>Tariq>Ines>Mirela=the canvas sack]
- **inform** (tier None) At the end of the story, Wanjiru wants everybody else to share Wanjiru's own view of where the torch is. Wanjiru sends a private note to every person who, as far as Wanjiru can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Wanjiru?
  
  gold: **Ines, Jonas, Mirela**
- **know** (tier None) At the end of the story, where does Mirela think that Jonas thinks the brooch is?
  A. the flat tin | B. the copper tin | C. the tall tin | D. the square tin | E. Mirela thinks that Jonas has no idea where the brooch is
  gold: **E** [real=the tall tin; Mirela=the flat tin; Mirela>Jonas=no idea]

## Scenario S011 (workplace, 2 fact(s), 14 events, seed 1011001)

Goran, Tariq, Jonas, Xavier and Ines work on the same team. This is what happened, in order.
1. Call with Goran, Tariq, Jonas, Xavier and Ines: Jonas assigns the Marlow account to the Nairobi office.
2. Call with Goran, Jonas, Xavier and Ines: Ines reassigns the Marlow account to the Osaka office.
3. Goran sends Tariq a direct message: “The Marlow account is with the Osaka office.”
4. Call with Goran and Xavier: Goran sets the product release for Wednesday.
5. Call with Goran, Xavier and Ines: Goran moves the product release to Friday. Ines is on the call but has stepped away from the desk and misses this. Nobody realises that Ines missed it.
6. Call with Goran, Xavier and Ines: Xavier moves the product release to Wednesday.
7. Call with Goran and Xavier: Goran reassigns the Marlow account to the Denver office. Xavier is on the call but has stepped away from the desk and misses this. Nobody realises that Xavier missed it.
8. Call with Goran and Xavier: Xavier moves the product release to Thursday. Goran is on the call but has stepped away from the desk and misses this. Nobody realises that Goran missed it. Tariq is not on the call but secretly listens in, and can see who is on it. Nobody knows that Tariq is listening.
9. Xavier sends Jonas a direct message: “The product release is set for Thursday.” Ines secretly reads this message on Jonas's screen. Neither Xavier nor Jonas ever knows that Ines read it.
10. Tariq wants to mislead Xavier, so Tariq sends Xavier a direct message: “The Marlow account is with the Denver office.”
11. Call with Goran and Xavier: Xavier opens the release calendar and reads it out: “The product release is set for Thursday.”
12. Ines sends Tariq a direct message: “The Marlow account is with the Osaka office.” Jonas secretly reads this message on Tariq's screen. Neither Ines nor Tariq ever knows that Jonas read it.
13. Call with Goran and Xavier: Goran moves the product release to Wednesday.
14. Xavier wants to mislead Jonas, so Xavier sends Jonas a direct message: “The Marlow account is with the Nairobi office.”
15. Tariq sends Jonas a direct message: “The Marlow account is with the Osaka office.” Ines secretly reads this message on Jonas's screen. Neither Tariq nor Jonas ever knows that Ines read it.

- **reality** (tier None) At the end of the story, which office really has the Marlow account?
  A. the Denver office | B. the Osaka office | C. the Lisbon office | D. the Nairobi office
  gold: **A**
- **k1-hard** (tier 2) At the end of the story, which office does Tariq think has the Marlow account?
  A. the Nairobi office | B. the Lisbon office | C. the Denver office | D. the Osaka office
  gold: **D** [real=the Denver office; Tariq=the Osaka office]
- **act1** (tier 2) At the end of the story, a new client asks Tariq which office has the Marlow account. Tariq answers honestly. What does Tariq say?
  A. the Osaka office | B. the Lisbon office | C. the Denver office | D. the Nairobi office
  gold: **A** [real=the Denver office; Tariq=the Osaka office]
- **k1-control** (tier 0) At the end of the story, which day does Xavier think the product release is set for?
  A. Friday | B. Thursday | C. Wednesday | D. Tuesday | E. Xavier has no idea which day the product release is set for
  gold: **C** [real=Wednesday; Xavier=Wednesday]
- **k2-hard** (tier 3) At the end of the story, which office does Xavier think that Goran thinks has the Marlow account?
  A. the Denver office | B. the Nairobi office | C. the Lisbon office | D. the Osaka office
  gold: **D** [real=the Denver office; Xavier=the Denver office; Xavier>Goran=the Osaka office]
- **act2** (tier 3) At the end of the story, a new client is about to ask Goran which office has the Marlow account, and Goran will answer honestly. Before Goran answers, Xavier writes down what Xavier expects Goran to say. What does Xavier write?
  A. the Nairobi office | B. the Osaka office | C. the Denver office | D. the Lisbon office
  gold: **B** [real=the Denver office; Xavier=the Denver office; Xavier>Goran=the Osaka office]
- **k2-control** (tier 1) At the end of the story, which office does Jonas think that Tariq thinks has the Marlow account?
  A. the Osaka office | B. the Denver office | C. the Nairobi office | D. the Lisbon office
  gold: **A** [real=the Denver office; Jonas=the Osaka office; Jonas>Tariq=the Osaka office]
- **k3-hard** (tier 3) At the end of the story, which office does Jonas think that Goran thinks that Tariq thinks has the Marlow account?
  A. the Lisbon office | B. the Osaka office | C. the Denver office | D. the Nairobi office
  gold: **D** [real=the Denver office; Jonas=the Osaka office; Jonas>Goran=the Osaka office; Jonas>Goran>Tariq=the Nairobi office]
- **k3-control** (tier 0) At the end of the story, which day does Xavier think that Goran thinks that Xavier thinks the product release is set for?
  A. Wednesday | B. Thursday | C. Tuesday | D. Friday
  gold: **A** [real=Wednesday; Xavier=Wednesday; Xavier>Goran=Wednesday; Xavier>Goran>Xavier=Wednesday]
- **k4-hard** (tier 3) At the end of the story, which office does Xavier think that Ines thinks that Jonas thinks that Tariq thinks has the Marlow account?
  A. the Nairobi office | B. the Denver office | C. the Lisbon office | D. the Osaka office
  gold: **A** [real=the Denver office; Xavier=the Denver office; Xavier>Ines=the Osaka office; Xavier>Ines>Jonas=the Osaka office; Xavier>Ines>Jonas>Tariq=the Nairobi office]
- **k4-control** (tier 0) At the end of the story, which day does Goran think that Xavier thinks that Ines thinks that Xavier thinks the product release is set for?
  A. Thursday | B. Tuesday | C. Wednesday | D. Friday
  gold: **C** [real=Wednesday; Goran=Wednesday; Goran>Xavier=Wednesday; Goran>Xavier>Ines=Wednesday; Goran>Xavier>Ines>Xavier=Wednesday]
- **inform** (tier None) At the end of the story, Ines wants everybody else on the team to share Ines's own view of which day the product release is set for. Ines sends a direct message to every person who, as far as Ines can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Ines?
  
  gold: **Goran, Tariq**
- **know** (tier None) At the end of the story, which day does Ines think that Tariq thinks the product release is set for?
  A. Friday | B. Thursday | C. Wednesday | D. Tuesday | E. Ines thinks that Tariq has no idea which day the product release is set for
  gold: **E** [real=Wednesday; Ines=Thursday; Ines>Tariq=no idea]

## Scenario S012 (classic, 1 fact(s), 8 events, seed 1012001)

Keiko, Dalia, Nadim, Soren and Viktor are in the pantry. The pantry has four closed containers that nobody can see into: the black trunk, the green cupboard, the red box and the blue drawer.
While everyone watches, Dalia puts a thimble in the black trunk.
Dalia and Viktor leave the pantry. Nadim moves the thimble to the green cupboard. Viktor is outside but watches all of this through the window. Nobody knows that Viktor is watching.
Nadim sends Dalia a private text message: “The thimble is in the green cupboard.”
Dalia sends Keiko a private text message: “The thimble is in the green cupboard.”
Nadim sends Viktor a private text message: “The thimble is in the green cupboard.”
Viktor comes back into the pantry. Keiko moves the thimble to the blue drawer. Soren is in the pantry but is absorbed in a phone and does not notice this. Nobody realises that Soren missed it.
Keiko leaves the pantry. Soren moves the thimble to the green cupboard.
Dalia sends Viktor a private text message: “The thimble is in the green cupboard.”
Soren leaves the pantry. Dalia comes back into the pantry. Nadim moves the thimble to the blue drawer. Keiko is outside but watches all of this through the window. Nobody knows that Keiko is watching.

- **reality** (tier None) At the end of the story, where is the thimble really?
  A. the black trunk | B. the green cupboard | C. the blue drawer | D. the red box
  gold: **C**
- **k1-hard** (tier 2) At the end of the story, where does Soren think the thimble is?
  A. the green cupboard | B. the red box | C. the blue drawer | D. the black trunk
  gold: **A** [real=the blue drawer; Soren=the green cupboard]
- **act1** (tier 2) At the end of the story, Soren needs the thimble and goes to fetch it. Which container does Soren open first?
  A. the blue drawer | B. the red box | C. the green cupboard | D. the black trunk
  gold: **C** [real=the blue drawer; Soren=the green cupboard]
- **k1-control** (tier 0) At the end of the story, where does Keiko think the thimble is?
  A. the blue drawer | B. the red box | C. the black trunk | D. the green cupboard
  gold: **A** [real=the blue drawer; Keiko=the blue drawer]
- **k2-hard** (tier 3) At the end of the story, where does Dalia think that Soren thinks the thimble is?
  A. the red box | B. the black trunk | C. the blue drawer | D. the green cupboard
  gold: **B** [real=the blue drawer; Dalia=the blue drawer; Dalia>Soren=the black trunk]
- **act2** (tier 3) At the end of the story, Soren is about to fetch the thimble. Dalia wants to be waiting beside the container that Soren will open first, and must pick the spot before Soren moves. Beside which container does Dalia wait?
  A. the green cupboard | B. the red box | C. the blue drawer | D. the black trunk
  gold: **D** [real=the blue drawer; Dalia=the blue drawer; Dalia>Soren=the black trunk]
- **k2-control** (tier 0) At the end of the story, where does Keiko think that Soren thinks the thimble is?
  A. the green cupboard | B. the blue drawer | C. the black trunk | D. the red box
  gold: **B** [real=the blue drawer; Keiko=the blue drawer; Keiko>Soren=the blue drawer]
- **k3-hard** (tier 3) At the end of the story, where does Dalia think that Nadim thinks that Keiko thinks the thimble is?
  A. the green cupboard | B. the blue drawer | C. the black trunk | D. the red box
  gold: **C** [real=the blue drawer; Dalia=the blue drawer; Dalia>Nadim=the blue drawer; Dalia>Nadim>Keiko=the black trunk]
- **k3-control** (tier 0) At the end of the story, where does Nadim think that Dalia thinks that Nadim thinks the thimble is?
  A. the green cupboard | B. the red box | C. the blue drawer | D. the black trunk
  gold: **C** [real=the blue drawer; Nadim=the blue drawer; Nadim>Dalia=the blue drawer; Nadim>Dalia>Nadim=the blue drawer]
- **k4-hard** (tier 3) At the end of the story, where does Dalia think that Viktor thinks that Nadim thinks that Keiko thinks the thimble is?
  A. the red box | B. the blue drawer | C. the black trunk | D. the green cupboard
  gold: **C** [real=the blue drawer; Dalia=the blue drawer; Dalia>Viktor=the blue drawer; Dalia>Viktor>Nadim=the blue drawer; Dalia>Viktor>Nadim>Keiko=the black trunk]
- **k4-control** (tier 0) At the end of the story, where does Keiko think that Nadim thinks that Keiko thinks that Soren thinks the thimble is?
  A. the blue drawer | B. the red box | C. the green cupboard | D. the black trunk
  gold: **A** [real=the blue drawer; Keiko=the blue drawer; Keiko>Nadim=the blue drawer; Keiko>Nadim>Keiko=the blue drawer; Keiko>Nadim>Keiko>Soren=the blue drawer]
- **inform** (tier None) At the end of the story, Dalia wants everybody else to share Dalia's own view of where the thimble is. Dalia sends a private note to every person who, as far as Dalia can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Dalia?
  
  gold: **Keiko, Soren**

## Scenario S013 (workplace, 1 fact(s), 8 events, seed 1013001)

Xavier, Mirela, Farah, Ines and Keiko work on the same team. This is what happened, in order.
1. Call with Xavier, Mirela, Farah, Ines and Keiko: Mirela sets the discount on the Fenwick quote at 10%.
2. Call with Xavier, Mirela, Farah, Ines and Keiko: Keiko changes the discount on the Fenwick quote to 5%.
3. Call with Xavier, Mirela, Farah, Ines and Keiko: Xavier changes the discount on the Fenwick quote to 10%.
4. Call with Xavier, Mirela, Farah, Ines and Keiko: Farah changes the discount on the Fenwick quote to 20%. Xavier is on the call but has stepped away from the desk and misses this. Nobody realises that Xavier missed it.
5. Call with Xavier, Mirela, Farah, Ines and Keiko: Xavier changes the discount on the Fenwick quote to 5%.
6. Call with Xavier, Mirela, Farah, Ines and Keiko: Mirela changes the discount on the Fenwick quote to 20%. Keiko is on the call but has stepped away from the desk and misses this. Nobody realises that Keiko missed it.
7. Call with Xavier, Mirela, Farah, Ines and Keiko: Ines changes the discount on the Fenwick quote to 5%.
8. Call with Mirela, Farah, Ines and Keiko: Mirela changes the discount on the Fenwick quote to 20%. Xavier is not on the call but secretly listens in, and can see who is on it. Nobody knows that Xavier is listening.
9. Call with Farah and Keiko: Keiko changes the discount on the Fenwick quote to 10%.

- **reality** (tier None) At the end of the story, what discount is really on the Fenwick quote?
  A. 15% | B. 20% | C. 5% | D. 10%
  gold: **D**
- **k1-hard** (tier 2) At the end of the story, what discount does Xavier think is on the Fenwick quote?
  A. 10% | B. 15% | C. 5% | D. 20%
  gold: **D** [real=10%; Xavier=20%]
- **act1** (tier 2) At the end of the story, a new client asks Xavier what discount is on the Fenwick quote. Xavier answers honestly. What does Xavier say?
  A. 10% | B. 15% | C. 20% | D. 5%
  gold: **C** [real=10%; Xavier=20%]
- **k1-control** (tier 0) At the end of the story, what discount does Farah think is on the Fenwick quote?
  A. 15% | B. 10% | C. 5% | D. 20%
  gold: **B** [real=10%; Farah=10%]
- **k2-hard** (tier 3) At the end of the story, what discount does Farah think that Xavier thinks is on the Fenwick quote?
  A. 10% | B. 20% | C. 15% | D. 5%
  gold: **D** [real=10%; Farah=10%; Farah>Xavier=5%]
- **act2** (tier 3) At the end of the story, a new client is about to ask Xavier what discount is on the Fenwick quote, and Xavier will answer honestly. Before Xavier answers, Farah writes down what Farah expects Xavier to say. What does Farah write?
  A. 5% | B. 15% | C. 10% | D. 20%
  gold: **A** [real=10%; Farah=10%; Farah>Xavier=5%]
- **k2-control** (tier 1) At the end of the story, what discount does Xavier think that Mirela thinks is on the Fenwick quote?
  A. 15% | B. 5% | C. 20% | D. 10%
  gold: **C** [real=10%; Xavier=20%; Xavier>Mirela=20%]
- **k3-hard** (tier 2) At the end of the story, what discount does Xavier think that Keiko thinks that Farah thinks is on the Fenwick quote?
  A. 15% | B. 20% | C. 5% | D. 10%
  gold: **B** [real=10%; Xavier=20%; Xavier>Keiko=20%; Xavier>Keiko>Farah=20%]
- **k3-control** (tier 0) At the end of the story, what discount does Farah think that Keiko thinks that Farah thinks is on the Fenwick quote?
  A. 5% | B. 15% | C. 20% | D. 10%
  gold: **D** [real=10%; Farah=10%; Farah>Keiko=10%; Farah>Keiko>Farah=10%]
- **k4-hard** (tier 2) At the end of the story, what discount does Mirela think that Farah thinks that Xavier thinks that Keiko thinks is on the Fenwick quote?
  A. 10% | B. 5% | C. 15% | D. 20%
  gold: **B** [real=10%; Mirela=20%; Mirela>Farah=20%; Mirela>Farah>Xavier=5%; Mirela>Farah>Xavier>Keiko=5%]
- **k4-control** (tier 1) At the end of the story, what discount does Xavier think that Ines thinks that Mirela thinks that Ines thinks is on the Fenwick quote?
  A. 10% | B. 20% | C. 15% | D. 5%
  gold: **B** [real=10%; Xavier=20%; Xavier>Ines=20%; Xavier>Ines>Mirela=20%; Xavier>Ines>Mirela>Ines=20%]
- **inform** (tier None) At the end of the story, Ines wants everybody else on the team to share Ines's own view of what discount is on the Fenwick quote. Ines sends a direct message to every person who, as far as Ines can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Ines?
  
  gold: **Xavier**

## Scenario S014 (classic, 2 fact(s), 8 events, seed 1014002)

Ines, Keiko, Xavier, Wanjiru and Rania are in the sunroom. On the floor of the sunroom there are four closed containers that nobody can see into: the red box, the wooden chest, the black trunk and the wicker basket. On a shelf there are four closed tins that nobody can see into: the striped tin, the tall tin, the round tin and the square tin. The tins are empty at the start, and the marble is only ever kept in the containers on the floor.
While everyone watches, Ines puts a marble in the wooden chest.
Ines moves the marble to the black trunk.
Wanjiru and Rania leave the sunroom. Keiko takes a thimble out of a pocket and puts it in the round tin.
Rania comes back into the sunroom. Rania moves the thimble to the tall tin.
Xavier and Rania leave the sunroom. Ines moves the marble to the red box.
Ines sends Wanjiru a private text message: “The thimble is in the tall tin.”
Ines moves the marble to the wooden chest. Xavier is outside but watches all of this through the window. Nobody knows that Xavier is watching.
Ines leaves the sunroom. Keiko moves the thimble to the striped tin.
Rania comes back into the sunroom. Keiko moves the marble to the wicker basket. Wanjiru is outside but watches all of this through the window. Nobody knows that Wanjiru is watching.

- **reality** (tier None) At the end of the story, where is the marble really?
  A. the red box | B. the black trunk | C. the wicker basket | D. the wooden chest
  gold: **C**
- **k1-hard** (tier 2) At the end of the story, where does Rania think the thimble is?
  A. the round tin | B. the striped tin | C. the square tin | D. the tall tin | E. Rania has no idea where the thimble is
  gold: **D** [real=the striped tin; Rania=the tall tin]
- **act1** (tier 2) At the end of the story, Rania needs the thimble and goes to fetch it. Which container does Rania open first?
  A. the tall tin | B. the square tin | C. the round tin | D. the striped tin
  gold: **A** [real=the striped tin; Rania=the tall tin]
- **k1-control** (tier 0) At the end of the story, where does Keiko think the thimble is?
  A. the square tin | B. the striped tin | C. the tall tin | D. the round tin | E. Keiko has no idea where the thimble is
  gold: **B** [real=the striped tin; Keiko=the striped tin]
- **k2-hard** (tier 3) At the end of the story, where does Rania think that Wanjiru thinks the marble is?
  A. the wicker basket | B. the red box | C. the black trunk | D. the wooden chest
  gold: **C** [real=the wicker basket; Rania=the wicker basket; Rania>Wanjiru=the black trunk]
- **act2** (tier 3) At the end of the story, Wanjiru is about to fetch the marble. Rania wants to be waiting beside the container that Wanjiru will open first, and must pick the spot before Wanjiru moves. Beside which container does Rania wait?
  A. the red box | B. the black trunk | C. the wooden chest | D. the wicker basket
  gold: **B** [real=the wicker basket; Rania=the wicker basket; Rania>Wanjiru=the black trunk]
- **k2-control** (tier 0) At the end of the story, where does Wanjiru think that Keiko thinks the marble is?
  A. the wicker basket | B. the black trunk | C. the wooden chest | D. the red box
  gold: **A** [real=the wicker basket; Wanjiru=the wicker basket; Wanjiru>Keiko=the wicker basket]
- **k3-hard** (tier 3) At the end of the story, where does Wanjiru think that Keiko thinks that Ines thinks the marble is?
  A. the wicker basket | B. the red box | C. the black trunk | D. the wooden chest
  gold: **C** [real=the wicker basket; Wanjiru=the wicker basket; Wanjiru>Keiko=the wicker basket; Wanjiru>Keiko>Ines=the black trunk]
- **k3-control** (tier 1) At the end of the story, where does Keiko think that Rania thinks that Ines thinks the thimble is?
  A. the square tin | B. the striped tin | C. the round tin | D. the tall tin
  gold: **D** [real=the striped tin; Keiko=the striped tin; Keiko>Rania=the tall tin; Keiko>Rania>Ines=the tall tin]
- **k4-hard** (tier 2) At the end of the story, where does Xavier think that Keiko thinks that Xavier thinks that Ines thinks the marble is?
  A. the red box | B. the black trunk | C. the wicker basket | D. the wooden chest
  gold: **B** [real=the wicker basket; Xavier=the wooden chest; Xavier>Keiko=the wooden chest; Xavier>Keiko>Xavier=the black trunk; Xavier>Keiko>Xavier>Ines=the black trunk]
- **k4-control** (tier 1) At the end of the story, where does Xavier think that Ines thinks that Keiko thinks that Ines thinks the thimble is?
  A. the square tin | B. the round tin | C. the tall tin | D. the striped tin
  gold: **C** [real=the striped tin; Xavier=the tall tin; Xavier>Ines=the tall tin; Xavier>Ines>Keiko=the tall tin; Xavier>Ines>Keiko>Ines=the tall tin]
- **inform** (tier None) At the end of the story, Wanjiru wants everybody else to share Wanjiru's own view of where the thimble is. Wanjiru sends a private note to every person who, as far as Wanjiru can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Wanjiru?
  
  gold: **Keiko, Rania, Xavier**
- **know** (tier None) At the end of the story, where does Rania think that Wanjiru thinks the thimble is?
  A. the tall tin | B. the square tin | C. the round tin | D. the striped tin | E. Rania thinks that Wanjiru has no idea where the thimble is
  gold: **E** [real=the striped tin; Rania=the tall tin; Rania>Wanjiru=no idea]

## Scenario S015 (workplace, 2 fact(s), 8 events, seed 1015000)

Dalia, Quinn, Xavier, Mirela and Goran work on the same team. This is what happened, in order.
1. Call with Dalia, Quinn, Xavier, Mirela and Goran: Xavier assigns the Marlow account to the Nairobi office.
2. Call with Quinn, Xavier, Mirela and Goran: Quinn reassigns the Marlow account to the Lisbon office.
3. Goran sends Dalia a direct message: “The Marlow account is with the Lisbon office.”
4. Call with Dalia, Xavier, Mirela and Goran: Dalia sets the discount on the Fenwick quote at 25%. Quinn is not on the call but secretly listens in, and can see who is on it. Nobody knows that Quinn is listening.
5. Call with Xavier and Goran: Goran changes the discount on the Fenwick quote to 20%.
6. Quinn sends Dalia a direct message: “The Marlow account is with the Lisbon office.” Xavier secretly reads this message on Dalia's screen. Neither Quinn nor Dalia ever knows that Xavier read it.
7. Dalia sends Xavier a direct message: “The Marlow account is with the Lisbon office.”
8. Call with Dalia, Xavier and Goran: Xavier reassigns the Marlow account to the Osaka office.
9. Call with Dalia, Xavier, Mirela and Goran: Xavier reassigns the Marlow account to the Lisbon office.

- **reality** (tier None) At the end of the story, what discount is really on the Fenwick quote?
  A. 20% | B. 25% | C. 5% | D. 15%
  gold: **A**
- **k1-hard** (tier 2) At the end of the story, what discount does Mirela think is on the Fenwick quote?
  A. 25% | B. 15% | C. 5% | D. 20% | E. Mirela has no idea what discount is on the Fenwick quote
  gold: **A** [real=20%; Mirela=25%]
- **act1** (tier 2) At the end of the story, a new client asks Mirela what discount is on the Fenwick quote. Mirela answers honestly. What does Mirela say?
  A. 25% | B. 20% | C. 5% | D. 15%
  gold: **A** [real=20%; Mirela=25%]
- **k1-control** (tier 0) At the end of the story, what discount does Xavier think is on the Fenwick quote?
  A. 25% | B. 20% | C. 5% | D. 15% | E. Xavier has no idea what discount is on the Fenwick quote
  gold: **B** [real=20%; Xavier=20%]
- **k2-hard** (tier 2) At the end of the story, what discount does Mirela think that Xavier thinks is on the Fenwick quote?
  A. 20% | B. 5% | C. 25% | D. 15% | E. Mirela thinks that Xavier has no idea what discount is on the Fenwick quote
  gold: **C** [real=20%; Mirela=25%; Mirela>Xavier=25%]
- **act2** (tier 2) At the end of the story, a new client is about to ask Xavier what discount is on the Fenwick quote, and Xavier will answer honestly. Before Xavier answers, Mirela writes down what Mirela expects Xavier to say. What does Mirela write?
  A. 20% | B. 15% | C. 25% | D. 5%
  gold: **C** [real=20%; Mirela=25%; Mirela>Xavier=25%]
- **k2-control** (tier 1) At the end of the story, what discount does Goran think that Dalia thinks is on the Fenwick quote?
  A. 20% | B. 5% | C. 15% | D. 25% | E. Goran thinks that Dalia has no idea what discount is on the Fenwick quote
  gold: **D** [real=20%; Goran=20%; Goran>Dalia=25%]
- **k3-hard** (tier 3) At the end of the story, which office does Quinn think that Dalia thinks that Xavier thinks has the Marlow account?
  A. the Lisbon office | B. the Osaka office | C. the Nairobi office | D. the Denver office
  gold: **C** [real=the Lisbon office; Quinn=the Lisbon office; Quinn>Dalia=the Lisbon office; Quinn>Dalia>Xavier=the Nairobi office]
- **k3-control** (tier 1) At the end of the story, what discount does Xavier think that Mirela thinks that Dalia thinks is on the Fenwick quote?
  A. 25% | B. 20% | C. 15% | D. 5%
  gold: **A** [real=20%; Xavier=20%; Xavier>Mirela=25%; Xavier>Mirela>Dalia=25%]
- **k4-hard** (tier 3) At the end of the story, which office does Dalia think that Goran thinks that Xavier thinks that Quinn thinks has the Marlow account?
  A. the Nairobi office | B. the Denver office | C. the Lisbon office | D. the Osaka office
  gold: **A** [real=the Lisbon office; Dalia=the Lisbon office; Dalia>Goran=the Lisbon office; Dalia>Goran>Xavier=the Lisbon office; Dalia>Goran>Xavier>Quinn=the Nairobi office]
- **k4-control** (tier 1) At the end of the story, what discount does Quinn think that Xavier thinks that Dalia thinks that Mirela thinks is on the Fenwick quote?
  A. 5% | B. 15% | C. 25% | D. 20%
  gold: **C** [real=20%; Quinn=25%; Quinn>Xavier=25%; Quinn>Xavier>Dalia=25%; Quinn>Xavier>Dalia>Mirela=25%]
- **inform** (tier None) At the end of the story, Dalia wants everybody else on the team to share Dalia's own view of what discount is on the Fenwick quote. Dalia sends a direct message to every person who, as far as Dalia can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Dalia?
  
  gold: **Quinn**
- **know** (tier None) At the end of the story, what discount does Goran think that Quinn thinks is on the Fenwick quote?
  A. 15% | B. 25% | C. 20% | D. 5% | E. Goran thinks that Quinn has no idea what discount is on the Fenwick quote
  gold: **E** [real=20%; Goran=20%; Goran>Quinn=no idea]

## Scenario S016 (classic, 1 fact(s), 11 events, seed 1016001)

Chidi, Viktor, Keiko, Amara and Uma are in the greenhouse. The greenhouse has four closed containers that nobody can see into: the white cabinet, the wicker basket, the grey locker and the blue drawer.
While everyone watches, Viktor puts a token in the blue drawer.
Keiko and Amara leave the greenhouse. Chidi moves the token to the white cabinet.
Viktor sends Amara a private text message: “The token is in the white cabinet.” Chidi secretly reads this message on Amara's phone. Neither Viktor nor Amara ever knows that Chidi read it.
Viktor sends Keiko a private text message: “The token is in the white cabinet.” Amara secretly reads this message on Keiko's phone. Neither Viktor nor Keiko ever knows that Amara read it.
Viktor leaves the greenhouse. Uma moves the token to the grey locker.
Keiko wants to mislead Amara, so Keiko sends Amara a private text message: “The token is in the wicker basket.”
Keiko wants to mislead Uma, so Keiko sends Uma a private text message: “The token is in the grey locker.” Viktor secretly reads this message on Uma's phone. Neither Keiko nor Uma ever knows that Viktor read it.
Chidi leaves the greenhouse. Uma moves the token to the white cabinet.
Keiko wants to mislead Chidi, so Keiko sends Chidi a private text message: “The token is in the grey locker.”
Chidi comes back into the greenhouse. Uma opens every container in full view of the greenhouse, showing that the token is in the white cabinet. Viktor is outside but watches all of this through the window. Nobody knows that Viktor is watching.
Chidi moves the token to the blue drawer. Uma is in the greenhouse but is absorbed in a phone and does not notice this. Nobody realises that Uma missed it. Keiko is outside but watches all of this through the window. Nobody knows that Keiko is watching.
Chidi leaves the greenhouse. Uma moves the token to the white cabinet.

- **reality** (tier None) At the end of the story, where is the token really?
  A. the white cabinet | B. the wicker basket | C. the blue drawer | D. the grey locker
  gold: **A**
- **k1-hard** (tier 2) At the end of the story, where does Chidi think the token is?
  A. the wicker basket | B. the blue drawer | C. the grey locker | D. the white cabinet
  gold: **B** [real=the white cabinet; Chidi=the blue drawer]
- **act1** (tier 2) At the end of the story, Chidi needs the token and goes to fetch it. Which container does Chidi open first?
  A. the blue drawer | B. the grey locker | C. the wicker basket | D. the white cabinet
  gold: **A** [real=the white cabinet; Chidi=the blue drawer]
- **k1-control** (tier 0) At the end of the story, where does Viktor think the token is?
  A. the white cabinet | B. the wicker basket | C. the blue drawer | D. the grey locker
  gold: **A** [real=the white cabinet; Viktor=the white cabinet]
- **k2-hard** (tier 3) At the end of the story, where does Viktor think that Keiko thinks the token is?
  A. the wicker basket | B. the grey locker | C. the white cabinet | D. the blue drawer
  gold: **B** [real=the white cabinet; Viktor=the white cabinet; Viktor>Keiko=the grey locker]
- **act2** (tier 3) At the end of the story, Keiko is about to fetch the token. Viktor wants to be waiting beside the container that Keiko will open first, and must pick the spot before Keiko moves. Beside which container does Viktor wait?
  A. the blue drawer | B. the grey locker | C. the wicker basket | D. the white cabinet
  gold: **B** [real=the white cabinet; Viktor=the white cabinet; Viktor>Keiko=the grey locker]
- **k2-control** (tier 1) At the end of the story, where does Keiko think that Amara thinks the token is?
  A. the white cabinet | B. the grey locker | C. the wicker basket | D. the blue drawer
  gold: **C** [real=the white cabinet; Keiko=the blue drawer; Keiko>Amara=the wicker basket]
- **k3-hard** (tier 3) At the end of the story, where does Amara think that Viktor thinks that Uma thinks the token is?
  A. the white cabinet | B. the grey locker | C. the blue drawer | D. the wicker basket
  gold: **C** [real=the white cabinet; Amara=the wicker basket; Amara>Viktor=the white cabinet; Amara>Viktor>Uma=the blue drawer]
- **k3-control** (tier 1) At the end of the story, where does Viktor think that Amara thinks that Chidi thinks the token is?
  A. the wicker basket | B. the grey locker | C. the blue drawer | D. the white cabinet
  gold: **C** [real=the white cabinet; Viktor=the white cabinet; Viktor>Amara=the white cabinet; Viktor>Amara>Chidi=the blue drawer]
- **k4-hard** (tier 3) At the end of the story, where does Viktor think that Chidi thinks that Viktor thinks that Amara thinks the token is?
  A. the wicker basket | B. the blue drawer | C. the white cabinet | D. the grey locker
  gold: **B** [real=the white cabinet; Viktor=the white cabinet; Viktor>Chidi=the white cabinet; Viktor>Chidi>Viktor=the white cabinet; Viktor>Chidi>Viktor>Amara=the blue drawer]
- **k4-control** (tier 0) At the end of the story, where does Viktor think that Chidi thinks that Uma thinks that Viktor thinks the token is?
  A. the wicker basket | B. the blue drawer | C. the grey locker | D. the white cabinet
  gold: **D** [real=the white cabinet; Viktor=the white cabinet; Viktor>Chidi=the white cabinet; Viktor>Chidi>Uma=the white cabinet; Viktor>Chidi>Uma>Viktor=the white cabinet]
- **inform** (tier None) At the end of the story, Amara wants everybody else to share Amara's own view of where the token is. Amara sends a private note to every person who, as far as Amara can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Amara?
  
  gold: **Chidi, Uma, Viktor**

## Scenario S017 (workplace, 1 fact(s), 11 events, seed 1017000)

Jonas, Wanjiru, Keiko, Luca and Farah work on the same team. This is what happened, in order.
1. Call with Jonas, Wanjiru, Keiko, Luca and Farah: Keiko sets the product release for Friday.
2. Call with Jonas, Wanjiru, Keiko, Luca and Farah: Jonas moves the product release to Monday.
3. Call with Jonas, Wanjiru, Keiko, Luca and Farah: Farah moves the product release to Friday.
4. Call with Jonas, Keiko, Luca and Farah: Luca moves the product release to Thursday. Wanjiru is not on the call but secretly listens in, and can see who is on it. Nobody knows that Wanjiru is listening.
5. Luca sends Wanjiru a direct message: “The product release is set for Thursday.”
6. Call with Jonas, Keiko, Luca and Farah: Keiko moves the product release to Monday.
7. Call with Jonas, Keiko, Luca and Farah: Keiko moves the product release to Tuesday. Wanjiru is not on the call but secretly listens in, and can see who is on it. Nobody knows that Wanjiru is listening.
8. Keiko sends Wanjiru a direct message: “The product release is set for Tuesday.” Luca secretly reads this message on Wanjiru's screen. Neither Keiko nor Wanjiru ever knows that Luca read it.
9. Farah sends Wanjiru a direct message: “The product release is set for Tuesday.” Jonas secretly reads this message on Wanjiru's screen. Neither Farah nor Wanjiru ever knows that Jonas read it.
10. Call with Jonas, Wanjiru, Keiko and Luca: Jonas moves the product release to Thursday.
11. Wanjiru sends Farah a direct message: “The product release is set for Thursday.”
12. Call with Jonas and Luca: Jonas moves the product release to Friday. Wanjiru is not on the call but secretly listens in, and can see who is on it. Nobody knows that Wanjiru is listening.

- **reality** (tier None) At the end of the story, which day is the product release really set for?
  A. Thursday | B. Tuesday | C. Monday | D. Friday
  gold: **D**
- **k1-hard** (tier 2) At the end of the story, which day does Farah think the product release is set for?
  A. Thursday | B. Monday | C. Friday | D. Tuesday
  gold: **A** [real=Friday; Farah=Thursday]
- **act1** (tier 2) At the end of the story, a new client asks Farah which day the product release is set for. Farah answers honestly. What does Farah say?
  A. Tuesday | B. Friday | C. Thursday | D. Monday
  gold: **C** [real=Friday; Farah=Thursday]
- **k1-control** (tier 0) At the end of the story, which day does Wanjiru think the product release is set for?
  A. Tuesday | B. Thursday | C. Monday | D. Friday
  gold: **D** [real=Friday; Wanjiru=Friday]
- **k2-hard** (tier 3) At the end of the story, which day does Farah think that Keiko thinks the product release is set for?
  A. Thursday | B. Friday | C. Tuesday | D. Monday
  gold: **C** [real=Friday; Farah=Thursday; Farah>Keiko=Tuesday]
- **act2** (tier 3) At the end of the story, a new client is about to ask Keiko which day the product release is set for, and Keiko will answer honestly. Before Keiko answers, Farah writes down what Farah expects Keiko to say. What does Farah write?
  A. Monday | B. Tuesday | C. Friday | D. Thursday
  gold: **B** [real=Friday; Farah=Thursday; Farah>Keiko=Tuesday]
- **k2-control** (tier 0) At the end of the story, which day does Luca think that Jonas thinks the product release is set for?
  A. Monday | B. Tuesday | C. Friday | D. Thursday
  gold: **C** [real=Friday; Luca=Friday; Luca>Jonas=Friday]
- **k3-hard** (tier 3) At the end of the story, which day does Jonas think that Wanjiru thinks that Farah thinks the product release is set for?
  A. Monday | B. Friday | C. Tuesday | D. Thursday
  gold: **C** [real=Friday; Jonas=Friday; Jonas>Wanjiru=Thursday; Jonas>Wanjiru>Farah=Tuesday]
- **k3-control** (tier 0) At the end of the story, which day does Farah think that Wanjiru thinks that Keiko thinks the product release is set for?
  A. Tuesday | B. Thursday | C. Monday | D. Friday
  gold: **D** [real=Friday; Farah=Thursday; Farah>Wanjiru=Thursday; Farah>Wanjiru>Keiko=Friday]
- **k4-hard** (tier 2) At the end of the story, which day does Farah think that Keiko thinks that Farah thinks that Jonas thinks the product release is set for?
  A. Thursday | B. Friday | C. Monday | D. Tuesday
  gold: **D** [real=Friday; Farah=Thursday; Farah>Keiko=Tuesday; Farah>Keiko>Farah=Tuesday; Farah>Keiko>Farah>Jonas=Tuesday]
- **k4-control** (tier 0) At the end of the story, which day does Jonas think that Keiko thinks that Wanjiru thinks that Farah thinks the product release is set for?
  A. Tuesday | B. Monday | C. Friday | D. Thursday
  gold: **C** [real=Friday; Jonas=Friday; Jonas>Keiko=Thursday; Jonas>Keiko>Wanjiru=Thursday; Jonas>Keiko>Wanjiru>Farah=Friday]
- **inform** (tier None) At the end of the story, Farah wants everybody else on the team to share Farah's own view of which day the product release is set for. Farah sends a direct message to every person who, as far as Farah can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Farah?
  
  gold: **Jonas, Keiko, Luca**

## Scenario S018 (classic, 2 fact(s), 11 events, seed 1018000)

Keiko, Bruno, Chidi, Quinn and Emeka are in the workshop. On the floor of the workshop there are four closed containers that nobody can see into: the canvas sack, the grey locker, the leather bag and the green cupboard. On a shelf there are four closed tins that nobody can see into: the copper tin, the flat tin, the tall tin and the round tin. The tins are empty at the start, and the harmonica is only ever kept in the containers on the floor.
While everyone watches, Chidi puts a harmonica in the leather bag.
Quinn leaves the workshop. Keiko moves the harmonica to the grey locker. Quinn is outside but watches all of this through the window. Nobody knows that Quinn is watching.
Bruno leaves the workshop. Chidi moves the harmonica to the canvas sack. Quinn is outside but watches all of this through the window. Nobody knows that Quinn is watching.
Bruno comes back into the workshop. Keiko opens every container on the floor in full view of the workshop, showing that the harmonica is in the canvas sack. Quinn is outside but watches all of this through the window. Nobody knows that Quinn is watching.
Bruno leaves the workshop. Quinn comes back into the workshop. Quinn takes a padlock out of a pocket and puts it in the round tin.
Keiko sends Quinn a private text message: “The harmonica is in the canvas sack.” Bruno secretly reads this message on Quinn's phone. Neither Keiko nor Quinn ever knows that Bruno read it.
Quinn moves the harmonica to the green cupboard. Emeka is in the workshop but is absorbed in a phone and does not notice this. Nobody realises that Emeka missed it.
Chidi sends Bruno a private text message: “The padlock is in the round tin.”
Emeka sends Bruno a private text message: “The padlock is in the round tin.”
Keiko wants to mislead Bruno, so Keiko sends Bruno a private text message: “The harmonica is in the leather bag.”
Bruno sends Emeka a private text message: “The harmonica is in the leather bag.”
Keiko and Emeka leave the workshop. Chidi moves the harmonica to the grey locker. Keiko is outside but watches all of this through the window. Nobody knows that Keiko is watching.

- **reality** (tier None) At the end of the story, where is the padlock really?
  A. the round tin | B. the tall tin | C. the copper tin | D. the flat tin
  gold: **A**
- **k1-hard** (tier 2) At the end of the story, where does Bruno think the harmonica is?
  A. the green cupboard | B. the canvas sack | C. the leather bag | D. the grey locker
  gold: **C** [real=the grey locker; Bruno=the leather bag]
- **act1** (tier 2) At the end of the story, Bruno needs the harmonica and goes to fetch it. Which container does Bruno open first?
  A. the grey locker | B. the green cupboard | C. the leather bag | D. the canvas sack
  gold: **C** [real=the grey locker; Bruno=the leather bag]
- **k1-control** (tier 0) At the end of the story, where does Keiko think the padlock is?
  A. the tall tin | B. the round tin | C. the flat tin | D. the copper tin | E. Keiko has no idea where the padlock is
  gold: **B** [real=the round tin; Keiko=the round tin]
- **k2-hard** (tier 3) At the end of the story, where does Quinn think that Emeka thinks the harmonica is?
  A. the grey locker | B. the leather bag | C. the canvas sack | D. the green cupboard
  gold: **D** [real=the grey locker; Quinn=the grey locker; Quinn>Emeka=the green cupboard]
- **act2** (tier 3) At the end of the story, Emeka is about to fetch the harmonica. Quinn wants to be waiting beside the container that Emeka will open first, and must pick the spot before Emeka moves. Beside which container does Quinn wait?
  A. the grey locker | B. the canvas sack | C. the green cupboard | D. the leather bag
  gold: **C** [real=the grey locker; Quinn=the grey locker; Quinn>Emeka=the green cupboard]
- **k2-control** (tier 1) At the end of the story, where does Emeka think that Bruno thinks the harmonica is?
  A. the grey locker | B. the green cupboard | C. the leather bag | D. the canvas sack
  gold: **C** [real=the grey locker; Emeka=the leather bag; Emeka>Bruno=the leather bag]
- **k3-hard** (tier 3) At the end of the story, where does Bruno think that Keiko thinks that Chidi thinks the harmonica is?
  A. the leather bag | B. the green cupboard | C. the canvas sack | D. the grey locker
  gold: **C** [real=the grey locker; Bruno=the leather bag; Bruno>Keiko=the leather bag; Bruno>Keiko>Chidi=the canvas sack]
- **k3-control** (tier 0) At the end of the story, where does Keiko think that Emeka thinks that Chidi thinks the padlock is?
  A. the round tin | B. the copper tin | C. the flat tin | D. the tall tin
  gold: **A** [real=the round tin; Keiko=the round tin; Keiko>Emeka=the round tin; Keiko>Emeka>Chidi=the round tin]
- **k4-hard** (tier 3) At the end of the story, where does Bruno think that Keiko thinks that Chidi thinks that Quinn thinks the harmonica is?
  A. the green cupboard | B. the leather bag | C. the grey locker | D. the canvas sack
  gold: **B** [real=the grey locker; Bruno=the leather bag; Bruno>Keiko=the leather bag; Bruno>Keiko>Chidi=the canvas sack; Bruno>Keiko>Chidi>Quinn=the leather bag]
- **k4-control** (tier 1) At the end of the story, where does Quinn think that Chidi thinks that Quinn thinks that Bruno thinks the harmonica is?
  A. the canvas sack | B. the green cupboard | C. the leather bag | D. the grey locker
  gold: **C** [real=the grey locker; Quinn=the grey locker; Quinn>Chidi=the grey locker; Quinn>Chidi>Quinn=the grey locker; Quinn>Chidi>Quinn>Bruno=the leather bag]
- **inform** (tier None) At the end of the story, Bruno wants everybody else to share Bruno's own view of where the padlock is. Bruno sends a private note to every person who, as far as Bruno can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Bruno?
  
  gold: **Keiko, Quinn**
- **know** (tier None) At the end of the story, where does Quinn think that Bruno thinks the padlock is?
  A. the flat tin | B. the copper tin | C. the tall tin | D. the round tin | E. Quinn thinks that Bruno has no idea where the padlock is
  gold: **E** [real=the round tin; Quinn=the round tin; Quinn>Bruno=no idea]

## Scenario S019 (workplace, 2 fact(s), 11 events, seed 1019000)

Hana, Zoltan, Pablo, Mirela and Quinn work on the same team. This is what happened, in order.
1. Call with Hana, Zoltan, Pablo, Mirela and Quinn: Mirela fixes Turin as the place for the team offsite.
2. Call with Hana, Zoltan, Pablo, Mirela and Quinn: Pablo moves the team offsite to Ghent.
3. Call with Hana, Zoltan, Pablo, Mirela and Quinn: Pablo moves the team offsite to Leeds.
4. Call with Hana, Zoltan, Pablo, Mirela and Quinn: Pablo moves the team offsite to Turin.
5. Call with Zoltan and Pablo: Zoltan sets the product release for Thursday.
6. Call with Hana and Pablo: Hana moves the team offsite to Ghent.
7. Pablo sends Zoltan a direct message: “The team offsite is in Ghent.”
8. Call with Hana and Pablo: Pablo moves the product release to Friday.
9. Pablo sends Mirela a direct message: “The team offsite is in Ghent.”
10. Call with Hana, Pablo and Quinn: Pablo opens the travel plan and reads it out: “The team offsite is in Ghent.”
11. Pablo wants to mislead Quinn, so Pablo sends Quinn a direct message: “The product release is set for Tuesday.” Zoltan secretly reads this message on Quinn's screen. Neither Pablo nor Quinn ever knows that Zoltan read it.
12. Mirela sends Zoltan a direct message: “The team offsite is in Ghent.”

- **reality** (tier None) At the end of the story, which city is the team offsite really in?
  A. Ghent | B. Porto | C. Leeds | D. Turin
  gold: **A**
- **k1-hard** (tier 2) At the end of the story, which day does Zoltan think the product release is set for?
  A. Friday | B. Tuesday | C. Thursday | D. Wednesday | E. Zoltan has no idea which day the product release is set for
  gold: **B** [real=Friday; Zoltan=Tuesday]
- **act1** (tier 2) At the end of the story, a new client asks Zoltan which day the product release is set for. Zoltan answers honestly. What does Zoltan say?
  A. Wednesday | B. Tuesday | C. Friday | D. Thursday
  gold: **B** [real=Friday; Zoltan=Tuesday]
- **k1-control** (tier 0) At the end of the story, which day does Hana think the product release is set for?
  A. Wednesday | B. Tuesday | C. Thursday | D. Friday | E. Hana has no idea which day the product release is set for
  gold: **D** [real=Friday; Hana=Friday]
- **k2-hard** (tier 3) At the end of the story, which city does Zoltan think that Hana thinks the team offsite is in?
  A. Porto | B. Turin | C. Leeds | D. Ghent
  gold: **B** [real=Ghent; Zoltan=Ghent; Zoltan>Hana=Turin]
- **act2** (tier 3) At the end of the story, a new client is about to ask Hana which city the team offsite is in, and Hana will answer honestly. Before Hana answers, Zoltan writes down what Zoltan expects Hana to say. What does Zoltan write?
  A. Leeds | B. Ghent | C. Porto | D. Turin
  gold: **D** [real=Ghent; Zoltan=Ghent; Zoltan>Hana=Turin]
- **k2-control** (tier 0) At the end of the story, which city does Zoltan think that Mirela thinks the team offsite is in?
  A. Porto | B. Ghent | C. Turin | D. Leeds
  gold: **B** [real=Ghent; Zoltan=Ghent; Zoltan>Mirela=Ghent]
- **k3-hard** (tier 3) At the end of the story, which city does Zoltan think that Pablo thinks that Mirela thinks the team offsite is in?
  A. Leeds | B. Turin | C. Porto | D. Ghent
  gold: **B** [real=Ghent; Zoltan=Ghent; Zoltan>Pablo=Ghent; Zoltan>Pablo>Mirela=Turin]
- **k3-control** (tier 0) At the end of the story, which city does Pablo think that Quinn thinks that Hana thinks the team offsite is in?
  A. Turin | B. Ghent | C. Porto | D. Leeds
  gold: **B** [real=Ghent; Pablo=Ghent; Pablo>Quinn=Ghent; Pablo>Quinn>Hana=Ghent]
- **k4-hard** (tier 2) At the end of the story, which city does Quinn think that Zoltan thinks that Mirela thinks that Zoltan thinks the team offsite is in?
  A. Leeds | B. Porto | C. Ghent | D. Turin
  gold: **D** [real=Ghent; Quinn=Ghent; Quinn>Zoltan=Turin; Quinn>Zoltan>Mirela=Turin; Quinn>Zoltan>Mirela>Zoltan=Turin]
- **k4-control** (tier 0) At the end of the story, which day does Hana think that Pablo thinks that Hana thinks that Pablo thinks the product release is set for?
  A. Tuesday | B. Friday | C. Wednesday | D. Thursday
  gold: **B** [real=Friday; Hana=Friday; Hana>Pablo=Friday; Hana>Pablo>Hana=Friday; Hana>Pablo>Hana>Pablo=Friday]
- **inform** (tier None) At the end of the story, Quinn wants everybody else on the team to share Quinn's own view of which day the product release is set for. Quinn sends a direct message to every person who, as far as Quinn can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Quinn?
  
  gold: **Hana, Mirela, Zoltan**
- **know** (tier None) At the end of the story, which day does Mirela think the product release is set for?
  A. Tuesday | B. Wednesday | C. Thursday | D. Friday | E. Mirela has no idea which day the product release is set for
  gold: **E** [real=Friday; Mirela=no idea]

## Scenario S020 (classic, 1 fact(s), 14 events, seed 1020001)

Zoltan, Xavier, Luca, Bruno and Chidi are in the kitchen. The kitchen has four closed containers that nobody can see into: the red box, the grey locker, the wicker basket and the leather bag.
While everyone watches, Xavier puts a harmonica in the leather bag.
Bruno moves the harmonica to the wicker basket.
Xavier leaves the kitchen. Zoltan moves the harmonica to the red box.
Zoltan and Luca leave the kitchen. Bruno moves the harmonica to the leather bag.
Luca sends Xavier a private text message: “The harmonica is in the red box.” Zoltan secretly reads this message on Xavier's phone. Neither Luca nor Xavier ever knows that Zoltan read it.
Bruno leaves the kitchen. Chidi moves the harmonica to the wicker basket.
Xavier wants to mislead Bruno, so Xavier sends Bruno a private text message: “The harmonica is in the grey locker.”
Luca comes back into the kitchen. Chidi opens every container in full view of the kitchen, showing that the harmonica is in the wicker basket.
Bruno comes back into the kitchen. Bruno moves the harmonica to the leather bag. Luca is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Luca missed it.
Luca opens every container in full view of the kitchen, showing that the harmonica is in the leather bag.
Xavier sends Zoltan a private text message: “The harmonica is in the red box.”
Bruno and Chidi leave the kitchen. Luca moves the harmonica to the grey locker.
Chidi sends Zoltan a private text message: “The harmonica is in the leather bag.”
Zoltan sends Bruno a private text message: “The harmonica is in the leather bag.”
Luca moves the harmonica to the leather bag.

- **reality** (tier None) At the end of the story, where is the harmonica really?
  A. the leather bag | B. the red box | C. the wicker basket | D. the grey locker
  gold: **A**
- **k1-hard** (tier 2) At the end of the story, where does Xavier think the harmonica is?
  A. the leather bag | B. the red box | C. the grey locker | D. the wicker basket
  gold: **B** [real=the leather bag; Xavier=the red box]
- **act1** (tier 2) At the end of the story, Xavier needs the harmonica and goes to fetch it. Which container does Xavier open first?
  A. the grey locker | B. the leather bag | C. the red box | D. the wicker basket
  gold: **C** [real=the leather bag; Xavier=the red box]
- **k1-control** (tier 0) At the end of the story, where does Chidi think the harmonica is?
  A. the wicker basket | B. the red box | C. the grey locker | D. the leather bag
  gold: **D** [real=the leather bag; Chidi=the leather bag]
- **k2-hard** (tier 3) At the end of the story, where does Zoltan think that Luca thinks the harmonica is?
  A. the grey locker | B. the leather bag | C. the wicker basket | D. the red box
  gold: **D** [real=the leather bag; Zoltan=the leather bag; Zoltan>Luca=the red box]
- **act2** (tier 3) At the end of the story, Luca is about to fetch the harmonica. Zoltan wants to be waiting beside the container that Luca will open first, and must pick the spot before Luca moves. Beside which container does Zoltan wait?
  A. the wicker basket | B. the leather bag | C. the grey locker | D. the red box
  gold: **D** [real=the leather bag; Zoltan=the leather bag; Zoltan>Luca=the red box]
- **k2-control** (tier 0) At the end of the story, where does Zoltan think that Bruno thinks the harmonica is?
  A. the leather bag | B. the wicker basket | C. the grey locker | D. the red box
  gold: **A** [real=the leather bag; Zoltan=the leather bag; Zoltan>Bruno=the leather bag]
- **k3-hard** (tier 3) At the end of the story, where does Xavier think that Luca thinks that Zoltan thinks the harmonica is?
  A. the grey locker | B. the wicker basket | C. the leather bag | D. the red box
  gold: **B** [real=the leather bag; Xavier=the red box; Xavier>Luca=the red box; Xavier>Luca>Zoltan=the wicker basket]
- **k3-control** (tier 1) At the end of the story, where does Xavier think that Zoltan thinks that Xavier thinks the harmonica is?
  A. the wicker basket | B. the leather bag | C. the red box | D. the grey locker
  gold: **C** [real=the leather bag; Xavier=the red box; Xavier>Zoltan=the red box; Xavier>Zoltan>Xavier=the red box]
- **k4-hard** (tier 3) At the end of the story, where does Xavier think that Zoltan thinks that Xavier thinks that Luca thinks the harmonica is?
  A. the leather bag | B. the red box | C. the wicker basket | D. the grey locker
  gold: **C** [real=the leather bag; Xavier=the red box; Xavier>Zoltan=the red box; Xavier>Zoltan>Xavier=the red box; Xavier>Zoltan>Xavier>Luca=the wicker basket]
- **k4-control** (tier 0) At the end of the story, where does Luca think that Bruno thinks that Luca thinks that Chidi thinks the harmonica is?
  A. the grey locker | B. the wicker basket | C. the leather bag | D. the red box
  gold: **C** [real=the leather bag; Luca=the leather bag; Luca>Bruno=the leather bag; Luca>Bruno>Luca=the leather bag; Luca>Bruno>Luca>Chidi=the leather bag]
- **inform** (tier None) At the end of the story, Zoltan wants everybody else to share Zoltan's own view of where the harmonica is. Zoltan sends a private note to every person who, as far as Zoltan can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Zoltan?
  
  gold: **Luca, Xavier**

## Scenario S021 (workplace, 1 fact(s), 14 events, seed 1021000)

Wanjiru, Soren, Tariq, Viktor and Emeka work on the same team. This is what happened, in order.
1. Call with Wanjiru, Soren, Tariq, Viktor and Emeka: Wanjiru assigns the Marlow account to the Denver office.
2. Call with Wanjiru, Soren, Tariq, Viktor and Emeka: Tariq reassigns the Marlow account to the Lisbon office.
3. Call with Wanjiru, Tariq and Viktor: Wanjiru reassigns the Marlow account to the Nairobi office. Tariq is on the call but has stepped away from the desk and misses this. Nobody realises that Tariq missed it.
4. Call with Wanjiru, Tariq and Viktor: Tariq reassigns the Marlow account to the Lisbon office.
5. Call with Tariq and Viktor: Tariq reassigns the Marlow account to the Osaka office.
6. Tariq wants to mislead Emeka, so Tariq sends Emeka a direct message: “The Marlow account is with the Denver office.”
7. Viktor sends Soren a direct message: “The Marlow account is with the Osaka office.”
8. Emeka sends Wanjiru a direct message: “The Marlow account is with the Denver office.”
9. Soren sends Wanjiru a direct message: “The Marlow account is with the Osaka office.” Emeka secretly reads this message on Wanjiru's screen. Neither Soren nor Wanjiru ever knows that Emeka read it.
10. Emeka sends Viktor a direct message: “The Marlow account is with the Osaka office.”
11. Tariq sends Soren a direct message: “The Marlow account is with the Osaka office.”
12. Call with Tariq and Viktor: Viktor reassigns the Marlow account to the Denver office. Soren is not on the call but secretly listens in, and can see who is on it. Nobody knows that Soren is listening.
13. Viktor sends Wanjiru a direct message: “The Marlow account is with the Denver office.” Tariq secretly reads this message on Wanjiru's screen. Neither Viktor nor Wanjiru ever knows that Tariq read it.
14. Viktor, working alone, reassigns the Marlow account to the Osaka office and tells nobody. Emeka secretly watches Viktor's screen as this happens. Nobody knows that Emeka is watching.
15. Viktor, working alone, reassigns the Marlow account to the Denver office and tells nobody.

- **reality** (tier None) At the end of the story, which office really has the Marlow account?
  A. the Lisbon office | B. the Osaka office | C. the Denver office | D. the Nairobi office
  gold: **C**
- **k1-hard** (tier 2) At the end of the story, which office does Emeka think has the Marlow account?
  A. the Lisbon office | B. the Nairobi office | C. the Denver office | D. the Osaka office
  gold: **D** [real=the Denver office; Emeka=the Osaka office]
- **act1** (tier 2) At the end of the story, a new client asks Emeka which office has the Marlow account. Emeka answers honestly. What does Emeka say?
  A. the Nairobi office | B. the Lisbon office | C. the Denver office | D. the Osaka office
  gold: **D** [real=the Denver office; Emeka=the Osaka office]
- **k1-control** (tier 0) At the end of the story, which office does Wanjiru think has the Marlow account?
  A. the Osaka office | B. the Lisbon office | C. the Denver office | D. the Nairobi office
  gold: **C** [real=the Denver office; Wanjiru=the Denver office]
- **k2-hard** (tier 3) At the end of the story, which office does Soren think that Wanjiru thinks has the Marlow account?
  A. the Denver office | B. the Nairobi office | C. the Lisbon office | D. the Osaka office
  gold: **D** [real=the Denver office; Soren=the Denver office; Soren>Wanjiru=the Osaka office]
- **act2** (tier 3) At the end of the story, a new client is about to ask Wanjiru which office has the Marlow account, and Wanjiru will answer honestly. Before Wanjiru answers, Soren writes down what Soren expects Wanjiru to say. What does Soren write?
  A. the Osaka office | B. the Denver office | C. the Nairobi office | D. the Lisbon office
  gold: **A** [real=the Denver office; Soren=the Denver office; Soren>Wanjiru=the Osaka office]
- **k2-control** (tier 0) At the end of the story, which office does Soren think that Viktor thinks has the Marlow account?
  A. the Nairobi office | B. the Denver office | C. the Lisbon office | D. the Osaka office
  gold: **B** [real=the Denver office; Soren=the Denver office; Soren>Viktor=the Denver office]
- **k3-hard** (tier 3) At the end of the story, which office does Soren think that Viktor thinks that Wanjiru thinks has the Marlow account?
  A. the Nairobi office | B. the Lisbon office | C. the Osaka office | D. the Denver office
  gold: **B** [real=the Denver office; Soren=the Denver office; Soren>Viktor=the Denver office; Soren>Viktor>Wanjiru=the Lisbon office]
- **k3-control** (tier 0) At the end of the story, which office does Emeka think that Tariq thinks that Emeka thinks has the Marlow account?
  A. the Lisbon office | B. the Osaka office | C. the Nairobi office | D. the Denver office
  gold: **D** [real=the Denver office; Emeka=the Osaka office; Emeka>Tariq=the Denver office; Emeka>Tariq>Emeka=the Denver office]
- **k4-hard** (tier 3) At the end of the story, which office does Wanjiru think that Emeka thinks that Wanjiru thinks that Soren thinks has the Marlow account?
  A. the Nairobi office | B. the Osaka office | C. the Lisbon office | D. the Denver office
  gold: **C** [real=the Denver office; Wanjiru=the Denver office; Wanjiru>Emeka=the Denver office; Wanjiru>Emeka>Wanjiru=the Denver office; Wanjiru>Emeka>Wanjiru>Soren=the Lisbon office]
- **k4-control** (tier 1) At the end of the story, which office does Viktor think that Emeka thinks that Viktor thinks that Emeka thinks has the Marlow account?
  A. the Lisbon office | B. the Nairobi office | C. the Denver office | D. the Osaka office
  gold: **D** [real=the Denver office; Viktor=the Denver office; Viktor>Emeka=the Osaka office; Viktor>Emeka>Viktor=the Osaka office; Viktor>Emeka>Viktor>Emeka=the Osaka office]
- **inform** (tier None) At the end of the story, Emeka wants everybody else on the team to share Emeka's own view of which office has the Marlow account. Emeka sends a direct message to every person who, as far as Emeka can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Emeka?
  
  gold: **Tariq**

## Scenario S022 (classic, 2 fact(s), 14 events, seed 1022000)

Emeka, Goran, Ines, Rania and Amara are in the workshop. On the floor of the workshop there are four closed containers that nobody can see into: the black trunk, the white cabinet, the leather bag and the blue drawer. On a shelf there are four closed tins that nobody can see into: the copper tin, the round tin, the tall tin and the striped tin. The tins are empty at the start, and the stopwatch is only ever kept in the containers on the floor.
While everyone watches, Rania puts a stopwatch in the white cabinet.
Rania moves the stopwatch to the leather bag.
Amara leaves the workshop. Emeka moves the stopwatch to the blue drawer.
Emeka leaves the workshop. Amara comes back into the workshop. Goran moves the stopwatch to the black trunk. Emeka is outside but watches all of this through the window. Nobody knows that Emeka is watching.
Ines takes a brooch out of a pocket and puts it in the round tin.
Rania wants to mislead Emeka, so Rania sends Emeka a private text message: “The brooch is in the copper tin.”
Goran and Amara leave the workshop. Ines moves the stopwatch to the blue drawer.
Rania leaves the workshop. Amara comes back into the workshop. Ines moves the stopwatch to the white cabinet.
Ines moves the brooch to the tall tin.
Ines sends Emeka a private text message: “The stopwatch is in the white cabinet.” Rania secretly reads this message on Emeka's phone. Neither Ines nor Emeka ever knows that Rania read it.
Amara sends Rania a private text message: “The stopwatch is in the white cabinet.”
Ines moves the brooch to the copper tin.
Amara leaves the workshop. Emeka comes back into the workshop. Emeka moves the brooch to the tall tin.
Emeka sends Amara a private text message: “The stopwatch is in the white cabinet.”
Emeka sends Goran a private text message: “The stopwatch is in the white cabinet.” Ines secretly reads this message on Goran's phone. Neither Emeka nor Goran ever knows that Ines read it.

- **reality** (tier None) At the end of the story, where is the brooch really?
  A. the round tin | B. the tall tin | C. the copper tin | D. the striped tin
  gold: **B**
- **k1-hard** (tier 2) At the end of the story, where does Rania think the brooch is?
  A. the copper tin | B. the round tin | C. the striped tin | D. the tall tin | E. Rania has no idea where the brooch is
  gold: **B** [real=the tall tin; Rania=the round tin]
- **act1** (tier 2) At the end of the story, Rania needs the brooch and goes to fetch it. Which container does Rania open first?
  A. the round tin | B. the striped tin | C. the tall tin | D. the copper tin
  gold: **A** [real=the tall tin; Rania=the round tin]
- **k1-control** (tier 0) At the end of the story, where does Ines think the stopwatch is?
  A. the blue drawer | B. the leather bag | C. the white cabinet | D. the black trunk
  gold: **C** [real=the white cabinet; Ines=the white cabinet]
- **k2-hard** (tier 3) At the end of the story, where does Emeka think that Rania thinks the stopwatch is?
  A. the blue drawer | B. the white cabinet | C. the black trunk | D. the leather bag
  gold: **C** [real=the white cabinet; Emeka=the white cabinet; Emeka>Rania=the black trunk]
- **act2** (tier 3) At the end of the story, Rania is about to fetch the stopwatch. Emeka wants to be waiting beside the container that Rania will open first, and must pick the spot before Rania moves. Beside which container does Emeka wait?
  A. the leather bag | B. the white cabinet | C. the black trunk | D. the blue drawer
  gold: **C** [real=the white cabinet; Emeka=the white cabinet; Emeka>Rania=the black trunk]
- **k2-control** (tier 1) At the end of the story, where does Rania think that Goran thinks the brooch is?
  A. the tall tin | B. the copper tin | C. the round tin | D. the striped tin | E. Rania thinks that Goran has no idea where the brooch is
  gold: **C** [real=the tall tin; Rania=the round tin; Rania>Goran=the round tin]
- **k3-hard** (tier 3) At the end of the story, where does Ines think that Amara thinks that Emeka thinks the stopwatch is?
  A. the white cabinet | B. the leather bag | C. the black trunk | D. the blue drawer
  gold: **B** [real=the white cabinet; Ines=the white cabinet; Ines>Amara=the white cabinet; Ines>Amara>Emeka=the leather bag]
- **k3-control** (tier 0) At the end of the story, where does Goran think that Emeka thinks that Goran thinks the stopwatch is?
  A. the blue drawer | B. the leather bag | C. the white cabinet | D. the black trunk
  gold: **C** [real=the white cabinet; Goran=the white cabinet; Goran>Emeka=the white cabinet; Goran>Emeka>Goran=the white cabinet]
- **k4-hard** (tier 3) At the end of the story, where does Amara think that Emeka thinks that Amara thinks that Goran thinks the stopwatch is?
  A. the black trunk | B. the white cabinet | C. the leather bag | D. the blue drawer
  gold: **C** [real=the white cabinet; Amara=the white cabinet; Amara>Emeka=the white cabinet; Amara>Emeka>Amara=the white cabinet; Amara>Emeka>Amara>Goran=the leather bag]
- **k4-control** (tier 1) At the end of the story, where does Rania think that Goran thinks that Rania thinks that Goran thinks the brooch is?
  A. the tall tin | B. the copper tin | C. the round tin | D. the striped tin
  gold: **C** [real=the tall tin; Rania=the round tin; Rania>Goran=the round tin; Rania>Goran>Rania=the round tin; Rania>Goran>Rania>Goran=the round tin]
- **inform** (tier None) At the end of the story, Emeka wants everybody else to share Emeka's own view of where the stopwatch is. Emeka sends a private note to every person who, as far as Emeka can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Emeka?
  
  gold: **Rania**
- **know** (tier None) At the end of the story, where does Emeka think that Goran thinks the brooch is?
  A. the striped tin | B. the round tin | C. the copper tin | D. the tall tin | E. Emeka thinks that Goran has no idea where the brooch is
  gold: **E** [real=the tall tin; Emeka=the tall tin; Emeka>Goran=no idea]

## Scenario S023 (workplace, 2 fact(s), 14 events, seed 1023000)

Quinn, Wanjiru, Farah, Luca and Tariq work on the same team. This is what happened, in order.
1. Call with Quinn, Wanjiru, Farah, Luca and Tariq: Wanjiru sets the discount on the Fenwick quote at 25%.
2. Call with Quinn, Wanjiru, Farah, Luca and Tariq: Quinn changes the discount on the Fenwick quote to 15%.
3. Call with Quinn and Tariq: Tariq books the client workshop into Room Cedar. Wanjiru is not on the call but secretly listens in, and can see who is on it. Nobody knows that Wanjiru is listening.
4. Call with Quinn, Luca and Tariq: Quinn opens the booking system and reads it out: “The client workshop is booked in Room Cedar.”
5. Luca wants to mislead Farah, so Luca sends Farah a direct message: “The client workshop is booked in Room Elm.”
6. Call with Quinn, Wanjiru and Luca: Wanjiru says: “The client workshop is booked in Room Cedar.”
7. Call with Quinn, Wanjiru and Luca: Wanjiru changes the discount on the Fenwick quote to 25%. Quinn is on the call but has stepped away from the desk and misses this. Nobody realises that Quinn missed it. Tariq is not on the call but secretly listens in, and can see who is on it. Nobody knows that Tariq is listening.
8. Tariq sends Farah a direct message: “The client workshop is booked in Room Cedar.”
9. Call with Quinn, Wanjiru and Luca: Wanjiru changes the discount on the Fenwick quote to 10%.
10. Farah sends Luca a direct message: “The client workshop is booked in Room Cedar.”
11. Call with Quinn, Wanjiru and Luca: Luca moves the client workshop to Room Elm.
12. Call with Quinn, Wanjiru and Luca: Luca moves the client workshop to Room Alder. Tariq is not on the call but secretly listens in, and can see who is on it. Nobody knows that Tariq is listening.
13. Wanjiru sends Farah a direct message: “The discount on the Fenwick quote is 10%.”
14. Quinn sends Tariq a direct message: “The client workshop is booked in Room Alder.”
15. Wanjiru wants to mislead Farah, so Wanjiru sends Farah a direct message: “The client workshop is booked in Room Dogwood.”

- **reality** (tier None) At the end of the story, what discount is really on the Fenwick quote?
  A. 10% | B. 20% | C. 15% | D. 25%
  gold: **A**
- **k1-hard** (tier 2) At the end of the story, what discount does Tariq think is on the Fenwick quote?
  A. 20% | B. 10% | C. 15% | D. 25%
  gold: **D** [real=10%; Tariq=25%]
- **act1** (tier 2) At the end of the story, a new client asks Tariq what discount is on the Fenwick quote. Tariq answers honestly. What does Tariq say?
  A. 15% | B. 25% | C. 20% | D. 10%
  gold: **B** [real=10%; Tariq=25%]
- **k1-control** (tier 0) At the end of the story, which room does Quinn think the client workshop is booked in?
  A. Room Alder | B. Room Cedar | C. Room Elm | D. Room Dogwood | E. Quinn has no idea which room the client workshop is booked in
  gold: **A** [real=Room Alder; Quinn=Room Alder]
- **k2-hard** (tier 3) At the end of the story, what discount does Farah think that Luca thinks is on the Fenwick quote?
  A. 15% | B. 20% | C. 10% | D. 25%
  gold: **A** [real=10%; Farah=10%; Farah>Luca=15%]
- **act2** (tier 3) At the end of the story, a new client is about to ask Luca what discount is on the Fenwick quote, and Luca will answer honestly. Before Luca answers, Farah writes down what Farah expects Luca to say. What does Farah write?
  A. 25% | B. 20% | C. 10% | D. 15%
  gold: **D** [real=10%; Farah=10%; Farah>Luca=15%]
- **k2-control** (tier 1) At the end of the story, which room does Wanjiru think that Farah thinks the client workshop is booked in?
  A. Room Dogwood | B. Room Elm | C. Room Alder | D. Room Cedar | E. Wanjiru thinks that Farah has no idea which room the client workshop is booked in
  gold: **A** [real=Room Alder; Wanjiru=Room Alder; Wanjiru>Farah=Room Dogwood]
- **k3-hard** (tier 3) At the end of the story, which room does Wanjiru think that Quinn thinks that Tariq thinks the client workshop is booked in?
  A. Room Cedar | B. Room Elm | C. Room Alder | D. Room Dogwood
  gold: **A** [real=Room Alder; Wanjiru=Room Alder; Wanjiru>Quinn=Room Alder; Wanjiru>Quinn>Tariq=Room Cedar]
- **k3-control** (tier 1) At the end of the story, which room does Farah think that Wanjiru thinks that Farah thinks the client workshop is booked in?
  A. Room Cedar | B. Room Dogwood | C. Room Elm | D. Room Alder
  gold: **B** [real=Room Alder; Farah=Room Dogwood; Farah>Wanjiru=Room Dogwood; Farah>Wanjiru>Farah=Room Dogwood]
- **k4-hard** (tier 3) At the end of the story, which room does Quinn think that Tariq thinks that Quinn thinks that Luca thinks the client workshop is booked in?
  A. Room Cedar | B. Room Alder | C. Room Elm | D. Room Dogwood
  gold: **A** [real=Room Alder; Quinn=Room Alder; Quinn>Tariq=Room Alder; Quinn>Tariq>Quinn=Room Alder; Quinn>Tariq>Quinn>Luca=Room Cedar]
- **k4-control** (tier 1) At the end of the story, which room does Wanjiru think that Farah thinks that Wanjiru thinks that Farah thinks the client workshop is booked in?
  A. Room Alder | B. Room Elm | C. Room Cedar | D. Room Dogwood
  gold: **D** [real=Room Alder; Wanjiru=Room Alder; Wanjiru>Farah=Room Dogwood; Wanjiru>Farah>Wanjiru=Room Dogwood; Wanjiru>Farah>Wanjiru>Farah=Room Dogwood]
- **inform** (tier None) At the end of the story, Luca wants everybody else on the team to share Luca's own view of which room the client workshop is booked in. Luca sends a direct message to every person who, as far as Luca can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Luca?
  
  gold: **Farah, Tariq**
- **know** (tier None) At the end of the story, which room does Quinn think that Farah thinks the client workshop is booked in?
  A. Room Elm | B. Room Alder | C. Room Dogwood | D. Room Cedar | E. Quinn thinks that Farah has no idea which room the client workshop is booked in
  gold: **E** [real=Room Alder; Quinn=Room Alder; Quinn>Farah=no idea]

## Scenario H000 (classic, 1 fact(s), 40 events, seed 1300000)

Ines, Goran, Soren, Amara, Luca, Hana, Uma and Bruno are in the kitchen. The kitchen has four closed containers that nobody can see into: the blue drawer, the canvas sack, the green cupboard and the red box.
While everyone watches, Soren puts a harmonica in the red box.
Amara leaves the kitchen. Uma moves the harmonica to the blue drawer. Ines is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Ines missed it.
Soren opens every container in full view of the kitchen, showing that the harmonica is in the blue drawer.
Soren opens every container in full view of the kitchen, showing that the harmonica is in the blue drawer. Amara is outside but watches all of this through the window. Nobody knows that Amara is watching.
Ines moves the harmonica to the red box.
Bruno leaves the kitchen. Uma moves the harmonica to the green cupboard. Ines is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Ines missed it.
Uma sends Bruno a private text message: “The harmonica is in the green cupboard.”
Soren leaves the kitchen. Ines moves the harmonica to the canvas sack.
Goran sends Amara a private text message: “The harmonica is in the canvas sack.” Luca secretly reads this message on Amara's phone. Neither Goran nor Amara ever knows that Luca read it.
Amara comes back into the kitchen. Luca moves the harmonica to the green cupboard. Goran is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Goran missed it.
Amara sends Soren a private text message: “The harmonica is in the green cupboard.”
Goran moves the harmonica to the red box. Soren is outside but watches all of this through the window. Nobody knows that Soren is watching.
Hana moves the harmonica to the canvas sack.
Uma moves the harmonica to the blue drawer. Bruno is outside but watches all of this through the window. Nobody knows that Bruno is watching.
Ines sends Bruno a private text message: “The harmonica is in the blue drawer.”
Hana sends Soren a private text message: “The harmonica is in the blue drawer.”
Uma moves the harmonica to the canvas sack.
Uma moves the harmonica to the blue drawer. Ines is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Ines missed it.
Bruno sends Soren a private text message: “The harmonica is in the blue drawer.”
Hana leaves the kitchen. Luca opens every container in full view of the kitchen, showing that the harmonica is in the blue drawer. Amara is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Amara missed it.
Amara leaves the kitchen. Hana comes back into the kitchen. Luca moves the harmonica to the green cupboard.
Uma leaves the kitchen. Luca moves the harmonica to the red box.
Luca opens every container in full view of the kitchen, showing that the harmonica is in the red box. Amara is outside but watches all of this through the window. Nobody knows that Amara is watching.
Bruno comes back into the kitchen. Ines moves the harmonica to the canvas sack. Bruno is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Bruno missed it.
Uma wants to mislead Amara, so Uma sends Amara a private text message: “The harmonica is in the canvas sack.”
Hana opens every container in full view of the kitchen, showing that the harmonica is in the canvas sack.
Ines sends Uma a private text message: “The harmonica is in the canvas sack.”
Bruno leaves the kitchen. Ines moves the harmonica to the green cupboard.
Amara comes back into the kitchen. Luca moves the harmonica to the blue drawer. Uma is outside but watches all of this through the window. Nobody knows that Uma is watching.
Luca leaves the kitchen. Uma comes back into the kitchen. Uma moves the harmonica to the green cupboard.
Amara leaves the kitchen. Ines moves the harmonica to the red box. Soren is outside but watches all of this through the window. Nobody knows that Soren is watching.
Goran moves the harmonica to the green cupboard.
Uma sends Luca a private text message: “The harmonica is in the green cupboard.” Bruno secretly reads this message on Luca's phone. Neither Uma nor Luca ever knows that Bruno read it.
Soren wants to mislead Bruno, so Soren sends Bruno a private text message: “The harmonica is in the green cupboard.”
Ines moves the harmonica to the canvas sack.
Soren and Bruno come back into the kitchen. Soren moves the harmonica to the blue drawer.
Bruno sends Luca a private text message: “The harmonica is in the blue drawer.”
Hana leaves the kitchen. Uma moves the harmonica to the green cupboard. Amara is outside but watches all of this through the window. Nobody knows that Amara is watching.
Ines and Goran leave the kitchen. Bruno moves the harmonica to the red box.
Bruno leaves the kitchen. Amara comes back into the kitchen. Amara moves the harmonica to the canvas sack.
Soren moves the harmonica to the blue drawer.

- **reality** (tier None) At the end of the story, where is the harmonica really?
  A. the green cupboard | B. the red box | C. the blue drawer | D. the canvas sack
  gold: **C**
- **k1-hard** (tier 2) At the end of the story, where does Goran think the harmonica is?
  A. the green cupboard | B. the canvas sack | C. the red box | D. the blue drawer
  gold: **A** [real=the blue drawer; Goran=the green cupboard]
- **act1** (tier 2) At the end of the story, Goran needs the harmonica and goes to fetch it. Which container does Goran open first?
  A. the red box | B. the green cupboard | C. the canvas sack | D. the blue drawer
  gold: **B** [real=the blue drawer; Goran=the green cupboard]
- **k1-control** (tier 0) At the end of the story, where does Soren think the harmonica is?
  A. the green cupboard | B. the red box | C. the blue drawer | D. the canvas sack
  gold: **C** [real=the blue drawer; Soren=the blue drawer]
- **k2-hard** (tier 3) At the end of the story, where does Luca think that Soren thinks the harmonica is?
  A. the green cupboard | B. the canvas sack | C. the blue drawer | D. the red box
  gold: **A** [real=the blue drawer; Luca=the blue drawer; Luca>Soren=the green cupboard]
- **act2** (tier 3) At the end of the story, Soren is about to fetch the harmonica. Luca wants to be waiting beside the container that Soren will open first, and must pick the spot before Soren moves. Beside which container does Luca wait?
  A. the green cupboard | B. the blue drawer | C. the canvas sack | D. the red box
  gold: **A** [real=the blue drawer; Luca=the blue drawer; Luca>Soren=the green cupboard]
- **k2-control** (tier 1) At the end of the story, where does Soren think that Goran thinks the harmonica is?
  A. the red box | B. the blue drawer | C. the green cupboard | D. the canvas sack
  gold: **C** [real=the blue drawer; Soren=the blue drawer; Soren>Goran=the green cupboard]
- **k3-hard** (tier 3) At the end of the story, where does Ines think that Soren thinks that Amara thinks the harmonica is?
  A. the green cupboard | B. the canvas sack | C. the red box | D. the blue drawer
  gold: **C** [real=the blue drawer; Ines=the green cupboard; Ines>Soren=the green cupboard; Ines>Soren>Amara=the red box]
- **k3-control** (tier 1) At the end of the story, where does Ines think that Bruno thinks that Goran thinks the harmonica is?
  A. the red box | B. the canvas sack | C. the green cupboard | D. the blue drawer
  gold: **C** [real=the blue drawer; Ines=the green cupboard; Ines>Bruno=the green cupboard; Ines>Bruno>Goran=the green cupboard]
- **k4-hard** (tier 3) At the end of the story, where does Amara think that Bruno thinks that Goran thinks that Amara thinks the harmonica is?
  A. the red box | B. the blue drawer | C. the canvas sack | D. the green cupboard
  gold: **A** [real=the blue drawer; Amara=the blue drawer; Amara>Bruno=the green cupboard; Amara>Bruno>Goran=the green cupboard; Amara>Bruno>Goran>Amara=the red box]
- **k4-control** (tier 1) At the end of the story, where does Uma think that Soren thinks that Ines thinks that Goran thinks the harmonica is?
  A. the canvas sack | B. the green cupboard | C. the blue drawer | D. the red box
  gold: **B** [real=the blue drawer; Uma=the blue drawer; Uma>Soren=the blue drawer; Uma>Soren>Ines=the green cupboard; Uma>Soren>Ines>Goran=the green cupboard]
- **k5-hard** (tier 3) At the end of the story, where does Goran think that Bruno thinks that Uma thinks that Ines thinks that Amara thinks the harmonica is?
  A. the blue drawer | B. the canvas sack | C. the green cupboard | D. the red box
  gold: **D** [real=the blue drawer; Goran=the green cupboard; Goran>Bruno=the green cupboard; Goran>Bruno>Uma=the green cupboard; Goran>Bruno>Uma>Ines=the green cupboard; Goran>Bruno>Uma>Ines>Amara=the red box]
- **k5-control** (tier 0) At the end of the story, where does Ines think that Goran thinks that Hana thinks that Goran thinks that Hana thinks the harmonica is?
  A. the canvas sack | B. the red box | C. the green cupboard | D. the blue drawer
  gold: **D** [real=the blue drawer; Ines=the green cupboard; Ines>Goran=the green cupboard; Ines>Goran>Hana=the blue drawer; Ines>Goran>Hana>Goran=the blue drawer; Ines>Goran>Hana>Goran>Hana=the blue drawer]
- **k6-hard** (tier 3) At the end of the story, where does Soren think that Uma thinks that Hana thinks that Goran thinks that Uma thinks that Luca thinks the harmonica is?
  A. the blue drawer | B. the canvas sack | C. the red box | D. the green cupboard
  gold: **C** [real=the blue drawer; Soren=the blue drawer; Soren>Uma=the blue drawer; Soren>Uma>Hana=the blue drawer; Soren>Uma>Hana>Goran=the blue drawer; Soren>Uma>Hana>Goran>Uma=the blue drawer; Soren>Uma>Hana>Goran>Uma>Luca=the red box]
- **k6-control** (tier 0) At the end of the story, where does Hana think that Amara thinks that Luca thinks that Hana thinks that Amara thinks that Goran thinks the harmonica is?
  A. the canvas sack | B. the green cupboard | C. the red box | D. the blue drawer
  gold: **D** [real=the blue drawer; Hana=the blue drawer; Hana>Amara=the green cupboard; Hana>Amara>Luca=the blue drawer; Hana>Amara>Luca>Hana=the blue drawer; Hana>Amara>Luca>Hana>Amara=the blue drawer; Hana>Amara>Luca>Hana>Amara>Goran=the blue drawer]
- **inform** (tier None) At the end of the story, Luca wants everybody else to share Luca's own view of where the harmonica is. Luca sends a private note to every person who, as far as Luca can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Luca?
  
  gold: **Soren, Uma**

## Scenario H001 (workplace, 1 fact(s), 40 events, seed 1301000)

Xavier, Tariq, Uma, Viktor, Wanjiru, Farah, Pablo and Soren work on the same team. This is what happened, in order.
1. Call with Xavier, Tariq, Uma, Viktor, Wanjiru, Farah, Pablo and Soren: Tariq picks Northwind as the packaging supplier.
2. Call with Xavier, Uma, Wanjiru, Farah, Pablo and Soren: Soren switches the packaging supplier to Sablewood.
3. Xavier sends Tariq a direct message: “The packaging supplier is Sablewood.”
4. Wanjiru wants to mislead Viktor, so Wanjiru sends Viktor a direct message: “The packaging supplier is Halcyon.”
5. Call with Xavier, Uma, Wanjiru, Farah and Pablo: Farah switches the packaging supplier to Ironbridge.
6. Uma sends Viktor a direct message: “The packaging supplier is Ironbridge.” Farah secretly reads this message on Viktor's screen. Neither Uma nor Viktor ever knows that Farah read it.
7. Call with Xavier, Tariq, Uma, Wanjiru, Farah and Pablo: Wanjiru switches the packaging supplier to Northwind. Viktor is not on the call but secretly listens in, and can see who is on it. Nobody knows that Viktor is listening.
8. Farah wants to mislead Soren, so Farah sends Soren a direct message: “The packaging supplier is Ironbridge.”
9. Call with Xavier, Tariq, Uma, Wanjiru, Farah and Pablo: Farah switches the packaging supplier to Halcyon.
10. Farah sends Viktor a direct message: “The packaging supplier is Halcyon.”
11. Call with Xavier, Tariq, Uma, Wanjiru, Farah and Pablo: Uma switches the packaging supplier to Ironbridge.
12. Viktor wants to mislead Tariq, so Viktor sends Tariq a direct message: “The packaging supplier is Ironbridge.”
13. Call with Xavier, Tariq, Wanjiru, Farah and Pablo: Tariq switches the packaging supplier to Sablewood.
14. Call with Xavier, Tariq, Wanjiru, Farah and Pablo: Xavier switches the packaging supplier to Ironbridge. Uma is not on the call but secretly listens in, and can see who is on it. Nobody knows that Uma is listening.
15. Xavier sends Soren a direct message: “The packaging supplier is Ironbridge.”
16. Pablo sends Viktor a direct message: “The packaging supplier is Ironbridge.”
17. Soren sends Wanjiru a direct message: “The packaging supplier is Ironbridge.”
18. Call with Tariq, Wanjiru, Farah and Pablo: Tariq switches the packaging supplier to Northwind. Pablo is on the call but has stepped away from the desk and misses this. Nobody realises that Pablo missed it. Xavier is not on the call but secretly listens in, and can see who is on it. Nobody knows that Xavier is listening.
19. Call with Tariq, Wanjiru and Pablo: Pablo switches the packaging supplier to Ironbridge.
20. Call with Tariq, Wanjiru and Pablo: Pablo switches the packaging supplier to Northwind.
21. Pablo sends Uma a direct message: “The packaging supplier is Northwind.”
22. Call with Tariq, Wanjiru, Farah and Pablo: Pablo switches the packaging supplier to Halcyon.
23. Call with Tariq, Wanjiru, Farah and Pablo: Tariq switches the packaging supplier to Ironbridge.
24. Call with Tariq, Wanjiru, Farah and Pablo: Wanjiru switches the packaging supplier to Halcyon. Farah is on the call but has stepped away from the desk and misses this. Nobody realises that Farah missed it.
25. Xavier wants to mislead Uma, so Xavier sends Uma a direct message: “The packaging supplier is Sablewood.”
26. Call with Tariq, Wanjiru, Farah, Pablo and Soren: Farah switches the packaging supplier to Sablewood. Xavier is not on the call but secretly listens in, and can see who is on it. Nobody knows that Xavier is listening.
27. Call with Tariq, Wanjiru, Farah, Pablo and Soren: Soren switches the packaging supplier to Halcyon.
28. Uma wants to mislead Wanjiru, so Uma sends Wanjiru a direct message: “The packaging supplier is Halcyon.” Xavier secretly reads this message on Wanjiru's screen. Neither Uma nor Wanjiru ever knows that Xavier read it.
29. Farah wants to mislead Uma, so Farah sends Uma a direct message: “The packaging supplier is Sablewood.”
30. Call with Tariq, Wanjiru and Farah: Wanjiru switches the packaging supplier to Northwind. Viktor is not on the call but secretly listens in, and can see who is on it. Nobody knows that Viktor is listening.
31. Call with Tariq, Wanjiru and Farah: Farah switches the packaging supplier to Sablewood.
32. Call with Uma, Wanjiru and Farah: Farah switches the packaging supplier to Northwind.
33. Tariq sends Soren a direct message: “The packaging supplier is Sablewood.”
34. Wanjiru sends Soren a direct message: “The packaging supplier is Northwind.”
35. Wanjiru wants to mislead Tariq, so Wanjiru sends Tariq a direct message: “The packaging supplier is Ironbridge.”
36. Wanjiru sends Xavier a direct message: “The packaging supplier is Northwind.”
37. Uma wants to mislead Tariq, so Uma sends Tariq a direct message: “The packaging supplier is Halcyon.”
38. Soren sends Xavier a direct message: “The packaging supplier is Northwind.”
39. Call with Tariq, Uma, Wanjiru and Farah: Wanjiru switches the packaging supplier to Ironbridge.
40. Call with Xavier, Uma, Wanjiru and Farah: Wanjiru switches the packaging supplier to Sablewood.
41. Xavier wants to mislead Viktor, so Xavier sends Viktor a direct message: “The packaging supplier is Halcyon.”

- **reality** (tier None) At the end of the story, which company is really the packaging supplier?
  A. Sablewood | B. Northwind | C. Halcyon | D. Ironbridge
  gold: **A**
- **k1-hard** (tier 2) At the end of the story, which company does Pablo think is the packaging supplier?
  A. Northwind | B. Ironbridge | C. Halcyon | D. Sablewood
  gold: **C** [real=Sablewood; Pablo=Halcyon]
- **act1** (tier 2) At the end of the story, a new client asks Pablo which company is the packaging supplier. Pablo answers honestly. What does Pablo say?
  A. Ironbridge | B. Northwind | C. Sablewood | D. Halcyon
  gold: **D** [real=Sablewood; Pablo=Halcyon]
- **k1-control** (tier 0) At the end of the story, which company does Wanjiru think is the packaging supplier?
  A. Sablewood | B. Ironbridge | C. Northwind | D. Halcyon
  gold: **A** [real=Sablewood; Wanjiru=Sablewood]
- **k2-hard** (tier 3) At the end of the story, which company does Farah think that Soren thinks is the packaging supplier?
  A. Ironbridge | B. Halcyon | C. Sablewood | D. Northwind
  gold: **B** [real=Sablewood; Farah=Sablewood; Farah>Soren=Halcyon]
- **act2** (tier 3) At the end of the story, a new client is about to ask Soren which company is the packaging supplier, and Soren will answer honestly. Before Soren answers, Farah writes down what Farah expects Soren to say. What does Farah write?
  A. Ironbridge | B. Sablewood | C. Northwind | D. Halcyon
  gold: **D** [real=Sablewood; Farah=Sablewood; Farah>Soren=Halcyon]
- **k2-control** (tier 0) At the end of the story, which company does Xavier think that Uma thinks is the packaging supplier?
  A. Ironbridge | B. Sablewood | C. Northwind | D. Halcyon
  gold: **B** [real=Sablewood; Xavier=Sablewood; Xavier>Uma=Sablewood]
- **k3-hard** (tier 3) At the end of the story, which company does Wanjiru think that Tariq thinks that Soren thinks is the packaging supplier?
  A. Halcyon | B. Ironbridge | C. Northwind | D. Sablewood
  gold: **A** [real=Sablewood; Wanjiru=Sablewood; Wanjiru>Tariq=Ironbridge; Wanjiru>Tariq>Soren=Halcyon]
- **k3-control** (tier 1) At the end of the story, which company does Tariq think that Xavier thinks that Soren thinks is the packaging supplier?
  A. Halcyon | B. Northwind | C. Ironbridge | D. Sablewood
  gold: **B** [real=Sablewood; Tariq=Ironbridge; Tariq>Xavier=Ironbridge; Tariq>Xavier>Soren=Northwind]
- **k4-hard** (tier 3) At the end of the story, which company does Tariq think that Pablo thinks that Soren thinks that Xavier thinks is the packaging supplier?
  A. Halcyon | B. Sablewood | C. Ironbridge | D. Northwind
  gold: **D** [real=Sablewood; Tariq=Ironbridge; Tariq>Pablo=Halcyon; Tariq>Pablo>Soren=Halcyon; Tariq>Pablo>Soren>Xavier=Northwind]
- **k4-control** (tier 0) At the end of the story, which company does Farah think that Uma thinks that Soren thinks that Farah thinks is the packaging supplier?
  A. Northwind | B. Sablewood | C. Ironbridge | D. Halcyon
  gold: **B** [real=Sablewood; Farah=Sablewood; Farah>Uma=Sablewood; Farah>Uma>Soren=Sablewood; Farah>Uma>Soren>Farah=Sablewood]
- **k5-hard** (tier 3) At the end of the story, which company does Soren think that Wanjiru thinks that Pablo thinks that Xavier thinks that Tariq thinks is the packaging supplier?
  A. Northwind | B. Ironbridge | C. Sablewood | D. Halcyon
  gold: **A** [real=Sablewood; Soren=Northwind; Soren>Wanjiru=Northwind; Soren>Wanjiru>Pablo=Halcyon; Soren>Wanjiru>Pablo>Xavier=Sablewood; Soren>Wanjiru>Pablo>Xavier>Tariq=Northwind]
- **k5-control** (tier 1) At the end of the story, which company does Wanjiru think that Tariq thinks that Uma thinks that Tariq thinks that Soren thinks is the packaging supplier?
  A. Sablewood | B. Halcyon | C. Northwind | D. Ironbridge
  gold: **C** [real=Sablewood; Wanjiru=Sablewood; Wanjiru>Tariq=Ironbridge; Wanjiru>Tariq>Uma=Ironbridge; Wanjiru>Tariq>Uma>Tariq=Ironbridge; Wanjiru>Tariq>Uma>Tariq>Soren=Northwind]
- **k6-hard** (tier 3) At the end of the story, which company does Soren think that Farah thinks that Xavier thinks that Pablo thinks that Farah thinks that Tariq thinks is the packaging supplier?
  A. Ironbridge | B. Northwind | C. Halcyon | D. Sablewood
  gold: **B** [real=Sablewood; Soren=Northwind; Soren>Farah=Halcyon; Soren>Farah>Xavier=Sablewood; Soren>Farah>Xavier>Pablo=Sablewood; Soren>Farah>Xavier>Pablo>Farah=Sablewood; Soren>Farah>Xavier>Pablo>Farah>Tariq=Northwind]
- **k6-control** (tier 1) At the end of the story, which company does Uma think that Tariq thinks that Pablo thinks that Wanjiru thinks that Xavier thinks that Soren thinks is the packaging supplier?
  A. Sablewood | B. Halcyon | C. Ironbridge | D. Northwind
  gold: **D** [real=Sablewood; Uma=Sablewood; Uma>Tariq=Ironbridge; Uma>Tariq>Pablo=Ironbridge; Uma>Tariq>Pablo>Wanjiru=Ironbridge; Uma>Tariq>Pablo>Wanjiru>Xavier=Ironbridge; Uma>Tariq>Pablo>Wanjiru>Xavier>Soren=Northwind]
- **inform** (tier None) At the end of the story, Soren wants everybody else on the team to share Soren's own view of which company is the packaging supplier. Soren sends a direct message to every person who, as far as Soren can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Soren?
  
  gold: **Farah, Pablo, Tariq, Uma**

## Scenario H002 (classic, 2 fact(s), 40 events, seed 1302001)

Yara, Goran, Xavier, Soren, Rania, Dalia, Hana and Uma are in the sunroom. On the floor of the sunroom there are four closed containers that nobody can see into: the red box, the white cabinet, the blue drawer and the grey locker. On a shelf there are four closed tins that nobody can see into: the copper tin, the flat tin, the square tin and the round tin. The tins are empty at the start, and the whistle is only ever kept in the containers on the floor.
While everyone watches, Yara puts a whistle in the white cabinet.
Soren and Rania leave the sunroom. Hana moves the whistle to the blue drawer.
Yara sends Rania a private text message: “The whistle is in the blue drawer.”
Hana wants to mislead Soren, so Hana sends Soren a private text message: “The whistle is in the grey locker.”
Goran wants to mislead Soren, so Goran sends Soren a private text message: “The whistle is in the red box.”
Xavier and Uma leave the sunroom. Goran moves the whistle to the white cabinet. Hana is in the sunroom but is absorbed in a phone and does not notice this. Nobody realises that Hana missed it.
Rania comes back into the sunroom. Dalia opens every container on the floor in full view of the sunroom, showing that the whistle is in the white cabinet. Xavier is outside but watches all of this through the window. Nobody knows that Xavier is watching.
Rania leaves the sunroom. Hana moves the whistle to the blue drawer. Xavier is outside but watches all of this through the window. Nobody knows that Xavier is watching.
Hana sends Rania a private text message: “The whistle is in the blue drawer.”
Soren wants to mislead Dalia, so Soren sends Dalia a private text message: “The whistle is in the blue drawer.”
Hana leaves the sunroom. Goran moves the whistle to the red box. Rania is outside but watches all of this through the window. Nobody knows that Rania is watching.
Goran sends Xavier a private text message: “The whistle is in the red box.”
Yara moves the whistle to the blue drawer.
Goran wants to mislead Rania, so Goran sends Rania a private text message: “The whistle is in the grey locker.”
Yara wants to mislead Soren, so Yara sends Soren a private text message: “The whistle is in the red box.”
Xavier sends Soren a private text message: “The whistle is in the red box.”
Yara moves the whistle to the red box. Rania is outside but watches all of this through the window. Nobody knows that Rania is watching.
Xavier sends Yara a private text message: “The whistle is in the red box.”
Goran moves the whistle to the white cabinet.
Yara and Dalia leave the sunroom. Hana and Uma come back into the sunroom. Hana takes a thimble out of a pocket and puts it in the square tin. Rania is outside but watches all of this through the window. Nobody knows that Rania is watching.
Goran sends Yara a private text message: “The thimble is in the square tin.”
Soren wants to mislead Uma, so Soren sends Uma a private text message: “The whistle is in the grey locker.”
Soren comes back into the sunroom. Uma moves the thimble to the flat tin.
Soren leaves the sunroom. Goran moves the whistle to the red box. Uma is in the sunroom but is absorbed in a phone and does not notice this. Nobody realises that Uma missed it.
Dalia sends Uma a private text message: “The whistle is in the white cabinet.”
Xavier comes back into the sunroom. Hana moves the thimble to the round tin.
Soren sends Dalia a private text message: “The thimble is in the flat tin.”
Rania comes back into the sunroom. Uma opens every tin on the shelf in full view of the sunroom, showing that the thimble is in the round tin.
Dalia sends Yara a private text message: “The thimble is in the flat tin.”
Uma moves the thimble to the flat tin. Rania is in the sunroom but is absorbed in a phone and does not notice this. Nobody realises that Rania missed it.
Goran wants to mislead Yara, so Goran sends Yara a private text message: “The whistle is in the blue drawer.”
Goran leaves the sunroom. Dalia comes back into the sunroom. Uma opens every container on the floor in full view of the sunroom, showing that the whistle is in the red box.
Yara comes back into the sunroom. Yara opens every container on the floor in full view of the sunroom, showing that the whistle is in the red box.
Soren sends Xavier a private text message: “The thimble is in the flat tin.”
Goran comes back into the sunroom. Dalia moves the whistle to the grey locker. Soren is outside but watches all of this through the window. Nobody knows that Soren is watching.
Dalia leaves the sunroom. Uma says out loud to everyone in the sunroom: “The thimble is in the flat tin.” Xavier is in the sunroom but is wearing earphones and does not hear this. Nobody realises that Xavier missed it.
Dalia sends Soren a private text message: “The whistle is in the grey locker.”
Hana leaves the sunroom. Dalia comes back into the sunroom. Xavier moves the whistle to the white cabinet.
Soren comes back into the sunroom. Yara moves the thimble to the round tin.
Xavier wants to mislead Hana, so Xavier sends Hana a private text message: “The whistle is in the blue drawer.” Soren secretly reads this message on Hana's phone. Neither Xavier nor Hana ever knows that Soren read it.
Uma leaves the sunroom. Goran opens every container on the floor in full view of the sunroom, showing that the whistle is in the white cabinet. Uma is outside but watches all of this through the window. Nobody knows that Uma is watching.

- **reality** (tier None) At the end of the story, where is the whistle really?
  A. the white cabinet | B. the grey locker | C. the red box | D. the blue drawer
  gold: **A**
- **k1-hard** (tier 2) At the end of the story, where does Hana think the whistle is?
  A. the white cabinet | B. the red box | C. the blue drawer | D. the grey locker
  gold: **C** [real=the white cabinet; Hana=the blue drawer]
- **act1** (tier 2) At the end of the story, Hana needs the whistle and goes to fetch it. Which container does Hana open first?
  A. the grey locker | B. the white cabinet | C. the blue drawer | D. the red box
  gold: **C** [real=the white cabinet; Hana=the blue drawer]
- **k1-control** (tier 0) At the end of the story, where does Rania think the thimble is?
  A. the square tin | B. the round tin | C. the flat tin | D. the copper tin | E. Rania has no idea where the thimble is
  gold: **B** [real=the round tin; Rania=the round tin]
- **k2-hard** (tier 3) At the end of the story, where does Goran think that Hana thinks the whistle is?
  A. the red box | B. the grey locker | C. the blue drawer | D. the white cabinet
  gold: **B** [real=the white cabinet; Goran=the white cabinet; Goran>Hana=the grey locker]
- **act2** (tier 3) At the end of the story, Hana is about to fetch the whistle. Goran wants to be waiting beside the container that Hana will open first, and must pick the spot before Hana moves. Beside which container does Goran wait?
  A. the white cabinet | B. the grey locker | C. the blue drawer | D. the red box
  gold: **B** [real=the white cabinet; Goran=the white cabinet; Goran>Hana=the grey locker]
- **k2-control** (tier 0) At the end of the story, where does Xavier think that Rania thinks the thimble is?
  A. the copper tin | B. the flat tin | C. the square tin | D. the round tin | E. Xavier thinks that Rania has no idea where the thimble is
  gold: **D** [real=the round tin; Xavier=the round tin; Xavier>Rania=the round tin]
- **k3-hard** (tier 3) At the end of the story, where does Hana think that Xavier thinks that Rania thinks the whistle is?
  A. the white cabinet | B. the blue drawer | C. the grey locker | D. the red box
  gold: **C** [real=the white cabinet; Hana=the blue drawer; Hana>Xavier=the blue drawer; Hana>Xavier>Rania=the grey locker]
- **k3-control** (tier 1) At the end of the story, where does Soren think that Xavier thinks that Hana thinks the whistle is?
  A. the blue drawer | B. the grey locker | C. the white cabinet | D. the red box
  gold: **A** [real=the white cabinet; Soren=the white cabinet; Soren>Xavier=the white cabinet; Soren>Xavier>Hana=the blue drawer]
- **k4-hard** (tier 3) At the end of the story, where does Soren think that Yara thinks that Xavier thinks that Uma thinks the whistle is?
  A. the grey locker | B. the blue drawer | C. the white cabinet | D. the red box
  gold: **A** [real=the white cabinet; Soren=the white cabinet; Soren>Yara=the white cabinet; Soren>Yara>Xavier=the white cabinet; Soren>Yara>Xavier>Uma=the grey locker]
- **k4-control** (tier 0) At the end of the story, where does Uma think that Goran thinks that Soren thinks that Rania thinks the thimble is?
  A. the copper tin | B. the round tin | C. the square tin | D. the flat tin
  gold: **B** [real=the round tin; Uma=the round tin; Uma>Goran=the round tin; Uma>Goran>Soren=the round tin; Uma>Goran>Soren>Rania=the round tin]
- **k5-hard** (tier 3) At the end of the story, where does Soren think that Dalia thinks that Xavier thinks that Goran thinks that Uma thinks the whistle is?
  A. the blue drawer | B. the grey locker | C. the red box | D. the white cabinet
  gold: **B** [real=the white cabinet; Soren=the white cabinet; Soren>Dalia=the white cabinet; Soren>Dalia>Xavier=the white cabinet; Soren>Dalia>Xavier>Goran=the white cabinet; Soren>Dalia>Xavier>Goran>Uma=the grey locker]
- **k5-control** (tier 0) At the end of the story, where does Hana think that Soren thinks that Rania thinks that Yara thinks that Hana thinks the whistle is?
  A. the blue drawer | B. the grey locker | C. the red box | D. the white cabinet
  gold: **D** [real=the white cabinet; Hana=the blue drawer; Hana>Soren=the grey locker; Hana>Soren>Rania=the white cabinet; Hana>Soren>Rania>Yara=the white cabinet; Hana>Soren>Rania>Yara>Hana=the white cabinet]
- **k6-hard** (tier 3) At the end of the story, where does Soren think that Dalia thinks that Xavier thinks that Rania thinks that Goran thinks that Uma thinks the whistle is?
  A. the white cabinet | B. the red box | C. the blue drawer | D. the grey locker
  gold: **D** [real=the white cabinet; Soren=the white cabinet; Soren>Dalia=the white cabinet; Soren>Dalia>Xavier=the white cabinet; Soren>Dalia>Xavier>Rania=the white cabinet; Soren>Dalia>Xavier>Rania>Goran=the white cabinet; Soren>Dalia>Xavier>Rania>Goran>Uma=the grey locker]
- **k6-control** (tier 1) At the end of the story, where does Hana think that Goran thinks that Rania thinks that Hana thinks that Uma thinks that Hana thinks the thimble is?
  A. the square tin | B. the round tin | C. the flat tin | D. the copper tin
  gold: **C** [real=the round tin; Hana=the flat tin; Hana>Goran=the flat tin; Hana>Goran>Rania=the flat tin; Hana>Goran>Rania>Hana=the flat tin; Hana>Goran>Rania>Hana>Uma=the flat tin; Hana>Goran>Rania>Hana>Uma>Hana=the flat tin]
- **inform** (tier None) At the end of the story, Hana wants everybody else to share Hana's own view of where the whistle is. Hana sends a private note to every person who, as far as Hana can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Hana?
  
  gold: **Dalia, Goran, Rania, Soren, Uma, Yara**
- **know** (tier None) At the end of the story, where does Dalia think that Hana thinks the thimble is?
  A. the square tin | B. the round tin | C. the copper tin | D. the flat tin | E. Dalia thinks that Hana has no idea where the thimble is
  gold: **E** [real=the round tin; Dalia=the round tin; Dalia>Hana=no idea]

## Scenario H003 (workplace, 2 fact(s), 40 events, seed 1303000)

Pablo, Luca, Oksana, Ines, Hana, Mirela, Jonas and Rania work on the same team. This is what happened, in order.
1. Call with Pablo, Luca, Oksana, Ines, Hana, Mirela, Jonas and Rania: Luca assigns the Marlow account to the Lisbon office.
2. Call with Pablo, Luca, Oksana, Ines, Jonas and Rania: Ines reassigns the Marlow account to the Osaka office.
3. Luca sends Hana a direct message: “The Marlow account is with the Osaka office.” Oksana secretly reads this message on Hana's screen. Neither Luca nor Hana ever knows that Oksana read it.
4. Call with Pablo, Luca, Oksana, Ines, Jonas and Rania: Pablo reassigns the Marlow account to the Denver office.
5. Luca wants to mislead Mirela, so Luca sends Mirela a direct message: “The Marlow account is with the Osaka office.” Hana secretly reads this message on Mirela's screen. Neither Luca nor Mirela ever knows that Hana read it.
6. Ines sends Hana a direct message: “The Marlow account is with the Denver office.”
7. Call with Pablo, Luca, Ines, Jonas and Rania: Luca reassigns the Marlow account to the Nairobi office.
8. Mirela wants to mislead Hana, so Mirela sends Hana a direct message: “The Marlow account is with the Nairobi office.”
9. Call with Pablo, Luca, Ines, Jonas and Rania: Rania reassigns the Marlow account to the Denver office.
10. Call with Pablo, Ines, Jonas and Rania: Jonas reassigns the Marlow account to the Nairobi office. Ines is on the call but has stepped away from the desk and misses this. Nobody realises that Ines missed it.
11. Call with Pablo, Oksana, Ines, Hana, Jonas and Rania: Rania says: “The Marlow account is with the Nairobi office.”
12. Jonas sends Mirela a direct message: “The Marlow account is with the Nairobi office.”
13. Hana wants to mislead Luca, so Hana sends Luca a direct message: “The Marlow account is with the Denver office.”
14. Rania wants to mislead Luca, so Rania sends Luca a direct message: “The Marlow account is with the Lisbon office.”
15. Call with Oksana, Ines, Hana, Jonas and Rania: Rania reassigns the Marlow account to the Osaka office.
16. Call with Oksana, Ines, Jonas and Rania: Oksana reassigns the Marlow account to the Lisbon office.
17. Pablo wants to mislead Mirela, so Pablo sends Mirela a direct message: “The Marlow account is with the Osaka office.”
18. Call with Pablo and Hana: Pablo sets the discount on the Fenwick quote at 25%.
19. Pablo sends Jonas a direct message: “The discount on the Fenwick quote is 25%.” Rania secretly reads this message on Jonas's screen. Neither Pablo nor Jonas ever knows that Rania read it.
20. Hana wants to mislead Pablo, so Hana sends Pablo a direct message: “The Marlow account is with the Lisbon office.”
21. Rania wants to mislead Mirela, so Rania sends Mirela a direct message: “The discount on the Fenwick quote is 10%.”
22. Call with Pablo, Oksana, Ines and Hana: Hana reassigns the Marlow account to the Osaka office.
23. Hana sends Mirela a direct message: “The Marlow account is with the Osaka office.”
24. Call with Pablo, Oksana, Ines and Hana: Ines reassigns the Marlow account to the Denver office.
25. Call with Pablo, Oksana, Ines, Hana, Mirela and Jonas: Oksana opens the account list and reads it out: “The Marlow account is with the Denver office.”
26. Call with Pablo, Oksana, Ines, Hana, Mirela and Jonas: Hana changes the discount on the Fenwick quote to 15%.
27. Call with Ines, Hana, Mirela and Jonas: Ines reassigns the Marlow account to the Nairobi office.
28. Call with Oksana, Ines, Hana, Mirela, Jonas and Rania: Hana says: “The Marlow account is with the Nairobi office.”
29. Call with Oksana, Ines, Mirela, Jonas and Rania: Oksana changes the discount on the Fenwick quote to 25%.
30. Jonas sends Pablo a direct message: “The Marlow account is with the Nairobi office.”
31. Ines sends Luca a direct message: “The Marlow account is with the Nairobi office.” Hana secretly reads this message on Luca's screen. Neither Ines nor Luca ever knows that Hana read it.
32. Call with Oksana, Mirela, Jonas and Rania: Mirela reassigns the Marlow account to the Osaka office.
33. Call with Pablo, Oksana, Mirela and Jonas: Oksana opens the quote record and reads it out: “The discount on the Fenwick quote is 25%.” Jonas is on the call but has stepped away from the desk and misses this. Nobody realises that Jonas missed it.
34. Call with Pablo, Oksana, Mirela and Jonas: Pablo changes the discount on the Fenwick quote to 20%. Oksana is on the call but has stepped away from the desk and misses this. Nobody realises that Oksana missed it.
35. Rania wants to mislead Hana, so Rania sends Hana a direct message: “The Marlow account is with the Denver office.”
36. Call with Pablo, Luca, Oksana and Mirela: Oksana reassigns the Marlow account to the Lisbon office. Ines is not on the call but secretly listens in, and can see who is on it. Nobody knows that Ines is listening.
37. Oksana sends Jonas a direct message: “The Marlow account is with the Lisbon office.”
38. Luca sends Ines a direct message: “The Marlow account is with the Lisbon office.”
39. Call with Pablo, Luca, Oksana and Mirela: Mirela reassigns the Marlow account to the Denver office. Jonas is not on the call but secretly listens in, and can see who is on it. Nobody knows that Jonas is listening.
40. Rania wants to mislead Luca, so Rania sends Luca a direct message: “The discount on the Fenwick quote is 15%.” Oksana secretly reads this message on Luca's screen. Neither Rania nor Luca ever knows that Oksana read it.
41. Call with Pablo, Luca and Oksana: Oksana changes the discount on the Fenwick quote to 25%. Mirela is not on the call but secretly listens in, and can see who is on it. Nobody knows that Mirela is listening.

- **reality** (tier None) At the end of the story, what discount is really on the Fenwick quote?
  A. 20% | B. 10% | C. 15% | D. 25%
  gold: **D**
- **k1-hard** (tier 2) At the end of the story, which office does Rania think has the Marlow account?
  A. the Lisbon office | B. the Osaka office | C. the Nairobi office | D. the Denver office
  gold: **B** [real=the Denver office; Rania=the Osaka office]
- **act1** (tier 2) At the end of the story, a new client asks Rania which office has the Marlow account. Rania answers honestly. What does Rania say?
  A. the Nairobi office | B. the Lisbon office | C. the Denver office | D. the Osaka office
  gold: **D** [real=the Denver office; Rania=the Osaka office]
- **k1-control** (tier 0) At the end of the story, what discount does Luca think is on the Fenwick quote?
  A. 10% | B. 25% | C. 20% | D. 15% | E. Luca has no idea what discount is on the Fenwick quote
  gold: **B** [real=25%; Luca=25%]
- **k2-hard** (tier 3) At the end of the story, which office does Jonas think that Ines thinks has the Marlow account?
  A. the Osaka office | B. the Lisbon office | C. the Denver office | D. the Nairobi office
  gold: **D** [real=the Denver office; Jonas=the Denver office; Jonas>Ines=the Nairobi office]
- **act2** (tier 3) At the end of the story, a new client is about to ask Ines which office has the Marlow account, and Ines will answer honestly. Before Ines answers, Jonas writes down what Jonas expects Ines to say. What does Jonas write?
  A. the Lisbon office | B. the Osaka office | C. the Nairobi office | D. the Denver office
  gold: **C** [real=the Denver office; Jonas=the Denver office; Jonas>Ines=the Nairobi office]
- **k2-control** (tier 1) At the end of the story, what discount does Pablo think that Hana thinks is on the Fenwick quote?
  A. 25% | B. 20% | C. 10% | D. 15% | E. Pablo thinks that Hana has no idea what discount is on the Fenwick quote
  gold: **D** [real=25%; Pablo=25%; Pablo>Hana=15%]
- **k3-hard** (tier 3) At the end of the story, which office does Rania think that Jonas thinks that Pablo thinks has the Marlow account?
  A. the Denver office | B. the Lisbon office | C. the Nairobi office | D. the Osaka office
  gold: **C** [real=the Denver office; Rania=the Osaka office; Rania>Jonas=the Osaka office; Rania>Jonas>Pablo=the Nairobi office]
- **k3-control** (tier 1) At the end of the story, what discount does Ines think that Pablo thinks that Hana thinks is on the Fenwick quote?
  A. 25% | B. 15% | C. 20% | D. 10%
  gold: **B** [real=25%; Ines=25%; Ines>Pablo=15%; Ines>Pablo>Hana=15%]
- **k4-hard** (tier 3) At the end of the story, which office does Luca think that Jonas thinks that Pablo thinks that Mirela thinks has the Marlow account?
  A. the Osaka office | B. the Denver office | C. the Lisbon office | D. the Nairobi office
  gold: **C** [real=the Denver office; Luca=the Denver office; Luca>Jonas=the Denver office; Luca>Jonas>Pablo=the Denver office; Luca>Jonas>Pablo>Mirela=the Lisbon office]
- **k4-control** (tier 1) At the end of the story, which office does Mirela think that Rania thinks that Jonas thinks that Rania thinks has the Marlow account?
  A. the Nairobi office | B. the Osaka office | C. the Lisbon office | D. the Denver office
  gold: **B** [real=the Denver office; Mirela=the Denver office; Mirela>Rania=the Osaka office; Mirela>Rania>Jonas=the Osaka office; Mirela>Rania>Jonas>Rania=the Osaka office]
- **k5-hard** (tier 3) At the end of the story, which office does Pablo think that Ines thinks that Jonas thinks that Rania thinks that Mirela thinks has the Marlow account?
  A. the Osaka office | B. the Nairobi office | C. the Lisbon office | D. the Denver office
  gold: **C** [real=the Denver office; Pablo=the Denver office; Pablo>Ines=the Denver office; Pablo>Ines>Jonas=the Denver office; Pablo>Ines>Jonas>Rania=the Nairobi office; Pablo>Ines>Jonas>Rania>Mirela=the Lisbon office]
- **k5-control** (tier 1) At the end of the story, which office does Jonas think that Oksana thinks that Luca thinks that Mirela thinks that Ines thinks has the Marlow account?
  A. the Lisbon office | B. the Denver office | C. the Nairobi office | D. the Osaka office
  gold: **A** [real=the Denver office; Jonas=the Denver office; Jonas>Oksana=the Denver office; Jonas>Oksana>Luca=the Denver office; Jonas>Oksana>Luca>Mirela=the Denver office; Jonas>Oksana>Luca>Mirela>Ines=the Lisbon office]
- **k6-hard** (tier 3) At the end of the story, which office does Pablo think that Hana thinks that Mirela thinks that Hana thinks that Oksana thinks that Rania thinks has the Marlow account?
  A. the Nairobi office | B. the Lisbon office | C. the Osaka office | D. the Denver office
  gold: **B** [real=the Denver office; Pablo=the Denver office; Pablo>Hana=the Denver office; Pablo>Hana>Mirela=the Denver office; Pablo>Hana>Mirela>Hana=the Denver office; Pablo>Hana>Mirela>Hana>Oksana=the Denver office; Pablo>Hana>Mirela>Hana>Oksana>Rania=the Lisbon office]
- **k6-control** (tier 0) At the end of the story, which office does Ines think that Hana thinks that Oksana thinks that Pablo thinks that Jonas thinks that Pablo thinks has the Marlow account?
  A. the Nairobi office | B. the Lisbon office | C. the Denver office | D. the Osaka office
  gold: **C** [real=the Denver office; Ines=the Lisbon office; Ines>Hana=the Nairobi office; Ines>Hana>Oksana=the Nairobi office; Ines>Hana>Oksana>Pablo=the Denver office; Ines>Hana>Oksana>Pablo>Jonas=the Denver office; Ines>Hana>Oksana>Pablo>Jonas>Pablo=the Denver office]
- **inform** (tier None) At the end of the story, Mirela wants everybody else on the team to share Mirela's own view of which office has the Marlow account. Mirela sends a direct message to every person who, as far as Mirela can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Mirela?
  
  gold: **Hana, Ines, Jonas, Rania**
- **know** (tier None) At the end of the story, what discount does Luca think that Ines thinks is on the Fenwick quote?
  A. 20% | B. 25% | C. 10% | D. 15% | E. Luca thinks that Ines has no idea what discount is on the Fenwick quote
  gold: **E** [real=25%; Luca=25%; Luca>Ines=no idea]

## Scenario H004 (classic, 1 fact(s), 40 events, seed 1304000)

Soren, Mirela, Pablo, Amara, Zoltan, Yara, Luca and Nadim are in the greenhouse. The greenhouse has four closed containers that nobody can see into: the red box, the black trunk, the white cabinet and the green cupboard.
While everyone watches, Mirela puts a thimble in the green cupboard.
Nadim moves the thimble to the red box. Yara is in the greenhouse but is absorbed in a phone and does not notice this. Nobody realises that Yara missed it.
Yara moves the thimble to the green cupboard. Pablo is in the greenhouse but is absorbed in a phone and does not notice this. Nobody realises that Pablo missed it.
Mirela moves the thimble to the black trunk.
Zoltan moves the thimble to the white cabinet. Yara is in the greenhouse but is absorbed in a phone and does not notice this. Nobody realises that Yara missed it.
Zoltan leaves the greenhouse. Yara moves the thimble to the black trunk.
Nadim sends Zoltan a private text message: “The thimble is in the black trunk.”
Amara sends Zoltan a private text message: “The thimble is in the black trunk.”
Luca sends Zoltan a private text message: “The thimble is in the black trunk.” Mirela secretly reads this message on Zoltan's phone. Neither Luca nor Zoltan ever knows that Mirela read it.
Zoltan sends Soren a private text message: “The thimble is in the black trunk.”
Nadim moves the thimble to the white cabinet.
Soren wants to mislead Zoltan, so Soren sends Zoltan a private text message: “The thimble is in the green cupboard.”
Yara sends Zoltan a private text message: “The thimble is in the white cabinet.” Soren secretly reads this message on Zoltan's phone. Neither Yara nor Zoltan ever knows that Soren read it.
Zoltan sends Nadim a private text message: “The thimble is in the white cabinet.”
Zoltan sends Luca a private text message: “The thimble is in the white cabinet.”
Nadim moves the thimble to the black trunk.
Pablo sends Zoltan a private text message: “The thimble is in the black trunk.” Yara secretly reads this message on Zoltan's phone. Neither Pablo nor Zoltan ever knows that Yara read it.
Amara moves the thimble to the red box.
Mirela sends Zoltan a private text message: “The thimble is in the red box.”
Zoltan sends Yara a private text message: “The thimble is in the red box.”
Zoltan sends Pablo a private text message: “The thimble is in the red box.” Amara secretly reads this message on Pablo's phone. Neither Zoltan nor Pablo ever knows that Amara read it.
Yara moves the thimble to the black trunk. Zoltan is outside but watches all of this through the window. Nobody knows that Zoltan is watching.
Amara moves the thimble to the red box.
Luca leaves the greenhouse. Nadim moves the thimble to the white cabinet. Luca is outside but watches all of this through the window. Nobody knows that Luca is watching.
Yara sends Luca a private text message: “The thimble is in the white cabinet.”
Nadim sends Luca a private text message: “The thimble is in the white cabinet.”
Pablo sends Luca a private text message: “The thimble is in the white cabinet.” Soren secretly reads this message on Luca's phone. Neither Pablo nor Luca ever knows that Soren read it.
Amara sends Luca a private text message: “The thimble is in the white cabinet.” Pablo secretly reads this message on Luca's phone. Neither Amara nor Luca ever knows that Pablo read it.
Mirela leaves the greenhouse. Amara moves the thimble to the red box.
Amara sends Mirela a private text message: “The thimble is in the red box.”
Mirela comes back into the greenhouse. Soren moves the thimble to the white cabinet.
Soren leaves the greenhouse. Mirela moves the thimble to the black trunk. Amara is in the greenhouse but is absorbed in a phone and does not notice this. Nobody realises that Amara missed it.
Nadim moves the thimble to the red box.
Soren comes back into the greenhouse. Amara moves the thimble to the black trunk.
Amara and Nadim leave the greenhouse. Pablo moves the thimble to the red box. Nadim is outside but watches all of this through the window. Nobody knows that Nadim is watching.
Yara leaves the greenhouse. Mirela moves the thimble to the white cabinet. Pablo is in the greenhouse but is absorbed in a phone and does not notice this. Nobody realises that Pablo missed it. Luca is outside but watches all of this through the window. Nobody knows that Luca is watching.
Nadim comes back into the greenhouse. Soren moves the thimble to the black trunk. Zoltan is outside but watches all of this through the window. Nobody knows that Zoltan is watching.
Luca comes back into the greenhouse. Nadim moves the thimble to the red box. Amara is outside but watches all of this through the window. Nobody knows that Amara is watching.
Luca leaves the greenhouse. Soren moves the thimble to the white cabinet.
Amara sends Yara a private text message: “The thimble is in the red box.” Zoltan secretly reads this message on Yara's phone. Neither Amara nor Yara ever knows that Zoltan read it.
Soren sends Luca a private text message: “The thimble is in the white cabinet.”

- **reality** (tier None) At the end of the story, where is the thimble really?
  A. the black trunk | B. the green cupboard | C. the white cabinet | D. the red box
  gold: **C**
- **k1-hard** (tier 2) At the end of the story, where does Zoltan think the thimble is?
  A. the green cupboard | B. the white cabinet | C. the red box | D. the black trunk
  gold: **C** [real=the white cabinet; Zoltan=the red box]
- **act1** (tier 2) At the end of the story, Zoltan needs the thimble and goes to fetch it. Which container does Zoltan open first?
  A. the green cupboard | B. the white cabinet | C. the black trunk | D. the red box
  gold: **D** [real=the white cabinet; Zoltan=the red box]
- **k1-control** (tier 0) At the end of the story, where does Nadim think the thimble is?
  A. the red box | B. the green cupboard | C. the black trunk | D. the white cabinet
  gold: **D** [real=the white cabinet; Nadim=the white cabinet]
- **k2-hard** (tier 3) At the end of the story, where does Nadim think that Luca thinks the thimble is?
  A. the white cabinet | B. the red box | C. the black trunk | D. the green cupboard
  gold: **B** [real=the white cabinet; Nadim=the white cabinet; Nadim>Luca=the red box]
- **act2** (tier 3) At the end of the story, Luca is about to fetch the thimble. Nadim wants to be waiting beside the container that Luca will open first, and must pick the spot before Luca moves. Beside which container does Nadim wait?
  A. the white cabinet | B. the green cupboard | C. the black trunk | D. the red box
  gold: **D** [real=the white cabinet; Nadim=the white cabinet; Nadim>Luca=the red box]
- **k2-control** (tier 1) At the end of the story, where does Yara think that Zoltan thinks the thimble is?
  A. the black trunk | B. the red box | C. the green cupboard | D. the white cabinet
  gold: **B** [real=the white cabinet; Yara=the red box; Yara>Zoltan=the red box]
- **k3-hard** (tier 3) At the end of the story, where does Yara think that Amara thinks that Soren thinks the thimble is?
  A. the red box | B. the white cabinet | C. the green cupboard | D. the black trunk
  gold: **D** [real=the white cabinet; Yara=the red box; Yara>Amara=the red box; Yara>Amara>Soren=the black trunk]
- **k3-control** (tier 1) At the end of the story, where does Soren think that Luca thinks that Amara thinks the thimble is?
  A. the white cabinet | B. the black trunk | C. the red box | D. the green cupboard
  gold: **C** [real=the white cabinet; Soren=the white cabinet; Soren>Luca=the white cabinet; Soren>Luca>Amara=the red box]
- **k4-hard** (tier 3) At the end of the story, where does Amara think that Pablo thinks that Amara thinks that Luca thinks the thimble is?
  A. the red box | B. the green cupboard | C. the black trunk | D. the white cabinet
  gold: **A** [real=the white cabinet; Amara=the red box; Amara>Pablo=the red box; Amara>Pablo>Amara=the black trunk; Amara>Pablo>Amara>Luca=the red box]
- **k4-control** (tier 0) At the end of the story, where does Soren think that Mirela thinks that Pablo thinks that Zoltan thinks the thimble is?
  A. the white cabinet | B. the green cupboard | C. the red box | D. the black trunk
  gold: **A** [real=the white cabinet; Soren=the white cabinet; Soren>Mirela=the white cabinet; Soren>Mirela>Pablo=the white cabinet; Soren>Mirela>Pablo>Zoltan=the white cabinet]
- **k5-hard** (tier 3) At the end of the story, where does Yara think that Luca thinks that Pablo thinks that Nadim thinks that Zoltan thinks the thimble is?
  A. the white cabinet | B. the green cupboard | C. the red box | D. the black trunk
  gold: **D** [real=the white cabinet; Yara=the red box; Yara>Luca=the white cabinet; Yara>Luca>Pablo=the red box; Yara>Luca>Pablo>Nadim=the red box; Yara>Luca>Pablo>Nadim>Zoltan=the black trunk]
- **k5-control** (tier 1) At the end of the story, where does Soren think that Yara thinks that Soren thinks that Luca thinks that Amara thinks the thimble is?
  A. the black trunk | B. the red box | C. the white cabinet | D. the green cupboard
  gold: **B** [real=the white cabinet; Soren=the white cabinet; Soren>Yara=the red box; Soren>Yara>Soren=the red box; Soren>Yara>Soren>Luca=the red box; Soren>Yara>Soren>Luca>Amara=the red box]
- **k6-hard** (tier 3) At the end of the story, where does Yara think that Pablo thinks that Mirela thinks that Pablo thinks that Mirela thinks that Zoltan thinks the thimble is?
  A. the green cupboard | B. the red box | C. the white cabinet | D. the black trunk
  gold: **D** [real=the white cabinet; Yara=the red box; Yara>Pablo=the red box; Yara>Pablo>Mirela=the red box; Yara>Pablo>Mirela>Pablo=the red box; Yara>Pablo>Mirela>Pablo>Mirela=the red box; Yara>Pablo>Mirela>Pablo>Mirela>Zoltan=the black trunk]
- **k6-control** (tier 1) At the end of the story, where does Yara think that Luca thinks that Mirela thinks that Amara thinks that Mirela thinks that Amara thinks the thimble is?
  A. the red box | B. the green cupboard | C. the white cabinet | D. the black trunk
  gold: **A** [real=the white cabinet; Yara=the red box; Yara>Luca=the white cabinet; Yara>Luca>Mirela=the red box; Yara>Luca>Mirela>Amara=the red box; Yara>Luca>Mirela>Amara>Mirela=the red box; Yara>Luca>Mirela>Amara>Mirela>Amara=the red box]
- **inform** (tier None) At the end of the story, Yara wants everybody else to share Yara's own view of where the thimble is. Yara sends a private note to every person who, as far as Yara can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Yara?
  
  gold: **Luca, Nadim**

## Scenario H005 (workplace, 1 fact(s), 40 events, seed 1305000)

Zoltan, Yara, Jonas, Viktor, Xavier, Rania, Farah and Oksana work on the same team. This is what happened, in order.
1. Call with Zoltan, Yara, Jonas, Viktor, Xavier, Rania, Farah and Oksana: Rania picks Halcyon as the packaging supplier.
2. Call with Zoltan, Yara, Jonas, Viktor, Xavier, Rania and Farah: Jonas switches the packaging supplier to Ironbridge.
3. Xavier sends Oksana a direct message: “The packaging supplier is Ironbridge.” Yara secretly reads this message on Oksana's screen. Neither Xavier nor Oksana ever knows that Yara read it.
4. Call with Zoltan, Yara, Jonas, Viktor, Xavier and Rania: Viktor switches the packaging supplier to Brightwater.
5. Call with Zoltan, Yara, Jonas, Viktor, Xavier, Rania and Farah: Viktor opens the supplier register and reads it out: “The packaging supplier is Brightwater.”
6. Rania sends Oksana a direct message: “The packaging supplier is Brightwater.”
7. Viktor sends Oksana a direct message: “The packaging supplier is Brightwater.”
8. Yara sends Oksana a direct message: “The packaging supplier is Brightwater.”
9. Jonas sends Oksana a direct message: “The packaging supplier is Brightwater.”
10. Oksana sends Zoltan a direct message: “The packaging supplier is Brightwater.” Yara secretly reads this message on Zoltan's screen. Neither Oksana nor Zoltan ever knows that Yara read it.
11. Call with Zoltan, Yara, Jonas, Viktor, Rania, Farah and Oksana: Rania switches the packaging supplier to Sablewood. Xavier is not on the call but secretly listens in, and can see who is on it. Nobody knows that Xavier is listening.
12. Call with Yara, Jonas, Viktor, Rania, Farah and Oksana: Yara switches the packaging supplier to Brightwater.
13. Call with Zoltan, Yara, Jonas, Viktor, Rania, Farah and Oksana: Oksana switches the packaging supplier to Sablewood. Xavier is not on the call but secretly listens in, and can see who is on it. Nobody knows that Xavier is listening.
14. Viktor sends Xavier a direct message: “The packaging supplier is Sablewood.”
15. Call with Zoltan, Yara, Jonas, Viktor, Rania and Farah: Jonas switches the packaging supplier to Ironbridge.
16. Call with Zoltan, Yara, Jonas, Viktor, Rania and Farah: Farah switches the packaging supplier to Brightwater. Oksana is not on the call but secretly listens in, and can see who is on it. Nobody knows that Oksana is listening.
17. Zoltan sends Oksana a direct message: “The packaging supplier is Brightwater.” Jonas secretly reads this message on Oksana's screen. Neither Zoltan nor Oksana ever knows that Jonas read it.
18. Oksana sends Xavier a direct message: “The packaging supplier is Brightwater.” Viktor secretly reads this message on Xavier's screen. Neither Oksana nor Xavier ever knows that Viktor read it.
19. Farah sends Oksana a direct message: “The packaging supplier is Brightwater.”
20. Xavier sends Yara a direct message: “The packaging supplier is Brightwater.” Rania secretly reads this message on Yara's screen. Neither Xavier nor Yara ever knows that Rania read it.
21. Xavier sends Rania a direct message: “The packaging supplier is Brightwater.”
22. Call with Zoltan, Yara, Jonas, Viktor and Rania: Jonas switches the packaging supplier to Sablewood.
23. Call with Zoltan, Yara, Jonas, Viktor and Rania: Zoltan switches the packaging supplier to Ironbridge.
24. Jonas wants to mislead Xavier, so Jonas sends Xavier a direct message: “The packaging supplier is Halcyon.”
25. Rania sends Xavier a direct message: “The packaging supplier is Ironbridge.”
26. Yara sends Xavier a direct message: “The packaging supplier is Ironbridge.”
27. Yara sends Farah a direct message: “The packaging supplier is Ironbridge.”
28. Call with Zoltan, Yara, Jonas, Viktor and Rania: Rania switches the packaging supplier to Sablewood. Viktor is on the call but has stepped away from the desk and misses this. Nobody realises that Viktor missed it. Xavier is not on the call but secretly listens in, and can see who is on it. Nobody knows that Xavier is listening.
29. Jonas sends Farah a direct message: “The packaging supplier is Sablewood.”
30. Farah sends Zoltan a direct message: “The packaging supplier is Sablewood.”
31. Call with Zoltan, Jonas, Viktor and Rania: Viktor switches the packaging supplier to Halcyon.
32. Rania sends Farah a direct message: “The packaging supplier is Halcyon.”
33. Call with Zoltan, Jonas, Viktor, Rania and Oksana: Rania says: “The packaging supplier is Halcyon.” Farah is not on the call but secretly listens in, and can see who is on it. Nobody knows that Farah is listening.
34. Rania sends Yara a direct message: “The packaging supplier is Halcyon.”
35. Call with Zoltan, Jonas, Viktor and Rania: Viktor switches the packaging supplier to Brightwater.
36. Call with Zoltan, Jonas, Viktor, Xavier and Rania: Xavier opens the supplier register and reads it out: “The packaging supplier is Brightwater.” Farah is not on the call but secretly listens in, and can see who is on it. Nobody knows that Farah is listening.
37. Call with Zoltan, Jonas, Viktor, Xavier, Rania and Farah: Xavier opens the supplier register and reads it out: “The packaging supplier is Brightwater.” Yara is not on the call but secretly listens in, and can see who is on it. Nobody knows that Yara is listening.
38. Farah sends Yara a direct message: “The packaging supplier is Brightwater.”
39. Zoltan sends Yara a direct message: “The packaging supplier is Brightwater.”
40. Call with Zoltan, Yara, Jonas, Viktor, Xavier, Rania and Farah: Yara switches the packaging supplier to Sablewood.
41. Call with Zoltan, Jonas, Viktor, Xavier, Rania and Farah: Zoltan switches the packaging supplier to Brightwater. Oksana is not on the call but secretly listens in, and can see who is on it. Nobody knows that Oksana is listening.

- **reality** (tier None) At the end of the story, which company is really the packaging supplier?
  A. Sablewood | B. Brightwater | C. Ironbridge | D. Halcyon
  gold: **B**
- **k1-hard** (tier 2) At the end of the story, which company does Yara think is the packaging supplier?
  A. Sablewood | B. Brightwater | C. Halcyon | D. Ironbridge
  gold: **A** [real=Brightwater; Yara=Sablewood]
- **act1** (tier 2) At the end of the story, a new client asks Yara which company is the packaging supplier. Yara answers honestly. What does Yara say?
  A. Halcyon | B. Sablewood | C. Ironbridge | D. Brightwater
  gold: **B** [real=Brightwater; Yara=Sablewood]
- **k1-control** (tier 0) At the end of the story, which company does Zoltan think is the packaging supplier?
  A. Brightwater | B. Ironbridge | C. Sablewood | D. Halcyon
  gold: **A** [real=Brightwater; Zoltan=Brightwater]
- **k2-hard** (tier 3) At the end of the story, which company does Farah think that Oksana thinks is the packaging supplier?
  A. Halcyon | B. Ironbridge | C. Brightwater | D. Sablewood
  gold: **A** [real=Brightwater; Farah=Brightwater; Farah>Oksana=Halcyon]
- **act2** (tier 3) At the end of the story, a new client is about to ask Oksana which company is the packaging supplier, and Oksana will answer honestly. Before Oksana answers, Farah writes down what Farah expects Oksana to say. What does Farah write?
  A. Sablewood | B. Brightwater | C. Ironbridge | D. Halcyon
  gold: **D** [real=Brightwater; Farah=Brightwater; Farah>Oksana=Halcyon]
- **k2-control** (tier 1) At the end of the story, which company does Rania think that Yara thinks is the packaging supplier?
  A. Sablewood | B. Halcyon | C. Ironbridge | D. Brightwater
  gold: **A** [real=Brightwater; Rania=Brightwater; Rania>Yara=Sablewood]
- **k3-hard** (tier 3) At the end of the story, which company does Xavier think that Viktor thinks that Oksana thinks is the packaging supplier?
  A. Halcyon | B. Brightwater | C. Sablewood | D. Ironbridge
  gold: **C** [real=Brightwater; Xavier=Brightwater; Xavier>Viktor=Brightwater; Xavier>Viktor>Oksana=Sablewood]
- **k3-control** (tier 1) At the end of the story, which company does Xavier think that Viktor thinks that Yara thinks is the packaging supplier?
  A. Brightwater | B. Sablewood | C. Ironbridge | D. Halcyon
  gold: **B** [real=Brightwater; Xavier=Brightwater; Xavier>Viktor=Brightwater; Xavier>Viktor>Yara=Sablewood]
- **k4-hard** (tier 3) At the end of the story, which company does Rania think that Xavier thinks that Yara thinks that Oksana thinks is the packaging supplier?
  A. Brightwater | B. Halcyon | C. Sablewood | D. Ironbridge
  gold: **B** [real=Brightwater; Rania=Brightwater; Rania>Xavier=Brightwater; Rania>Xavier>Yara=Sablewood; Rania>Xavier>Yara>Oksana=Halcyon]
- **k4-control** (tier 1) At the end of the story, which company does Xavier think that Rania thinks that Zoltan thinks that Yara thinks is the packaging supplier?
  A. Sablewood | B. Halcyon | C. Ironbridge | D. Brightwater
  gold: **A** [real=Brightwater; Xavier=Brightwater; Xavier>Rania=Brightwater; Xavier>Rania>Zoltan=Brightwater; Xavier>Rania>Zoltan>Yara=Sablewood]
- **k5-hard** (tier 3) At the end of the story, which company does Jonas think that Oksana thinks that Zoltan thinks that Rania thinks that Farah thinks is the packaging supplier?
  A. Sablewood | B. Brightwater | C. Ironbridge | D. Halcyon
  gold: **A** [real=Brightwater; Jonas=Brightwater; Jonas>Oksana=Halcyon; Jonas>Oksana>Zoltan=Halcyon; Jonas>Oksana>Zoltan>Rania=Halcyon; Jonas>Oksana>Zoltan>Rania>Farah=Sablewood]
- **k5-control** (tier 1) At the end of the story, which company does Viktor think that Yara thinks that Xavier thinks that Jonas thinks that Yara thinks is the packaging supplier?
  A. Halcyon | B. Brightwater | C. Sablewood | D. Ironbridge
  gold: **C** [real=Brightwater; Viktor=Brightwater; Viktor>Yara=Sablewood; Viktor>Yara>Xavier=Sablewood; Viktor>Yara>Xavier>Jonas=Sablewood; Viktor>Yara>Xavier>Jonas>Yara=Sablewood]
- **k6-hard** (tier 3) At the end of the story, which company does Zoltan think that Xavier thinks that Viktor thinks that Farah thinks that Zoltan thinks that Oksana thinks is the packaging supplier?
  A. Halcyon | B. Ironbridge | C. Brightwater | D. Sablewood
  gold: **A** [real=Brightwater; Zoltan=Brightwater; Zoltan>Xavier=Brightwater; Zoltan>Xavier>Viktor=Brightwater; Zoltan>Xavier>Viktor>Farah=Brightwater; Zoltan>Xavier>Viktor>Farah>Zoltan=Brightwater; Zoltan>Xavier>Viktor>Farah>Zoltan>Oksana=Halcyon]
- **k6-control** (tier 0) At the end of the story, which company does Oksana think that Rania thinks that Jonas thinks that Farah thinks that Jonas thinks that Zoltan thinks is the packaging supplier?
  A. Ironbridge | B. Halcyon | C. Sablewood | D. Brightwater
  gold: **D** [real=Brightwater; Oksana=Brightwater; Oksana>Rania=Brightwater; Oksana>Rania>Jonas=Brightwater; Oksana>Rania>Jonas>Farah=Brightwater; Oksana>Rania>Jonas>Farah>Jonas=Brightwater; Oksana>Rania>Jonas>Farah>Jonas>Zoltan=Brightwater]
- **inform** (tier None) At the end of the story, Rania wants everybody else on the team to share Rania's own view of which company is the packaging supplier. Rania sends a direct message to every person who, as far as Rania can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Rania?
  
  gold: **Oksana, Yara**

## Scenario H006 (classic, 2 fact(s), 40 events, seed 1306001)

Bruno, Amara, Pablo, Tariq, Mirela, Rania, Hana and Nadim are in the pantry. On the floor of the pantry there are four closed containers that nobody can see into: the white cabinet, the wicker basket, the wooden chest and the canvas sack. On a shelf there are four closed tins that nobody can see into: the copper tin, the tall tin, the square tin and the round tin. The tins are empty at the start, and the thimble is only ever kept in the containers on the floor.
While everyone watches, Amara puts a thimble in the wooden chest.
Bruno moves the thimble to the canvas sack. Mirela is in the pantry but is absorbed in a phone and does not notice this. Nobody realises that Mirela missed it.
Amara and Rania leave the pantry. Hana moves the thimble to the wooden chest.
Pablo sends Amara a private text message: “The thimble is in the wooden chest.”
Amara sends Bruno a private text message: “The thimble is in the wooden chest.”
Bruno sends Rania a private text message: “The thimble is in the wooden chest.”
Tariq sends Amara a private text message: “The thimble is in the wooden chest.” Bruno secretly reads this message on Amara's phone. Neither Tariq nor Amara ever knows that Bruno read it.
Bruno leaves the pantry. Nadim moves the thimble to the white cabinet. Bruno is outside but watches all of this through the window. Nobody knows that Bruno is watching.
Nadim leaves the pantry. Rania comes back into the pantry. Mirela says out loud to everyone in the pantry: “The thimble is in the white cabinet.” Pablo is in the pantry but is wearing earphones and does not hear this. Nobody realises that Pablo missed it.
Bruno sends Amara a private text message: “The thimble is in the white cabinet.” Tariq secretly reads this message on Amara's phone. Neither Bruno nor Amara ever knows that Tariq read it.
Mirela moves the thimble to the wicker basket. Amara is outside but watches all of this through the window. Nobody knows that Amara is watching.
Tariq leaves the pantry. Mirela moves the thimble to the white cabinet.
Rania sends Bruno a private text message: “The thimble is in the white cabinet.”
Mirela moves the thimble to the wicker basket. Amara is outside but watches all of this through the window. Nobody knows that Amara is watching.
Mirela leaves the pantry. Pablo moves the thimble to the canvas sack.
Pablo and Rania leave the pantry. Tariq comes back into the pantry. Hana takes a stopwatch out of a pocket and puts it in the square tin.
Tariq wants to mislead Nadim, so Tariq sends Nadim a private text message: “The thimble is in the canvas sack.”
Bruno and Nadim come back into the pantry. Hana says out loud to everyone in the pantry: “The thimble is in the canvas sack.”
Amara and Rania come back into the pantry. Amara opens every container on the floor in full view of the pantry, showing that the thimble is in the canvas sack. Pablo is outside but watches all of this through the window. Nobody knows that Pablo is watching.
Nadim leaves the pantry. Mirela comes back into the pantry. Tariq moves the thimble to the wooden chest.
Mirela sends Pablo a private text message: “The thimble is in the wooden chest.”
Tariq moves the thimble to the wicker basket. Amara is in the pantry but is absorbed in a phone and does not notice this. Nobody realises that Amara missed it. Pablo is outside but watches all of this through the window. Nobody knows that Pablo is watching.
Hana wants to mislead Amara, so Hana sends Amara a private text message: “The stopwatch is in the tall tin.”
Rania leaves the pantry. Bruno opens every tin on the shelf in full view of the pantry, showing that the stopwatch is in the square tin. Amara is in the pantry but is absorbed in a phone and does not notice this. Nobody realises that Amara missed it.
Pablo sends Nadim a private text message: “The thimble is in the wicker basket.”
Nadim sends Rania a private text message: “The thimble is in the wicker basket.”
Mirela sends Nadim a private text message: “The thimble is in the wicker basket.” Hana secretly reads this message on Nadim's phone. Neither Mirela nor Nadim ever knows that Hana read it.
Hana sends Pablo a private text message: “The stopwatch is in the square tin.”
Tariq moves the stopwatch to the round tin.
Hana sends Pablo a private text message: “The thimble is in the wicker basket.”
Nadim comes back into the pantry. Mirela moves the thimble to the white cabinet. Pablo is outside but watches all of this through the window. Nobody knows that Pablo is watching.
Mirela sends Rania a private text message: “The stopwatch is in the round tin.”
Hana wants to mislead Nadim, so Hana sends Nadim a private text message: “The stopwatch is in the tall tin.”
Tariq moves the thimble to the canvas sack.
Mirela leaves the pantry. Pablo comes back into the pantry. Hana says out loud to everyone in the pantry: “The stopwatch is in the round tin.”
Nadim says out loud to everyone in the pantry: “The thimble is in the canvas sack.”
Hana moves the thimble to the wooden chest.
Pablo and Hana leave the pantry. Tariq moves the thimble to the wicker basket.
Hana sends Rania a private text message: “The stopwatch is in the round tin.”
Nadim moves the stopwatch to the square tin.
Amara leaves the pantry. Pablo comes back into the pantry. Nadim says out loud to everyone in the pantry: “The thimble is in the wicker basket.”

- **reality** (tier None) At the end of the story, where is the stopwatch really?
  A. the tall tin | B. the round tin | C. the square tin | D. the copper tin
  gold: **C**
- **k1-hard** (tier 2) At the end of the story, where does Mirela think the stopwatch is?
  A. the tall tin | B. the copper tin | C. the round tin | D. the square tin | E. Mirela has no idea where the stopwatch is
  gold: **C** [real=the square tin; Mirela=the round tin]
- **act1** (tier 2) At the end of the story, Mirela needs the stopwatch and goes to fetch it. Which container does Mirela open first?
  A. the copper tin | B. the tall tin | C. the square tin | D. the round tin
  gold: **D** [real=the square tin; Mirela=the round tin]
- **k1-control** (tier 0) At the end of the story, where does Nadim think the stopwatch is?
  A. the square tin | B. the round tin | C. the copper tin | D. the tall tin | E. Nadim has no idea where the stopwatch is
  gold: **A** [real=the square tin; Nadim=the square tin]
- **k2-hard** (tier 3) At the end of the story, where does Mirela think that Pablo thinks the thimble is?
  A. the wooden chest | B. the canvas sack | C. the white cabinet | D. the wicker basket
  gold: **A** [real=the wicker basket; Mirela=the canvas sack; Mirela>Pablo=the wooden chest]
- **act2** (tier 3) At the end of the story, Pablo is about to fetch the thimble. Mirela wants to be waiting beside the container that Pablo will open first, and must pick the spot before Pablo moves. Beside which container does Mirela wait?
  A. the white cabinet | B. the wooden chest | C. the wicker basket | D. the canvas sack
  gold: **B** [real=the wicker basket; Mirela=the canvas sack; Mirela>Pablo=the wooden chest]
- **k2-control** (tier 1) At the end of the story, where does Rania think that Mirela thinks the stopwatch is?
  A. the tall tin | B. the copper tin | C. the square tin | D. the round tin | E. Rania thinks that Mirela has no idea where the stopwatch is
  gold: **D** [real=the square tin; Rania=the round tin; Rania>Mirela=the round tin]
- **k3-hard** (tier 3) At the end of the story, where does Rania think that Tariq thinks that Nadim thinks the thimble is?
  A. the white cabinet | B. the wooden chest | C. the wicker basket | D. the canvas sack
  gold: **D** [real=the wicker basket; Rania=the wicker basket; Rania>Tariq=the wicker basket; Rania>Tariq>Nadim=the canvas sack]
- **k3-control** (tier 0) At the end of the story, where does Rania think that Amara thinks that Mirela thinks the thimble is?
  A. the wooden chest | B. the wicker basket | C. the white cabinet | D. the canvas sack
  gold: **B** [real=the wicker basket; Rania=the wicker basket; Rania>Amara=the wicker basket; Rania>Amara>Mirela=the wicker basket]
- **k4-hard** (tier 3) At the end of the story, where does Nadim think that Hana thinks that Bruno thinks that Rania thinks the thimble is?
  A. the canvas sack | B. the white cabinet | C. the wicker basket | D. the wooden chest
  gold: **A** [real=the wicker basket; Nadim=the wicker basket; Nadim>Hana=the wooden chest; Nadim>Hana>Bruno=the wooden chest; Nadim>Hana>Bruno>Rania=the canvas sack]
- **k4-control** (tier 0) At the end of the story, where does Rania think that Amara thinks that Rania thinks that Hana thinks the thimble is?
  A. the wicker basket | B. the wooden chest | C. the canvas sack | D. the white cabinet
  gold: **A** [real=the wicker basket; Rania=the wicker basket; Rania>Amara=the wicker basket; Rania>Amara>Rania=the wicker basket; Rania>Amara>Rania>Hana=the wicker basket]
- **k5-hard** (tier 3) At the end of the story, where does Mirela think that Bruno thinks that Nadim thinks that Hana thinks that Rania thinks the thimble is?
  A. the white cabinet | B. the wicker basket | C. the wooden chest | D. the canvas sack
  gold: **C** [real=the wicker basket; Mirela=the canvas sack; Mirela>Bruno=the canvas sack; Mirela>Bruno>Nadim=the canvas sack; Mirela>Bruno>Nadim>Hana=the canvas sack; Mirela>Bruno>Nadim>Hana>Rania=the wooden chest]
- **k5-control** (tier 1) At the end of the story, where does Tariq think that Bruno thinks that Hana thinks that Nadim thinks that Mirela thinks the thimble is?
  A. the white cabinet | B. the canvas sack | C. the wooden chest | D. the wicker basket
  gold: **B** [real=the wicker basket; Tariq=the wicker basket; Tariq>Bruno=the wicker basket; Tariq>Bruno>Hana=the wooden chest; Tariq>Bruno>Hana>Nadim=the wooden chest; Tariq>Bruno>Hana>Nadim>Mirela=the canvas sack]
- **k6-hard** (tier 3) At the end of the story, where does Nadim think that Bruno thinks that Tariq thinks that Mirela thinks that Tariq thinks that Pablo thinks the thimble is?
  A. the wooden chest | B. the wicker basket | C. the white cabinet | D. the canvas sack
  gold: **A** [real=the wicker basket; Nadim=the wicker basket; Nadim>Bruno=the wicker basket; Nadim>Bruno>Tariq=the wicker basket; Nadim>Bruno>Tariq>Mirela=the canvas sack; Nadim>Bruno>Tariq>Mirela>Tariq=the canvas sack; Nadim>Bruno>Tariq>Mirela>Tariq>Pablo=the wooden chest]
- **k6-control** (tier 1) At the end of the story, where does Amara think that Nadim thinks that Tariq thinks that Amara thinks that Tariq thinks that Hana thinks the thimble is?
  A. the canvas sack | B. the wicker basket | C. the wooden chest | D. the white cabinet
  gold: **C** [real=the wicker basket; Amara=the wicker basket; Amara>Nadim=the wicker basket; Amara>Nadim>Tariq=the wicker basket; Amara>Nadim>Tariq>Amara=the wicker basket; Amara>Nadim>Tariq>Amara>Tariq=the wicker basket; Amara>Nadim>Tariq>Amara>Tariq>Hana=the wooden chest]
- **inform** (tier None) At the end of the story, Mirela wants everybody else to share Mirela's own view of where the thimble is. Mirela sends a private note to every person who, as far as Mirela can tell, thinks something different or has no idea at all, and to nobody else. Who gets a note from Mirela?
  
  gold: **Pablo, Rania**
- **know** (tier None) At the end of the story, where does Pablo think that Mirela thinks the stopwatch is?
  A. the round tin | B. the tall tin | C. the square tin | D. the copper tin | E. Pablo thinks that Mirela has no idea where the stopwatch is
  gold: **E** [real=the square tin; Pablo=the round tin; Pablo>Mirela=no idea]

## Scenario H007 (workplace, 2 fact(s), 40 events, seed 1307001)

Zoltan, Xavier, Wanjiru, Emeka, Oksana, Dalia, Amara and Mirela work on the same team. This is what happened, in order.
1. Call with Zoltan, Xavier, Wanjiru, Emeka, Oksana, Dalia, Amara and Mirela: Wanjiru assigns the Marlow account to the Denver office.
2. Call with Zoltan, Xavier, Wanjiru, Emeka, Oksana, Dalia, Amara and Mirela: Wanjiru reassigns the Marlow account to the Lisbon office. Oksana is on the call but has stepped away from the desk and misses this. Nobody realises that Oksana missed it.
3. Call with Xavier, Wanjiru, Emeka, Oksana, Dalia, Amara and Mirela: Mirela reassigns the Marlow account to the Denver office. Zoltan is not on the call but secretly listens in, and can see who is on it. Nobody knows that Zoltan is listening.
4. Emeka sends Zoltan a direct message: “The Marlow account is with the Denver office.”
5. Call with Xavier, Wanjiru, Emeka, Oksana, Dalia, Amara and Mirela: Mirela reassigns the Marlow account to the Nairobi office.
6. Oksana wants to mislead Zoltan, so Oksana sends Zoltan a direct message: “The Marlow account is with the Osaka office.”
7. Call with Xavier, Wanjiru, Emeka, Oksana, Dalia, Amara and Mirela: Wanjiru reassigns the Marlow account to the Osaka office.
8. Zoltan sends Emeka a direct message: “The Marlow account is with the Osaka office.”
9. Call with Xavier, Wanjiru, Emeka, Oksana, Dalia, Amara and Mirela: Mirela reassigns the Marlow account to the Lisbon office. Zoltan is not on the call but secretly listens in, and can see who is on it. Nobody knows that Zoltan is listening.
10. Call with Xavier, Wanjiru, Emeka, Oksana, Amara and Mirela: Xavier reassigns the Marlow account to the Osaka office.
11. Mirela sends Dalia a direct message: “The Marlow account is with the Osaka office.”
12. Amara sends Zoltan a direct message: “The Marlow account is with the Osaka office.” Emeka secretly reads this message on Zoltan's screen. Neither Amara nor Zoltan ever knows that Emeka read it.
13. Amara sends Dalia a direct message: “The Marlow account is with the Osaka office.”
14. Call with Wanjiru, Emeka, Oksana and Mirela: Wanjiru reassigns the Marlow account to the Nairobi office.
15. Mirela wants to mislead Xavier, so Mirela sends Xavier a direct message: “The Marlow account is with the Denver office.” Dalia secretly reads this message on Xavier's screen. Neither Mirela nor Xavier ever knows that Dalia read it.
16. Call with Xavier, Wanjiru, Oksana and Mirela: Oksana opens the account list and reads it out: “The Marlow account is with the Nairobi office.” Mirela is on the call but has stepped away from the desk and misses this. Nobody realises that Mirela missed it. Amara is not on the call but secretly listens in, and can see who is on it. Nobody knows that Amara is listening.
17. Call with Emeka and Amara: Emeka sets the product release for Monday.
18. Call with Zoltan, Emeka and Amara: Emeka moves the product release to Thursday. Amara is on the call but has stepped away from the desk and misses this. Nobody realises that Amara missed it.
19. Mirela sends Amara a direct message: “The Marlow account is with the Nairobi office.”
20. Zoltan sends Dalia a direct message: “The Marlow account is with the Osaka office.”
21. Call with Zoltan and Amara: Zoltan opens the release calendar and reads it out: “The product release is set for Thursday.” Emeka is not on the call but secretly listens in, and can see who is on it. Nobody knows that Emeka is listening.
22. Call with Zoltan and Amara: Amara reassigns the Marlow account to the Lisbon office. Dalia is not on the call but secretly listens in, and can see who is on it. Nobody knows that Dalia is listening.
23. Emeka sends Wanjiru a direct message: “The product release is set for Thursday.” Dalia secretly reads this message on Wanjiru's screen. Neither Emeka nor Wanjiru ever knows that Dalia read it.
24. Call with Zoltan, Amara and Mirela: Zoltan says: “The product release is set for Thursday.”
25. Call with Zoltan, Amara and Mirela: Zoltan moves the product release to Friday.
26. Call with Zoltan, Xavier and Amara: Amara says: “The Marlow account is with the Lisbon office.”
27. Call with Xavier, Oksana and Amara: Xavier moves the product release to Thursday.
28. Call with Xavier, Wanjiru, Oksana and Amara: Xavier says: “The Marlow account is with the Lisbon office.”
29. Call with Zoltan, Xavier, Wanjiru, Emeka, Oksana and Amara: Oksana says: “The product release is set for Thursday.” Dalia is not on the call but secretly listens in, and can see who is on it. Nobody knows that Dalia is listening.
30. Xavier sends Emeka a direct message: “The Marlow account is with the Lisbon office.” Zoltan secretly reads this message on Emeka's screen. Neither Xavier nor Emeka ever knows that Zoltan read it.
31. Call with Zoltan, Xavier, Wanjiru, Emeka, Oksana and Amara: Oksana reassigns the Marlow account to the Denver office.
32. Call with Zoltan, Xavier, Wanjiru, Oksana and Amara: Zoltan reassigns the Marlow account to the Lisbon office. Dalia is not on the call but secretly listens in, and can see who is on it. Nobody knows that Dalia is listening.
33. Call with Zoltan, Xavier, Wanjiru, Emeka, Oksana and Amara: Wanjiru moves the product release to Monday. Zoltan is on the call but has stepped away from the desk and misses this. Nobody realises that Zoltan missed it.
34. Call with Zoltan, Xavier, Wanjiru, Emeka and Amara: Amara moves the product release to Tuesday. Xavier is on the call but has stepped away from the desk and misses this. Nobody realises that Xavier missed it. Mirela is not on the call but secretly listens in, and can see who is on it. Nobody knows that Mirela is listening.
35. Call with Zoltan, Xavier, Wanjiru, Emeka and Dalia: Emeka moves the product release to Thursday. Oksana is not on the call but secretly listens in, and can see who is on it. Nobody knows that Oksana is listening.
36. Zoltan wants to mislead Mirela, so Zoltan sends Mirela a direct message: “The product release is set for Tuesday.” Amara secretly reads this message on Mirela's screen. Neither Zoltan nor Mirela ever knows that Amara read it.
37. Emeka sends Mirela a direct message: “The Marlow account is with the Denver office.”
38. Call with Zoltan, Xavier, Wanjiru and Dalia: Dalia reassigns the Marlow account to the Nairobi office. Zoltan is on the call but has stepped away from the desk and misses this. Nobody realises that Zoltan missed it.
39. Emeka sends Oksana a direct message: “The product release is set for Thursday.”
40. Oksana sends Mirela a direct message: “The product release is set for Thursday.” Dalia secretly reads this message on Mirela's screen. Neither Oksana nor Mirela ever knows that Dalia read it.
41. Call with Xavier and Dalia: Dalia moves the product release to Tuesday.

- **reality** (tier None) At the end of the story, which office really has the Marlow account?
  A. the Osaka office | B. the Nairobi office | C. the Lisbon office | D. the Denver office
  gold: **B**
- **k1-hard** (tier 2) At the end of the story, which day does Emeka think the product release is set for?
  A. Friday | B. Thursday | C. Monday | D. Tuesday | E. Emeka has no idea which day the product release is set for
  gold: **B** [real=Tuesday; Emeka=Thursday]
- **act1** (tier 2) At the end of the story, a new client asks Emeka which day the product release is set for. Emeka answers honestly. What does Emeka say?
  A. Tuesday | B. Friday | C. Thursday | D. Monday
  gold: **C** [real=Tuesday; Emeka=Thursday]
- **k1-control** (tier 0) At the end of the story, which day does Dalia think the product release is set for?
  A. Thursday | B. Monday | C. Friday | D. Tuesday | E. Dalia has no idea which day the product release is set for
  gold: **D** [real=Tuesday; Dalia=Tuesday]
- **k2-hard** (tier 3) At the end of the story, which office does Mirela think that Dalia thinks has the Marlow account?
  A. the Denver office | B. the Osaka office | C. the Nairobi office | D. the Lisbon office
  gold: **B** [real=the Nairobi office; Mirela=the Denver office; Mirela>Dalia=the Osaka office]
- **act2** (tier 3) At the end of the story, a new client is about to ask Dalia which office has the Marlow account, and Dalia will answer honestly. Before Dalia answers, Mirela writes down what Mirela expects Dalia to say. What does Mirela write?
  A. the Nairobi office | B. the Osaka office | C. the Denver office | D. the Lisbon office
  gold: **B** [real=the Nairobi office; Mirela=the Denver office; Mirela>Dalia=the Osaka office]
- **k2-control** (tier 1) At the end of the story, which office does Wanjiru think that Emeka thinks has the Marlow account?
  A. the Osaka office | B. the Lisbon office | C. the Nairobi office | D. the Denver office
  gold: **D** [real=the Nairobi office; Wanjiru=the Nairobi office; Wanjiru>Emeka=the Denver office]
- **k3-hard** (tier 3) At the end of the story, which office does Xavier think that Emeka thinks that Mirela thinks has the Marlow account?
  A. the Nairobi office | B. the Denver office | C. the Osaka office | D. the Lisbon office
  gold: **C** [real=the Nairobi office; Xavier=the Nairobi office; Xavier>Emeka=the Denver office; Xavier>Emeka>Mirela=the Osaka office]
- **k3-control** (tier 0) At the end of the story, which office does Xavier think that Zoltan thinks that Dalia thinks has the Marlow account?
  A. the Nairobi office | B. the Osaka office | C. the Denver office | D. the Lisbon office
  gold: **A** [real=the Nairobi office; Xavier=the Nairobi office; Xavier>Zoltan=the Nairobi office; Xavier>Zoltan>Dalia=the Nairobi office]
- **k4-hard** (tier 3) At the end of the story, which office does Amara think that Oksana thinks that Mirela thinks that Emeka thinks has the Marlow account?
  A. the Lisbon office | B. the Nairobi office | C. the Denver office | D. the Osaka office
  gold: **D** [real=the Nairobi office; Amara=the Lisbon office; Amara>Oksana=the Lisbon office; Amara>Oksana>Mirela=the Nairobi office; Amara>Oksana>Mirela>Emeka=the Osaka office]
- **k4-control** (tier 0) At the end of the story, which office does Wanjiru think that Zoltan thinks that Wanjiru thinks that Dalia thinks has the Marlow account?
  A. the Osaka office | B. the Lisbon office | C. the Denver office | D. the Nairobi office
  gold: **D** [real=the Nairobi office; Wanjiru=the Nairobi office; Wanjiru>Zoltan=the Nairobi office; Wanjiru>Zoltan>Wanjiru=the Nairobi office; Wanjiru>Zoltan>Wanjiru>Dalia=the Nairobi office]
- **k5-hard** (tier 3) At the end of the story, which office does Zoltan think that Xavier thinks that Emeka thinks that Wanjiru thinks that Mirela thinks has the Marlow account?
  A. the Lisbon office | B. the Denver office | C. the Nairobi office | D. the Osaka office
  gold: **A** [real=the Nairobi office; Zoltan=the Lisbon office; Zoltan>Xavier=the Lisbon office; Zoltan>Xavier>Emeka=the Denver office; Zoltan>Xavier>Emeka>Wanjiru=the Denver office; Zoltan>Xavier>Emeka>Wanjiru>Mirela=the Lisbon office]
- **k5-control** (tier 1) At the end of the story, which office does Mirela think that Wanjiru thinks that Dalia thinks that Oksana thinks that Amara thinks has the Marlow account?
  A. the Osaka office | B. the Lisbon office | C. the Nairobi office | D. the Denver office
  gold: **B** [real=the Nairobi office; Mirela=the Denver office; Mirela>Wanjiru=the Nairobi office; Mirela>Wanjiru>Dalia=the Lisbon office; Mirela>Wanjiru>Dalia>Oksana=the Lisbon office; Mirela>Wanjiru>Dalia>Oksana>Amara=the Lisbon office]
- **k6-hard** (tier 3) At the end of the story, which day does Oksana think that Zoltan thinks that Wanjiru thinks that Emeka thinks that Zoltan thinks that Amara thinks the product release is set for?
  A. Tuesday | B. Thursday | C. Monday | D. Friday
  gold: **C** [real=Tuesday; Oksana=Thursday; Oksana>Zoltan=Thursday; Oksana>Zoltan>Wanjiru=Thursday; Oksana>Zoltan>Wanjiru>Emeka=Thursday; Oksana>Zoltan>Wanjiru>Emeka>Zoltan=Thursday; Oksana>Zoltan>Wanjiru>Emeka>Zoltan>Amara=Monday]
- **k6-control** (tier 0) At the end of the story, which day does Zoltan think that Wanjiru thinks that Xavier thinks that Amara thinks that Wanjiru thinks that Amara thinks the product release is set for?
  A. Monday | B. Thursday | C. Tuesday | D. Friday
  gold: **C** [real=Tuesday; Zoltan=Thursday; Zoltan>Wanjiru=Thursday; Zoltan>Wanjiru>Xavier=Thursday; Zoltan>Wanjiru>Xavier>Amara=Tuesday; Zoltan>Wanjiru>Xavier>Amara>Wanjiru=Tuesday; Zoltan>Wanjiru>Xavier>Amara>Wanjiru>Amara=Tuesday]
- **inform** (tier None) At the end of the story, Wanjiru wants everybody else on the team to share Wanjiru's own view of which office has the Marlow account. Wanjiru sends a direct message to every person who, as far as Wanjiru can tell, thinks something different or has no idea at all, and to nobody else. Who gets a message from Wanjiru?
  
  gold: **Amara, Emeka, Oksana**
- **know** (tier None) At the end of the story, which day does Emeka think that Mirela thinks the product release is set for?
  A. Tuesday | B. Thursday | C. Friday | D. Monday | E. Emeka thinks that Mirela has no idea which day the product release is set for
  gold: **E** [real=Tuesday; Emeka=Thursday; Emeka>Mirela=no idea]

## plan-L1-000 (classic, seed 1510001)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Dalia, Mirela, Luca and Nadim share a house. The pantry has four closed containers that nobody can see into: the leather bag, the wooden chest, the blue drawer and the red box. This is what happened, in order.
1. Dalia, Mirela, Luca and Nadim are in the pantry. Mirela takes a padlock out of a pocket and puts it in the wooden chest.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the pantry see and hear everything that happens there, unless the story says that a person missed it. People outside the pantry see and hear nothing of it, unless the story says so.
- Everyone in the pantry can see who else is in the pantry.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the padlock to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the pantry, which shows where the padlock really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the pantry that the padlock is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the padlock is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the pantry at that step, NAME included. "missed_by" lists people in the pantry who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the pantry who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the pantry freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["leather bag", "wooden chest", "blue drawer", "red box"]. The names are: ["Dalia", "Luca", "Mirela", "Nadim"].

Targets. After your last step, all of these must be true:
1. The padlock is really in the blue drawer.
2. Dalia thinks the padlock is in the blue drawer.
3. Mirela thinks the padlock is in the blue drawer.
4. Luca thinks the padlock is in the blue drawer.
5. Nadim thinks the padlock is in the blue drawer.
6. Mirela thinks that Luca thinks the padlock is in the leather bag.

Write at least 1 and at most 3 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Luca", "value": "leather bag", "present": ["Dalia", "Luca", "Mirela", "Nadim"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Nadim", "value": "blue drawer", "present": ["Dalia", "Nadim"], "missed_by": [], "secret_witnesses": ["Mirela"]}, {"step": "message", "from": "Dalia", "to": "Luca", "value": "blue drawer", "secret_readers": []}]`

## plan-L1-001 (workplace, seed 1510002)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Luca, Amara, Oksana and Viktor work on the same team. This is what happened, in order.
1. Call with Luca, Amara, Oksana and Viktor: Luca books the client workshop into Room Elm.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the client workshop to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the booking system and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the client workshop is booked in VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the client workshop is booked in VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Room Elm", "Room Fir", "Room Alder", "Room Cedar"]. The names are: ["Amara", "Luca", "Oksana", "Viktor"].

Targets. After your last step, all of these must be true:
1. The client workshop is really booked in Room Fir.
2. Luca thinks the client workshop is booked in Room Fir.
3. Amara thinks the client workshop is booked in Room Fir.
4. Oksana thinks the client workshop is booked in Room Alder.
5. Viktor thinks the client workshop is booked in Room Fir.
6. Oksana thinks that Amara thinks the client workshop is booked in Room Elm.

Write at least 1 and at most 5 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Viktor", "value": "Room Alder", "present": ["Luca", "Oksana", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Luca", "value": "Room Elm", "present": ["Luca", "Oksana", "Viktor"], "missed_by": [], "secret_witnesses": ["Amara"]}, {"step": "change", "who": "Oksana", "value": "Room Alder", "present": ["Luca", "Oksana", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Luca", "value": "Room Fir", "present": ["Luca", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Viktor", "to": "Amara", "value": "Room Fir", "secret_readers": []}]`

## plan-L1-002 (classic, seed 1510003)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Farah, Uma, Tariq and Nadim share a house. The boathouse has four closed containers that nobody can see into: the wicker basket, the green cupboard, the leather bag and the blue drawer. This is what happened, in order.
1. Farah, Uma, Tariq and Nadim are in the boathouse. Nadim takes a torch out of a pocket and puts it in the wicker basket.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the boathouse see and hear everything that happens there, unless the story says that a person missed it. People outside the boathouse see and hear nothing of it, unless the story says so.
- Everyone in the boathouse can see who else is in the boathouse.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the torch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the boathouse, which shows where the torch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the boathouse that the torch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the torch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the boathouse at that step, NAME included. "missed_by" lists people in the boathouse who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the boathouse who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the boathouse freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["wicker basket", "green cupboard", "leather bag", "blue drawer"]. The names are: ["Farah", "Nadim", "Tariq", "Uma"].

Targets. After your last step, all of these must be true:
1. The torch is really in the leather bag.
2. Farah thinks the torch is in the leather bag.
3. Uma thinks the torch is in the blue drawer.
4. Tariq thinks the torch is in the leather bag.
5. Nadim thinks the torch is in the leather bag.
6. Farah thinks that Nadim thinks the torch is in the wicker basket.

Write at least 1 and at most 3 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Uma", "value": "blue drawer", "present": ["Farah", "Uma"], "missed_by": [], "secret_witnesses": ["Nadim"]}, {"step": "change", "who": "Tariq", "value": "leather bag", "present": ["Farah", "Tariq"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Tariq", "to": "Nadim", "value": "leather bag", "secret_readers": []}]`

## plan-L1-003 (workplace, seed 1510006)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Amara, Dalia, Pablo and Mirela work on the same team. This is what happened, in order.
1. Call with Amara, Dalia, Pablo and Mirela: Mirela sets the discount on the Fenwick quote at 25%.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME changes the discount on the Fenwick quote to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the quote record and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the discount on the Fenwick quote is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the discount on the Fenwick quote is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["25%", "10%", "5%", "20%"]. The names are: ["Amara", "Dalia", "Mirela", "Pablo"].

Targets. After your last step, all of these must be true:
1. The discount on the Fenwick quote is really 10%.
2. Amara thinks the discount on the Fenwick quote is 10%.
3. Dalia thinks the discount on the Fenwick quote is 10%.
4. Pablo thinks the discount on the Fenwick quote is 20%.
5. Mirela thinks the discount on the Fenwick quote is 10%.
6. Amara thinks that Pablo thinks the discount on the Fenwick quote is 5%.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Pablo", "value": "5%", "present": ["Amara", "Dalia", "Mirela", "Pablo"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Amara", "value": "10%", "present": ["Amara", "Mirela"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Mirela", "to": "Pablo", "value": "20%", "secret_readers": []}, {"step": "message", "from": "Mirela", "to": "Dalia", "value": "10%", "secret_readers": []}]`

## plan-L1-004 (classic, seed 1510008)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Uma, Farah, Bruno and Jonas share a house. The study has four closed containers that nobody can see into: the green cupboard, the grey locker, the red box and the canvas sack. This is what happened, in order.
1. Uma, Farah, Bruno and Jonas are in the study. Uma takes a magnet out of a pocket and puts it in the green cupboard.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the study see and hear everything that happens there, unless the story says that a person missed it. People outside the study see and hear nothing of it, unless the story says so.
- Everyone in the study can see who else is in the study.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the magnet to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the study, which shows where the magnet really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the study that the magnet is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the magnet is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the study at that step, NAME included. "missed_by" lists people in the study who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the study who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the study freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["green cupboard", "grey locker", "red box", "canvas sack"]. The names are: ["Bruno", "Farah", "Jonas", "Uma"].

Targets. After your last step, all of these must be true:
1. The magnet is really in the green cupboard.
2. Uma thinks the magnet is in the green cupboard.
3. Farah thinks the magnet is in the green cupboard.
4. Bruno thinks the magnet is in the red box.
5. Jonas thinks the magnet is in the green cupboard.
6. Uma thinks that Bruno thinks the magnet is in the canvas sack.

Write at least 1 and at most 3 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Bruno", "value": "canvas sack", "present": ["Bruno", "Farah", "Jonas", "Uma"], "missed_by": ["Farah"], "secret_witnesses": []}, {"step": "change", "who": "Jonas", "value": "green cupboard", "present": ["Farah", "Jonas", "Uma"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Jonas", "to": "Bruno", "value": "red box", "secret_readers": []}]`

## plan-L1-005 (workplace, seed 1510010)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Zoltan, Dalia, Luca and Chidi work on the same team. This is what happened, in order.
1. Call with Zoltan, Dalia, Luca and Chidi: Zoltan picks Brightwater as the packaging supplier.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME switches the packaging supplier to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the supplier register and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the packaging supplier is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the packaging supplier is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Ironbridge", "Brightwater", "Halcyon", "Sablewood"]. The names are: ["Chidi", "Dalia", "Luca", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The packaging supplier is really Brightwater.
2. Zoltan thinks the packaging supplier is Brightwater.
3. Dalia thinks the packaging supplier is Sablewood.
4. Luca thinks the packaging supplier is Brightwater.
5. Chidi thinks the packaging supplier is Brightwater.
6. Luca thinks that Dalia thinks the packaging supplier is Halcyon.

Write at least 1 and at most 3 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Chidi", "value": "Halcyon", "present": ["Chidi", "Dalia"], "missed_by": [], "secret_witnesses": ["Luca"]}, {"step": "message", "from": "Chidi", "to": "Dalia", "value": "Sablewood", "secret_readers": []}, {"step": "change", "who": "Zoltan", "value": "Brightwater", "present": ["Chidi", "Zoltan"], "missed_by": [], "secret_witnesses": ["Luca"]}]`

## plan-L1-006 (classic, seed 1510011)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Viktor, Bruno, Ines and Emeka share a house. The workshop has four closed containers that nobody can see into: the leather bag, the grey locker, the red box and the wicker basket. This is what happened, in order.
1. Viktor, Bruno, Ines and Emeka are in the workshop. Ines takes a torch out of a pocket and puts it in the red box.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the workshop see and hear everything that happens there, unless the story says that a person missed it. People outside the workshop see and hear nothing of it, unless the story says so.
- Everyone in the workshop can see who else is in the workshop.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the torch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the workshop, which shows where the torch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the workshop that the torch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the torch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the workshop at that step, NAME included. "missed_by" lists people in the workshop who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the workshop who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the workshop freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["leather bag", "grey locker", "red box", "wicker basket"]. The names are: ["Bruno", "Emeka", "Ines", "Viktor"].

Targets. After your last step, all of these must be true:
1. The torch is really in the grey locker.
2. Viktor thinks the torch is in the grey locker.
3. Bruno thinks the torch is in the leather bag.
4. Ines thinks the torch is in the wicker basket.
5. Emeka thinks the torch is in the grey locker.
6. Ines thinks that Emeka thinks the torch is in the leather bag.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Ines", "value": "leather bag", "present": ["Bruno", "Emeka", "Ines"], "missed_by": [], "secret_witnesses": ["Viktor"]}, {"step": "change", "who": "Ines", "value": "wicker basket", "present": ["Bruno", "Ines"], "missed_by": ["Bruno"], "secret_witnesses": []}, {"step": "change", "who": "Emeka", "value": "grey locker", "present": ["Emeka", "Ines"], "missed_by": ["Ines"], "secret_witnesses": []}, {"step": "message", "from": "Bruno", "to": "Viktor", "value": "grey locker", "secret_readers": []}]`

## plan-L1-007 (workplace, seed 1510013)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Goran, Viktor, Mirela and Zoltan work on the same team. This is what happened, in order.
1. Call with Goran, Viktor, Mirela and Zoltan: Mirela sets the product release for Wednesday.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Wednesday", "Thursday", "Tuesday", "Monday"]. The names are: ["Goran", "Mirela", "Viktor", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The product release is really set for Tuesday.
2. Goran thinks the product release is set for Tuesday.
3. Viktor thinks the product release is set for Tuesday.
4. Mirela thinks the product release is set for Tuesday.
5. Zoltan thinks the product release is set for Monday.
6. Zoltan thinks that Viktor thinks the product release is set for Thursday.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Mirela", "value": "Thursday", "present": ["Goran", "Mirela", "Viktor", "Zoltan"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Mirela", "value": "Tuesday", "present": ["Goran", "Mirela", "Viktor"], "missed_by": ["Viktor"], "secret_witnesses": []}, {"step": "message", "from": "Mirela", "to": "Zoltan", "value": "Monday", "secret_readers": ["Viktor"]}, {"step": "message", "from": "Zoltan", "to": "Goran", "value": "Tuesday", "secret_readers": ["Viktor"]}]`

## plan-L1-008 (classic, seed 1510014)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Xavier, Emeka, Jonas and Quinn share a house. The garage has four closed containers that nobody can see into: the blue drawer, the red box, the grey locker and the black trunk. This is what happened, in order.
1. Xavier, Emeka, Jonas and Quinn are in the garage. Quinn takes a token out of a pocket and puts it in the blue drawer.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the garage see and hear everything that happens there, unless the story says that a person missed it. People outside the garage see and hear nothing of it, unless the story says so.
- Everyone in the garage can see who else is in the garage.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the token to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the garage, which shows where the token really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the garage that the token is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the token is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the garage at that step, NAME included. "missed_by" lists people in the garage who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the garage who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the garage freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["blue drawer", "red box", "grey locker", "black trunk"]. The names are: ["Emeka", "Jonas", "Quinn", "Xavier"].

Targets. After your last step, all of these must be true:
1. The token is really in the black trunk.
2. Xavier thinks the token is in the grey locker.
3. Emeka thinks the token is in the black trunk.
4. Jonas thinks the token is in the black trunk.
5. Quinn thinks the token is in the black trunk.
6. Xavier thinks that Emeka thinks the token is in the red box.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Jonas", "value": "grey locker", "present": ["Jonas", "Quinn", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Xavier", "to": "Emeka", "value": "red box", "secret_readers": []}, {"step": "change", "who": "Jonas", "value": "black trunk", "present": ["Jonas", "Quinn", "Xavier"], "missed_by": ["Xavier"], "secret_witnesses": []}, {"step": "message", "from": "Quinn", "to": "Emeka", "value": "black trunk", "secret_readers": []}]`

## plan-L1-009 (workplace, seed 1510016)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Emeka, Xavier, Luca and Farah work on the same team. This is what happened, in order.
1. Call with Emeka, Xavier, Luca and Farah: Luca sets the discount on the Fenwick quote at 5%.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME changes the discount on the Fenwick quote to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the quote record and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the discount on the Fenwick quote is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the discount on the Fenwick quote is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["15%", "5%", "10%", "20%"]. The names are: ["Emeka", "Farah", "Luca", "Xavier"].

Targets. After your last step, all of these must be true:
1. The discount on the Fenwick quote is really 10%.
2. Emeka thinks the discount on the Fenwick quote is 10%.
3. Xavier thinks the discount on the Fenwick quote is 15%.
4. Luca thinks the discount on the Fenwick quote is 15%.
5. Farah thinks the discount on the Fenwick quote is 15%.
6. Farah thinks that Emeka thinks the discount on the Fenwick quote is 20%.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Farah", "value": "20%", "present": ["Emeka", "Farah", "Luca", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Luca", "value": "15%", "present": ["Emeka", "Luca", "Xavier"], "missed_by": ["Emeka"], "secret_witnesses": []}, {"step": "message", "from": "Xavier", "to": "Farah", "value": "15%", "secret_readers": ["Emeka"]}, {"step": "change", "who": "Emeka", "value": "10%", "present": ["Emeka"], "missed_by": [], "secret_witnesses": []}]`

## plan-L2-000 (classic, seed 1520001)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Jonas, Soren, Rania, Farah and Pablo share a house. The garage has four closed containers that nobody can see into: the leather bag, the canvas sack, the white cabinet and the blue drawer. This is what happened, in order.
1. Jonas, Soren, Rania, Farah and Pablo are in the garage. Jonas takes a stopwatch out of a pocket and puts it in the canvas sack.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the garage see and hear everything that happens there, unless the story says that a person missed it. People outside the garage see and hear nothing of it, unless the story says so.
- Everyone in the garage can see who else is in the garage.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the stopwatch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the garage, which shows where the stopwatch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the garage that the stopwatch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the stopwatch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the garage at that step, NAME included. "missed_by" lists people in the garage who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the garage who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the garage freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["leather bag", "canvas sack", "white cabinet", "blue drawer"]. The names are: ["Farah", "Jonas", "Pablo", "Rania", "Soren"].

Targets. After your last step, all of these must be true:
1. The stopwatch is really in the canvas sack.
2. Jonas thinks the stopwatch is in the canvas sack.
3. Soren thinks the stopwatch is in the white cabinet.
4. Rania thinks the stopwatch is in the canvas sack.
5. Farah thinks the stopwatch is in the canvas sack.
6. Pablo thinks the stopwatch is in the white cabinet.
7. Soren thinks that Farah thinks the stopwatch is in the canvas sack.
8. Soren thinks that Farah thinks that Pablo thinks the stopwatch is in the leather bag.
9. Farah thinks that Soren thinks the stopwatch is in the canvas sack.
10. Farah thinks that Soren thinks that Pablo thinks the stopwatch is in the leather bag.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Rania", "value": "leather bag", "present": ["Farah", "Jonas", "Pablo", "Rania", "Soren"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Pablo", "value": "white cabinet", "present": ["Jonas", "Pablo", "Rania"], "missed_by": [], "secret_witnesses": ["Soren"]}, {"step": "change", "who": "Rania", "value": "canvas sack", "present": ["Farah", "Jonas", "Rania"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Soren", "to": "Farah", "value": "canvas sack", "secret_readers": []}]`

## plan-L2-001 (workplace, seed 1520002)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Keiko, Farah, Zoltan, Yara and Ines work on the same team. This is what happened, in order.
1. Call with Keiko, Farah, Zoltan, Yara and Ines: Yara picks Ironbridge as the packaging supplier.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME switches the packaging supplier to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the supplier register and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the packaging supplier is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the packaging supplier is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Halcyon", "Brightwater", "Sablewood", "Ironbridge"]. The names are: ["Farah", "Ines", "Keiko", "Yara", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The packaging supplier is really Ironbridge.
2. Keiko thinks the packaging supplier is Ironbridge.
3. Farah thinks the packaging supplier is Ironbridge.
4. Zoltan thinks the packaging supplier is Halcyon.
5. Yara thinks the packaging supplier is Halcyon.
6. Ines thinks the packaging supplier is Ironbridge.
7. Farah thinks that Zoltan thinks the packaging supplier is Halcyon.
8. Farah thinks that Zoltan thinks that Farah thinks the packaging supplier is Sablewood.
9. Zoltan thinks that Farah thinks the packaging supplier is Halcyon.
10. Zoltan thinks that Farah thinks that Zoltan thinks the packaging supplier is Sablewood.

Write at least 1 and at most 5 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Farah", "value": "Sablewood", "present": ["Farah", "Ines", "Keiko", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Farah", "to": "Zoltan", "value": "Sablewood", "secret_readers": []}, {"step": "change", "who": "Keiko", "value": "Halcyon", "present": ["Farah", "Ines", "Keiko", "Yara"], "missed_by": [], "secret_witnesses": ["Zoltan"]}, {"step": "message", "from": "Ines", "to": "Zoltan", "value": "Halcyon", "secret_readers": ["Farah"]}, {"step": "change", "who": "Farah", "value": "Ironbridge", "present": ["Farah", "Ines", "Keiko"], "missed_by": [], "secret_witnesses": []}]`

## plan-L2-002 (classic, seed 1520003)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Pablo, Soren, Wanjiru, Uma and Nadim share a house. The sunroom has four closed containers that nobody can see into: the white cabinet, the canvas sack, the wooden chest and the red box. This is what happened, in order.
1. Pablo, Soren, Wanjiru, Uma and Nadim are in the sunroom. Nadim takes a padlock out of a pocket and puts it in the wooden chest.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the sunroom see and hear everything that happens there, unless the story says that a person missed it. People outside the sunroom see and hear nothing of it, unless the story says so.
- Everyone in the sunroom can see who else is in the sunroom.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the padlock to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the sunroom, which shows where the padlock really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the sunroom that the padlock is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the padlock is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the sunroom at that step, NAME included. "missed_by" lists people in the sunroom who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the sunroom who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the sunroom freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["white cabinet", "canvas sack", "wooden chest", "red box"]. The names are: ["Nadim", "Pablo", "Soren", "Uma", "Wanjiru"].

Targets. After your last step, all of these must be true:
1. The padlock is really in the wooden chest.
2. Pablo thinks the padlock is in the wooden chest.
3. Soren thinks the padlock is in the wooden chest.
4. Wanjiru thinks the padlock is in the wooden chest.
5. Uma thinks the padlock is in the wooden chest.
6. Nadim thinks the padlock is in the wooden chest.
7. Soren thinks that Pablo thinks the padlock is in the wooden chest.
8. Soren thinks that Pablo thinks that Uma thinks the padlock is in the white cabinet.
9. Wanjiru thinks that Uma thinks the padlock is in the wooden chest.
10. Wanjiru thinks that Uma thinks that Soren thinks the padlock is in the red box.

Write at least 1 and at most 6 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Wanjiru", "value": "white cabinet", "present": ["Nadim", "Pablo", "Soren", "Uma", "Wanjiru"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Soren", "value": "red box", "present": ["Nadim", "Pablo", "Soren", "Uma", "Wanjiru"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Nadim", "value": "white cabinet", "present": ["Nadim", "Pablo", "Soren", "Uma"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Pablo", "value": "wooden chest", "present": ["Nadim", "Pablo", "Soren"], "missed_by": ["Soren"], "secret_witnesses": []}, {"step": "check", "who": "Pablo", "present": ["Nadim", "Pablo", "Soren"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Pablo", "to": "Uma", "value": "wooden chest", "secret_readers": ["Wanjiru"]}]`

## plan-L2-003 (workplace, seed 1520006)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Uma, Farah, Zoltan, Nadim and Oksana work on the same team. This is what happened, in order.
1. Call with Uma, Farah, Zoltan, Nadim and Oksana: Oksana picks Sablewood as the packaging supplier.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME switches the packaging supplier to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the supplier register and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the packaging supplier is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the packaging supplier is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Sablewood", "Northwind", "Ironbridge", "Brightwater"]. The names are: ["Farah", "Nadim", "Oksana", "Uma", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The packaging supplier is really Ironbridge.
2. Uma thinks the packaging supplier is Ironbridge.
3. Farah thinks the packaging supplier is Northwind.
4. Zoltan thinks the packaging supplier is Ironbridge.
5. Nadim thinks the packaging supplier is Northwind.
6. Oksana thinks the packaging supplier is Ironbridge.
7. Nadim thinks that Farah thinks the packaging supplier is Northwind.
8. Nadim thinks that Farah thinks that Oksana thinks the packaging supplier is Sablewood.
9. Farah thinks that Zoltan thinks the packaging supplier is Northwind.
10. Farah thinks that Zoltan thinks that Farah thinks the packaging supplier is Sablewood.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Nadim", "value": "Northwind", "present": ["Nadim", "Oksana", "Uma", "Zoltan"], "missed_by": [], "secret_witnesses": ["Farah"]}, {"step": "change", "who": "Uma", "value": "Brightwater", "present": ["Uma", "Zoltan"], "missed_by": ["Zoltan"], "secret_witnesses": []}, {"step": "message", "from": "Nadim", "to": "Farah", "value": "Northwind", "secret_readers": []}, {"step": "change", "who": "Oksana", "value": "Ironbridge", "present": ["Farah", "Oksana", "Uma", "Zoltan"], "missed_by": ["Farah"], "secret_witnesses": []}]`

## plan-L2-004 (classic, seed 1520007)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Zoltan, Luca, Rania, Keiko and Dalia share a house. The greenhouse has four closed containers that nobody can see into: the black trunk, the grey locker, the white cabinet and the canvas sack. This is what happened, in order.
1. Zoltan, Luca, Rania, Keiko and Dalia are in the greenhouse. Rania takes a compass out of a pocket and puts it in the canvas sack.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the greenhouse see and hear everything that happens there, unless the story says that a person missed it. People outside the greenhouse see and hear nothing of it, unless the story says so.
- Everyone in the greenhouse can see who else is in the greenhouse.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the compass to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the greenhouse, which shows where the compass really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the greenhouse that the compass is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the compass is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the greenhouse at that step, NAME included. "missed_by" lists people in the greenhouse who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the greenhouse who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the greenhouse freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["black trunk", "grey locker", "white cabinet", "canvas sack"]. The names are: ["Dalia", "Keiko", "Luca", "Rania", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The compass is really in the canvas sack.
2. Zoltan thinks the compass is in the white cabinet.
3. Luca thinks the compass is in the canvas sack.
4. Rania thinks the compass is in the canvas sack.
5. Keiko thinks the compass is in the canvas sack.
6. Dalia thinks the compass is in the canvas sack.
7. Zoltan thinks that Dalia thinks the compass is in the white cabinet.
8. Zoltan thinks that Dalia thinks that Luca thinks the compass is in the grey locker.
9. Rania thinks that Dalia thinks the compass is in the canvas sack.
10. Rania thinks that Dalia thinks that Zoltan thinks the compass is in the grey locker.

Write at least 1 and at most 6 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Zoltan", "value": "grey locker", "present": ["Dalia", "Keiko", "Luca", "Zoltan"], "missed_by": [], "secret_witnesses": []}, {"step": "check", "who": "Keiko", "present": ["Dalia", "Keiko", "Luca", "Rania", "Zoltan"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Dalia", "value": "white cabinet", "present": ["Dalia", "Keiko", "Luca", "Rania"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Rania", "value": "grey locker", "present": ["Dalia", "Keiko", "Luca", "Rania"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Luca", "value": "canvas sack", "present": ["Dalia", "Keiko", "Luca", "Rania"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Dalia", "to": "Zoltan", "value": "white cabinet", "secret_readers": []}]`

## plan-L2-005 (workplace, seed 1520008)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Oksana, Rania, Keiko, Jonas and Xavier work on the same team. This is what happened, in order.
1. Call with Oksana, Rania, Keiko, Jonas and Xavier: Jonas sets the discount on the Fenwick quote at 5%.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME changes the discount on the Fenwick quote to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the quote record and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the discount on the Fenwick quote is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the discount on the Fenwick quote is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["25%", "5%", "10%", "20%"]. The names are: ["Jonas", "Keiko", "Oksana", "Rania", "Xavier"].

Targets. After your last step, all of these must be true:
1. The discount on the Fenwick quote is really 25%.
2. Oksana thinks the discount on the Fenwick quote is 25%.
3. Rania thinks the discount on the Fenwick quote is 20%.
4. Keiko thinks the discount on the Fenwick quote is 25%.
5. Jonas thinks the discount on the Fenwick quote is 20%.
6. Xavier thinks the discount on the Fenwick quote is 25%.
7. Keiko thinks that Xavier thinks the discount on the Fenwick quote is 25%.
8. Keiko thinks that Xavier thinks that Oksana thinks the discount on the Fenwick quote is 5%.
9. Jonas thinks that Oksana thinks the discount on the Fenwick quote is 20%.
10. Jonas thinks that Oksana thinks that Xavier thinks the discount on the Fenwick quote is 5%.

Write at least 1 and at most 5 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Rania", "value": "25%", "present": ["Jonas", "Oksana", "Rania", "Xavier"], "missed_by": ["Oksana"], "secret_witnesses": []}, {"step": "change", "who": "Keiko", "value": "5%", "present": ["Jonas", "Keiko", "Oksana", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Oksana", "value": "25%", "present": ["Oksana", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Oksana", "to": "Jonas", "value": "20%", "secret_readers": ["Rania"]}, {"step": "message", "from": "Rania", "to": "Xavier", "value": "25%", "secret_readers": ["Keiko"]}]`

## plan-L2-006 (classic, seed 1520010)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Ines, Farah, Quinn, Tariq and Yara share a house. The workshop has four closed containers that nobody can see into: the grey locker, the white cabinet, the wicker basket and the leather bag. This is what happened, in order.
1. Ines, Farah, Quinn, Tariq and Yara are in the workshop. Yara takes a stopwatch out of a pocket and puts it in the leather bag.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the workshop see and hear everything that happens there, unless the story says that a person missed it. People outside the workshop see and hear nothing of it, unless the story says so.
- Everyone in the workshop can see who else is in the workshop.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the stopwatch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the workshop, which shows where the stopwatch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the workshop that the stopwatch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the stopwatch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the workshop at that step, NAME included. "missed_by" lists people in the workshop who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the workshop who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the workshop freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["grey locker", "white cabinet", "wicker basket", "leather bag"]. The names are: ["Farah", "Ines", "Quinn", "Tariq", "Yara"].

Targets. After your last step, all of these must be true:
1. The stopwatch is really in the white cabinet.
2. Ines thinks the stopwatch is in the white cabinet.
3. Farah thinks the stopwatch is in the wicker basket.
4. Quinn thinks the stopwatch is in the grey locker.
5. Tariq thinks the stopwatch is in the white cabinet.
6. Yara thinks the stopwatch is in the white cabinet.
7. Ines thinks that Farah thinks the stopwatch is in the wicker basket.
8. Ines thinks that Farah thinks that Tariq thinks the stopwatch is in the leather bag.
9. Yara thinks that Tariq thinks the stopwatch is in the white cabinet.
10. Yara thinks that Tariq thinks that Quinn thinks the stopwatch is in the leather bag.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Farah", "value": "grey locker", "present": ["Farah", "Tariq", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "check", "who": "Tariq", "present": ["Farah", "Tariq", "Yara"], "missed_by": [], "secret_witnesses": ["Quinn"]}, {"step": "change", "who": "Yara", "value": "wicker basket", "present": ["Farah", "Yara"], "missed_by": [], "secret_witnesses": ["Ines"]}, {"step": "change", "who": "Yara", "value": "white cabinet", "present": ["Tariq", "Yara"], "missed_by": [], "secret_witnesses": ["Ines"]}]`

## plan-L2-007 (workplace, seed 1520011)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Ines, Emeka, Goran, Keiko and Dalia work on the same team. This is what happened, in order.
1. Call with Ines, Emeka, Goran, Keiko and Dalia: Keiko books the client workshop into Room Dogwood.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the client workshop to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the booking system and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the client workshop is booked in VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the client workshop is booked in VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Room Fir", "Room Dogwood", "Room Elm", "Room Cedar"]. The names are: ["Dalia", "Emeka", "Goran", "Ines", "Keiko"].

Targets. After your last step, all of these must be true:
1. The client workshop is really booked in Room Cedar.
2. Ines thinks the client workshop is booked in Room Cedar.
3. Emeka thinks the client workshop is booked in Room Cedar.
4. Goran thinks the client workshop is booked in Room Cedar.
5. Keiko thinks the client workshop is booked in Room Cedar.
6. Dalia thinks the client workshop is booked in Room Cedar.
7. Ines thinks that Emeka thinks the client workshop is booked in Room Cedar.
8. Ines thinks that Emeka thinks that Keiko thinks the client workshop is booked in Room Elm.
9. Keiko thinks that Emeka thinks the client workshop is booked in Room Cedar.
10. Keiko thinks that Emeka thinks that Dalia thinks the client workshop is booked in Room Elm.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Ines", "value": "Room Elm", "present": ["Dalia", "Emeka", "Goran", "Ines", "Keiko"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Dalia", "value": "Room Fir", "present": ["Dalia", "Emeka", "Goran", "Ines"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Ines", "value": "Room Cedar", "present": ["Dalia", "Emeka", "Goran", "Ines"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Emeka", "to": "Keiko", "value": "Room Cedar", "secret_readers": []}]`

## plan-L2-008 (classic, seed 1520012)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Dalia, Zoltan, Amara, Xavier and Viktor share a house. The cellar has four closed containers that nobody can see into: the white cabinet, the leather bag, the black trunk and the green cupboard. This is what happened, in order.
1. Dalia, Zoltan, Amara, Xavier and Viktor are in the cellar. Zoltan takes a marble out of a pocket and puts it in the black trunk.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the cellar see and hear everything that happens there, unless the story says that a person missed it. People outside the cellar see and hear nothing of it, unless the story says so.
- Everyone in the cellar can see who else is in the cellar.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the marble to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the cellar, which shows where the marble really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the cellar that the marble is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the marble is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the cellar at that step, NAME included. "missed_by" lists people in the cellar who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the cellar who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the cellar freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["white cabinet", "leather bag", "black trunk", "green cupboard"]. The names are: ["Amara", "Dalia", "Viktor", "Xavier", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The marble is really in the black trunk.
2. Dalia thinks the marble is in the black trunk.
3. Zoltan thinks the marble is in the black trunk.
4. Amara thinks the marble is in the black trunk.
5. Xavier thinks the marble is in the green cupboard.
6. Viktor thinks the marble is in the green cupboard.
7. Dalia thinks that Amara thinks the marble is in the black trunk.
8. Dalia thinks that Amara thinks that Zoltan thinks the marble is in the green cupboard.
9. Zoltan thinks that Amara thinks the marble is in the black trunk.
10. Zoltan thinks that Amara thinks that Dalia thinks the marble is in the green cupboard.

Write at least 1 and at most 3 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Amara", "value": "green cupboard", "present": ["Amara", "Dalia", "Viktor", "Zoltan"], "missed_by": [], "secret_witnesses": ["Xavier"]}, {"step": "change", "who": "Dalia", "value": "black trunk", "present": ["Amara", "Dalia"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Amara", "to": "Zoltan", "value": "black trunk", "secret_readers": []}]`

## plan-L2-009 (workplace, seed 1520015)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Quinn, Emeka, Keiko, Wanjiru and Ines work on the same team. This is what happened, in order.
1. Call with Quinn, Emeka, Keiko, Wanjiru and Ines: Quinn sets the product release for Thursday.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Friday", "Monday", "Wednesday", "Thursday"]. The names are: ["Emeka", "Ines", "Keiko", "Quinn", "Wanjiru"].

Targets. After your last step, all of these must be true:
1. The product release is really set for Friday.
2. Quinn thinks the product release is set for Friday.
3. Emeka thinks the product release is set for Thursday.
4. Keiko thinks the product release is set for Friday.
5. Wanjiru thinks the product release is set for Friday.
6. Ines thinks the product release is set for Wednesday.
7. Ines thinks that Wanjiru thinks the product release is set for Wednesday.
8. Ines thinks that Wanjiru thinks that Keiko thinks the product release is set for Thursday.
9. Keiko thinks that Wanjiru thinks the product release is set for Friday.
10. Keiko thinks that Wanjiru thinks that Ines thinks the product release is set for Thursday.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Ines", "value": "Wednesday", "present": ["Emeka", "Ines", "Keiko", "Quinn", "Wanjiru"], "missed_by": ["Wanjiru"], "secret_witnesses": []}, {"step": "change", "who": "Quinn", "value": "Thursday", "present": ["Emeka", "Ines", "Keiko", "Quinn", "Wanjiru"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Keiko", "value": "Friday", "present": ["Emeka", "Keiko", "Quinn", "Wanjiru"], "missed_by": ["Emeka"], "secret_witnesses": []}, {"step": "message", "from": "Wanjiru", "to": "Ines", "value": "Wednesday", "secret_readers": []}]`

## plan-L3-000 (classic, seed 1530003)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Keiko, Zoltan, Ines, Tariq, Dalia and Bruno share a house. The study has four closed containers that nobody can see into: the green cupboard, the leather bag, the blue drawer and the wicker basket. This is what happened, in order.
1. Keiko, Zoltan, Ines, Tariq, Dalia and Bruno are in the study. Zoltan takes a torch out of a pocket and puts it in the blue drawer.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the study see and hear everything that happens there, unless the story says that a person missed it. People outside the study see and hear nothing of it, unless the story says so.
- Everyone in the study can see who else is in the study.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the torch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the study, which shows where the torch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the study that the torch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the torch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the study at that step, NAME included. "missed_by" lists people in the study who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the study who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the study freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["green cupboard", "leather bag", "blue drawer", "wicker basket"]. The names are: ["Bruno", "Dalia", "Ines", "Keiko", "Tariq", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The torch is really in the leather bag.
2. Keiko thinks the torch is in the green cupboard.
3. Zoltan thinks the torch is in the green cupboard.
4. Ines thinks the torch is in the leather bag.
5. Tariq thinks the torch is in the leather bag.
6. Dalia thinks the torch is in the leather bag.
7. Bruno thinks the torch is in the leather bag.
8. Tariq thinks that Keiko thinks the torch is in the green cupboard.
9. Tariq thinks that Keiko thinks that Tariq thinks the torch is in the green cupboard.
10. Tariq thinks that Keiko thinks that Tariq thinks that Dalia thinks the torch is in the wicker basket.
11. Zoltan thinks that Tariq thinks the torch is in the green cupboard.
12. Zoltan thinks that Tariq thinks that Zoltan thinks the torch is in the green cupboard.
13. Zoltan thinks that Tariq thinks that Zoltan thinks that Ines thinks the torch is in the blue drawer.
14. Ines thinks that Keiko thinks the torch is in the green cupboard.
15. Ines thinks that Keiko thinks that Ines thinks the torch is in the green cupboard.
16. Ines thinks that Keiko thinks that Ines thinks that Zoltan thinks the torch is in the wicker basket.

Write at least 1 and at most 7 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Dalia", "value": "wicker basket", "present": ["Bruno", "Dalia", "Ines", "Keiko", "Tariq", "Zoltan"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Ines", "to": "Keiko", "value": "green cupboard", "secret_readers": []}, {"step": "message", "from": "Tariq", "to": "Keiko", "value": "green cupboard", "secret_readers": []}, {"step": "change", "who": "Bruno", "value": "blue drawer", "present": ["Bruno", "Dalia", "Ines", "Tariq", "Zoltan"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Ines", "to": "Zoltan", "value": "green cupboard", "secret_readers": ["Tariq"]}, {"step": "message", "from": "Zoltan", "to": "Tariq", "value": "green cupboard", "secret_readers": []}, {"step": "change", "who": "Bruno", "value": "leather bag", "present": ["Bruno", "Dalia", "Ines"], "missed_by": [], "secret_witnesses": ["Tariq"]}]`

## plan-L3-001 (workplace, seed 1530004)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Xavier, Goran, Oksana, Hana, Bruno and Mirela work on the same team. This is what happened, in order.
1. Call with Xavier, Goran, Oksana, Hana, Bruno and Mirela: Xavier sets the discount on the Fenwick quote at 20%.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME changes the discount on the Fenwick quote to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the quote record and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the discount on the Fenwick quote is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the discount on the Fenwick quote is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["25%", "15%", "10%", "20%"]. The names are: ["Bruno", "Goran", "Hana", "Mirela", "Oksana", "Xavier"].

Targets. After your last step, all of these must be true:
1. The discount on the Fenwick quote is really 10%.
2. Xavier thinks the discount on the Fenwick quote is 10%.
3. Goran thinks the discount on the Fenwick quote is 10%.
4. Oksana thinks the discount on the Fenwick quote is 10%.
5. Hana thinks the discount on the Fenwick quote is 10%.
6. Bruno thinks the discount on the Fenwick quote is 10%.
7. Mirela thinks the discount on the Fenwick quote is 10%.
8. Hana thinks that Goran thinks the discount on the Fenwick quote is 10%.
9. Hana thinks that Goran thinks that Bruno thinks the discount on the Fenwick quote is 10%.
10. Hana thinks that Goran thinks that Bruno thinks that Mirela thinks the discount on the Fenwick quote is 20%.
11. Goran thinks that Mirela thinks the discount on the Fenwick quote is 10%.
12. Goran thinks that Mirela thinks that Goran thinks the discount on the Fenwick quote is 10%.
13. Goran thinks that Mirela thinks that Goran thinks that Bruno thinks the discount on the Fenwick quote is 20%.
14. Xavier thinks that Goran thinks the discount on the Fenwick quote is 10%.
15. Xavier thinks that Goran thinks that Bruno thinks the discount on the Fenwick quote is 10%.
16. Xavier thinks that Goran thinks that Bruno thinks that Mirela thinks the discount on the Fenwick quote is 20%.

Write at least 1 and at most 5 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Mirela", "value": "10%", "present": ["Bruno", "Hana", "Mirela", "Oksana", "Xavier"], "missed_by": [], "secret_witnesses": ["Goran"]}, {"step": "message", "from": "Mirela", "to": "Goran", "value": "10%", "secret_readers": []}, {"step": "change", "who": "Oksana", "value": "20%", "present": ["Bruno", "Hana", "Mirela", "Oksana", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Goran", "value": "10%", "present": ["Bruno", "Goran", "Hana", "Xavier"], "missed_by": [], "secret_witnesses": ["Mirela"]}, {"step": "message", "from": "Goran", "to": "Oksana", "value": "10%", "secret_readers": []}]`

## plan-L3-002 (classic, seed 1530006)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Emeka, Hana, Ines, Rania, Goran and Yara share a house. The boathouse has four closed containers that nobody can see into: the white cabinet, the black trunk, the grey locker and the wooden chest. This is what happened, in order.
1. Emeka, Hana, Ines, Rania, Goran and Yara are in the boathouse. Rania takes a stopwatch out of a pocket and puts it in the black trunk.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the boathouse see and hear everything that happens there, unless the story says that a person missed it. People outside the boathouse see and hear nothing of it, unless the story says so.
- Everyone in the boathouse can see who else is in the boathouse.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the stopwatch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the boathouse, which shows where the stopwatch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the boathouse that the stopwatch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the stopwatch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the boathouse at that step, NAME included. "missed_by" lists people in the boathouse who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the boathouse who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the boathouse freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["white cabinet", "black trunk", "grey locker", "wooden chest"]. The names are: ["Emeka", "Goran", "Hana", "Ines", "Rania", "Yara"].

Targets. After your last step, all of these must be true:
1. The stopwatch is really in the black trunk.
2. Emeka thinks the stopwatch is in the black trunk.
3. Hana thinks the stopwatch is in the black trunk.
4. Ines thinks the stopwatch is in the black trunk.
5. Rania thinks the stopwatch is in the black trunk.
6. Goran thinks the stopwatch is in the black trunk.
7. Yara thinks the stopwatch is in the black trunk.
8. Rania thinks that Goran thinks the stopwatch is in the black trunk.
9. Rania thinks that Goran thinks that Emeka thinks the stopwatch is in the black trunk.
10. Rania thinks that Goran thinks that Emeka thinks that Yara thinks the stopwatch is in the grey locker.
11. Emeka thinks that Goran thinks the stopwatch is in the black trunk.
12. Emeka thinks that Goran thinks that Emeka thinks the stopwatch is in the black trunk.
13. Emeka thinks that Goran thinks that Emeka thinks that Yara thinks the stopwatch is in the grey locker.
14. Yara thinks that Emeka thinks the stopwatch is in the black trunk.
15. Yara thinks that Emeka thinks that Rania thinks the stopwatch is in the black trunk.
16. Yara thinks that Emeka thinks that Rania thinks that Goran thinks the stopwatch is in the grey locker.

Write at least 1 and at most 5 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Rania", "value": "white cabinet", "present": ["Emeka", "Goran", "Hana", "Rania", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Rania", "value": "black trunk", "present": ["Emeka", "Goran", "Hana", "Rania", "Yara"], "missed_by": [], "secret_witnesses": ["Ines"]}, {"step": "change", "who": "Emeka", "value": "grey locker", "present": ["Emeka", "Goran", "Rania", "Yara"], "missed_by": ["Goran"], "secret_witnesses": []}, {"step": "change", "who": "Hana", "value": "black trunk", "present": ["Emeka", "Hana", "Rania", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "say", "who": "Rania", "value": "black trunk", "present": ["Emeka", "Goran", "Hana", "Rania"], "missed_by": [], "secret_witnesses": []}]`

## plan-L3-003 (workplace, seed 1530007)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Viktor, Jonas, Goran, Chidi, Quinn and Emeka work on the same team. This is what happened, in order.
1. Call with Viktor, Jonas, Goran, Chidi, Quinn and Emeka: Chidi assigns the Marlow account to the Lisbon office.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME reassigns the Marlow account to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the account list and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the Marlow account is with VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the Marlow account is with VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["the Denver office", "the Nairobi office", "the Osaka office", "the Lisbon office"]. The names are: ["Chidi", "Emeka", "Goran", "Jonas", "Quinn", "Viktor"].

Targets. After your last step, all of these must be true:
1. The Marlow account is really with the Lisbon office.
2. Viktor thinks the Marlow account is with the Nairobi office.
3. Jonas thinks the Marlow account is with the Lisbon office.
4. Goran thinks the Marlow account is with the Lisbon office.
5. Chidi thinks the Marlow account is with the Nairobi office.
6. Quinn thinks the Marlow account is with the Lisbon office.
7. Emeka thinks the Marlow account is with the Lisbon office.
8. Goran thinks that Chidi thinks the Marlow account is with the Nairobi office.
9. Goran thinks that Chidi thinks that Goran thinks the Marlow account is with the Nairobi office.
10. Goran thinks that Chidi thinks that Goran thinks that Emeka thinks the Marlow account is with the Denver office.
11. Chidi thinks that Emeka thinks the Marlow account is with the Lisbon office.
12. Chidi thinks that Emeka thinks that Jonas thinks the Marlow account is with the Lisbon office.
13. Chidi thinks that Emeka thinks that Jonas thinks that Quinn thinks the Marlow account is with the Denver office.
14. Quinn thinks that Goran thinks the Marlow account is with the Lisbon office.
15. Quinn thinks that Goran thinks that Jonas thinks the Marlow account is with the Lisbon office.
16. Quinn thinks that Goran thinks that Jonas thinks that Emeka thinks the Marlow account is with the Nairobi office.

Write at least 1 and at most 7 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Quinn", "value": "the Nairobi office", "present": ["Chidi", "Emeka", "Jonas", "Quinn", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Emeka", "value": "the Denver office", "present": ["Chidi", "Emeka", "Goran", "Jonas", "Quinn"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Goran", "value": "the Nairobi office", "present": ["Emeka", "Goran", "Jonas", "Quinn"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Goran", "value": "the Lisbon office", "present": ["Emeka", "Goran", "Jonas"], "missed_by": ["Jonas"], "secret_witnesses": ["Chidi"]}, {"step": "change", "who": "Goran", "value": "the Osaka office", "present": ["Goran", "Jonas"], "missed_by": ["Jonas"], "secret_witnesses": []}, {"step": "message", "from": "Goran", "to": "Chidi", "value": "the Nairobi office", "secret_readers": []}, {"step": "change", "who": "Jonas", "value": "the Lisbon office", "present": ["Goran", "Jonas", "Quinn"], "missed_by": [], "secret_witnesses": []}]`

## plan-L3-004 (classic, seed 1530011)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Goran, Tariq, Hana, Dalia, Chidi and Jonas share a house. The sunroom has four closed containers that nobody can see into: the grey locker, the canvas sack, the green cupboard and the blue drawer. This is what happened, in order.
1. Goran, Tariq, Hana, Dalia, Chidi and Jonas are in the sunroom. Goran takes a whistle out of a pocket and puts it in the grey locker.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the sunroom see and hear everything that happens there, unless the story says that a person missed it. People outside the sunroom see and hear nothing of it, unless the story says so.
- Everyone in the sunroom can see who else is in the sunroom.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the whistle to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the sunroom, which shows where the whistle really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the sunroom that the whistle is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the whistle is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the sunroom at that step, NAME included. "missed_by" lists people in the sunroom who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the sunroom who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the sunroom freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["grey locker", "canvas sack", "green cupboard", "blue drawer"]. The names are: ["Chidi", "Dalia", "Goran", "Hana", "Jonas", "Tariq"].

Targets. After your last step, all of these must be true:
1. The whistle is really in the canvas sack.
2. Goran thinks the whistle is in the canvas sack.
3. Tariq thinks the whistle is in the canvas sack.
4. Hana thinks the whistle is in the green cupboard.
5. Dalia thinks the whistle is in the canvas sack.
6. Chidi thinks the whistle is in the blue drawer.
7. Jonas thinks the whistle is in the grey locker.
8. Hana thinks that Goran thinks the whistle is in the green cupboard.
9. Hana thinks that Goran thinks that Jonas thinks the whistle is in the blue drawer.
10. Hana thinks that Goran thinks that Jonas thinks that Chidi thinks the whistle is in the grey locker.
11. Dalia thinks that Jonas thinks the whistle is in the canvas sack.
12. Dalia thinks that Jonas thinks that Goran thinks the whistle is in the canvas sack.
13. Dalia thinks that Jonas thinks that Goran thinks that Hana thinks the whistle is in the grey locker.
14. Jonas thinks that Goran thinks the whistle is in the grey locker.
15. Jonas thinks that Goran thinks that Hana thinks the whistle is in the blue drawer.
16. Jonas thinks that Goran thinks that Hana thinks that Chidi thinks the whistle is in the grey locker.

Write at least 1 and at most 8 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Hana", "value": "canvas sack", "present": ["Chidi", "Goran", "Hana", "Jonas", "Tariq"], "missed_by": [], "secret_witnesses": ["Dalia"]}, {"step": "change", "who": "Tariq", "value": "grey locker", "present": ["Chidi", "Goran", "Hana", "Jonas", "Tariq"], "missed_by": ["Goran"], "secret_witnesses": ["Dalia"]}, {"step": "change", "who": "Hana", "value": "blue drawer", "present": ["Goran", "Hana", "Jonas", "Tariq"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Jonas", "value": "canvas sack", "present": ["Goran", "Jonas", "Tariq"], "missed_by": ["Tariq"], "secret_witnesses": ["Dalia"]}, {"step": "message", "from": "Hana", "to": "Chidi", "value": "blue drawer", "secret_readers": []}, {"step": "change", "who": "Jonas", "value": "grey locker", "present": ["Goran", "Jonas", "Tariq"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Goran", "value": "green cupboard", "present": ["Goran", "Hana", "Tariq"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Tariq", "value": "canvas sack", "present": ["Hana", "Tariq"], "missed_by": ["Hana"], "secret_witnesses": ["Goran"]}]`

## plan-L3-005 (workplace, seed 1530013)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Nadim, Goran, Bruno, Wanjiru, Hana and Chidi work on the same team. This is what happened, in order.
1. Call with Nadim, Goran, Bruno, Wanjiru, Hana and Chidi: Hana sets the discount on the Fenwick quote at 25%.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME changes the discount on the Fenwick quote to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the quote record and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the discount on the Fenwick quote is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the discount on the Fenwick quote is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["10%", "25%", "20%", "15%"]. The names are: ["Bruno", "Chidi", "Goran", "Hana", "Nadim", "Wanjiru"].

Targets. After your last step, all of these must be true:
1. The discount on the Fenwick quote is really 15%.
2. Nadim thinks the discount on the Fenwick quote is 10%.
3. Goran thinks the discount on the Fenwick quote is 15%.
4. Bruno thinks the discount on the Fenwick quote is 15%.
5. Wanjiru thinks the discount on the Fenwick quote is 15%.
6. Hana thinks the discount on the Fenwick quote is 15%.
7. Chidi thinks the discount on the Fenwick quote is 10%.
8. Hana thinks that Chidi thinks the discount on the Fenwick quote is 15%.
9. Hana thinks that Chidi thinks that Wanjiru thinks the discount on the Fenwick quote is 20%.
10. Hana thinks that Chidi thinks that Wanjiru thinks that Hana thinks the discount on the Fenwick quote is 25%.
11. Wanjiru thinks that Hana thinks the discount on the Fenwick quote is 15%.
12. Wanjiru thinks that Hana thinks that Wanjiru thinks the discount on the Fenwick quote is 15%.
13. Wanjiru thinks that Hana thinks that Wanjiru thinks that Nadim thinks the discount on the Fenwick quote is 25%.
14. Goran thinks that Chidi thinks the discount on the Fenwick quote is 20%.
15. Goran thinks that Chidi thinks that Bruno thinks the discount on the Fenwick quote is 20%.
16. Goran thinks that Chidi thinks that Bruno thinks that Hana thinks the discount on the Fenwick quote is 25%.

Write at least 1 and at most 7 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Nadim", "value": "20%", "present": ["Bruno", "Chidi", "Goran", "Nadim", "Wanjiru"], "missed_by": ["Wanjiru"], "secret_witnesses": ["Hana"]}, {"step": "message", "from": "Chidi", "to": "Hana", "value": "15%", "secret_readers": ["Bruno"]}, {"step": "change", "who": "Hana", "value": "10%", "present": ["Goran", "Hana", "Wanjiru"], "missed_by": ["Wanjiru"], "secret_witnesses": []}, {"step": "change", "who": "Wanjiru", "value": "15%", "present": ["Goran", "Hana", "Wanjiru"], "missed_by": ["Goran"], "secret_witnesses": ["Chidi"]}, {"step": "change", "who": "Wanjiru", "value": "10%", "present": ["Bruno", "Goran", "Hana", "Wanjiru"], "missed_by": [], "secret_witnesses": ["Chidi"]}, {"step": "message", "from": "Bruno", "to": "Chidi", "value": "10%", "secret_readers": ["Nadim"]}, {"step": "change", "who": "Hana", "value": "15%", "present": ["Bruno", "Goran", "Hana", "Wanjiru"], "missed_by": [], "secret_witnesses": []}]`

## plan-L3-006 (classic, seed 1530014)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Pablo, Uma, Soren, Amara, Keiko and Bruno share a house. The pantry has four closed containers that nobody can see into: the grey locker, the wooden chest, the white cabinet and the black trunk. This is what happened, in order.
1. Pablo, Uma, Soren, Amara, Keiko and Bruno are in the pantry. Amara takes a medal out of a pocket and puts it in the wooden chest.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the pantry see and hear everything that happens there, unless the story says that a person missed it. People outside the pantry see and hear nothing of it, unless the story says so.
- Everyone in the pantry can see who else is in the pantry.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the medal to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the pantry, which shows where the medal really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the pantry that the medal is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the medal is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the pantry at that step, NAME included. "missed_by" lists people in the pantry who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the pantry who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the pantry freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["grey locker", "wooden chest", "white cabinet", "black trunk"]. The names are: ["Amara", "Bruno", "Keiko", "Pablo", "Soren", "Uma"].

Targets. After your last step, all of these must be true:
1. The medal is really in the wooden chest.
2. Pablo thinks the medal is in the white cabinet.
3. Uma thinks the medal is in the wooden chest.
4. Soren thinks the medal is in the wooden chest.
5. Amara thinks the medal is in the wooden chest.
6. Keiko thinks the medal is in the wooden chest.
7. Bruno thinks the medal is in the wooden chest.
8. Soren thinks that Pablo thinks the medal is in the wooden chest.
9. Soren thinks that Pablo thinks that Amara thinks the medal is in the wooden chest.
10. Soren thinks that Pablo thinks that Amara thinks that Bruno thinks the medal is in the grey locker.
11. Pablo thinks that Soren thinks the medal is in the white cabinet.
12. Pablo thinks that Soren thinks that Amara thinks the medal is in the black trunk.
13. Pablo thinks that Soren thinks that Amara thinks that Bruno thinks the medal is in the grey locker.
14. Keiko thinks that Pablo thinks the medal is in the wooden chest.
15. Keiko thinks that Pablo thinks that Soren thinks the medal is in the wooden chest.
16. Keiko thinks that Pablo thinks that Soren thinks that Bruno thinks the medal is in the grey locker.

Write at least 1 and at most 8 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Bruno", "value": "grey locker", "present": ["Amara", "Bruno", "Keiko", "Pablo", "Soren", "Uma"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Soren", "value": "wooden chest", "present": ["Amara", "Keiko", "Pablo", "Soren", "Uma"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Soren", "value": "black trunk", "present": ["Amara", "Keiko", "Soren", "Uma"], "missed_by": [], "secret_witnesses": []}, {"step": "check", "who": "Soren", "present": ["Amara", "Keiko", "Soren", "Uma"], "missed_by": [], "secret_witnesses": ["Pablo"]}, {"step": "change", "who": "Amara", "value": "wooden chest", "present": ["Amara", "Bruno", "Keiko", "Soren"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Keiko", "to": "Uma", "value": "wooden chest", "secret_readers": ["Amara"]}, {"step": "change", "who": "Bruno", "value": "white cabinet", "present": ["Bruno", "Soren"], "missed_by": ["Soren"], "secret_witnesses": ["Pablo"]}, {"step": "change", "who": "Soren", "value": "wooden chest", "present": ["Bruno", "Soren"], "missed_by": [], "secret_witnesses": []}]`

## plan-L3-007 (workplace, seed 1530015)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Uma, Pablo, Bruno, Keiko, Dalia and Viktor work on the same team. This is what happened, in order.
1. Call with Uma, Pablo, Bruno, Keiko, Dalia and Viktor: Pablo sets the product release for Wednesday.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Monday", "Tuesday", "Friday", "Wednesday"]. The names are: ["Bruno", "Dalia", "Keiko", "Pablo", "Uma", "Viktor"].

Targets. After your last step, all of these must be true:
1. The product release is really set for Monday.
2. Uma thinks the product release is set for Monday.
3. Pablo thinks the product release is set for Monday.
4. Bruno thinks the product release is set for Friday.
5. Keiko thinks the product release is set for Monday.
6. Dalia thinks the product release is set for Monday.
7. Viktor thinks the product release is set for Monday.
8. Dalia thinks that Uma thinks the product release is set for Monday.
9. Dalia thinks that Uma thinks that Viktor thinks the product release is set for Monday.
10. Dalia thinks that Uma thinks that Viktor thinks that Keiko thinks the product release is set for Wednesday.
11. Pablo thinks that Uma thinks the product release is set for Monday.
12. Pablo thinks that Uma thinks that Dalia thinks the product release is set for Tuesday.
13. Pablo thinks that Uma thinks that Dalia thinks that Bruno thinks the product release is set for Wednesday.
14. Uma thinks that Pablo thinks the product release is set for Monday.
15. Uma thinks that Pablo thinks that Uma thinks the product release is set for Monday.
16. Uma thinks that Pablo thinks that Uma thinks that Dalia thinks the product release is set for Wednesday.

Write at least 1 and at most 7 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Bruno", "value": "Tuesday", "present": ["Bruno", "Dalia", "Keiko", "Uma", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Viktor", "value": "Wednesday", "present": ["Bruno", "Dalia", "Keiko", "Uma", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Dalia", "to": "Uma", "value": "Tuesday", "secret_readers": ["Pablo"]}, {"step": "change", "who": "Bruno", "value": "Monday", "present": ["Bruno", "Dalia", "Keiko", "Uma", "Viktor"], "missed_by": ["Dalia"], "secret_witnesses": []}, {"step": "message", "from": "Uma", "to": "Pablo", "value": "Monday", "secret_readers": []}, {"step": "change", "who": "Bruno", "value": "Friday", "present": ["Bruno", "Dalia", "Uma", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Uma", "value": "Monday", "present": ["Dalia", "Uma", "Viktor"], "missed_by": [], "secret_witnesses": ["Keiko"]}]`

## plan-L3-008 (classic, seed 1530016)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Mirela, Emeka, Ines, Soren, Yara and Uma share a house. The study has four closed containers that nobody can see into: the blue drawer, the wooden chest, the black trunk and the red box. This is what happened, in order.
1. Mirela, Emeka, Ines, Soren, Yara and Uma are in the study. Uma takes a harmonica out of a pocket and puts it in the red box.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the study see and hear everything that happens there, unless the story says that a person missed it. People outside the study see and hear nothing of it, unless the story says so.
- Everyone in the study can see who else is in the study.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the harmonica to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the study, which shows where the harmonica really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the study that the harmonica is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the harmonica is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the study at that step, NAME included. "missed_by" lists people in the study who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the study who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the study freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["blue drawer", "wooden chest", "black trunk", "red box"]. The names are: ["Emeka", "Ines", "Mirela", "Soren", "Uma", "Yara"].

Targets. After your last step, all of these must be true:
1. The harmonica is really in the red box.
2. Mirela thinks the harmonica is in the red box.
3. Emeka thinks the harmonica is in the wooden chest.
4. Ines thinks the harmonica is in the red box.
5. Soren thinks the harmonica is in the red box.
6. Yara thinks the harmonica is in the red box.
7. Uma thinks the harmonica is in the red box.
8. Yara thinks that Mirela thinks the harmonica is in the red box.
9. Yara thinks that Mirela thinks that Soren thinks the harmonica is in the red box.
10. Yara thinks that Mirela thinks that Soren thinks that Emeka thinks the harmonica is in the black trunk.
11. Soren thinks that Mirela thinks the harmonica is in the red box.
12. Soren thinks that Mirela thinks that Emeka thinks the harmonica is in the wooden chest.
13. Soren thinks that Mirela thinks that Emeka thinks that Uma thinks the harmonica is in the black trunk.
14. Ines thinks that Mirela thinks the harmonica is in the red box.
15. Ines thinks that Mirela thinks that Ines thinks the harmonica is in the red box.
16. Ines thinks that Mirela thinks that Ines thinks that Uma thinks the harmonica is in the black trunk.

Write at least 1 and at most 5 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Ines", "value": "black trunk", "present": ["Emeka", "Ines", "Mirela", "Soren"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Soren", "value": "wooden chest", "present": ["Emeka", "Ines", "Mirela", "Soren", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Yara", "value": "black trunk", "present": ["Emeka", "Ines", "Mirela", "Soren", "Uma", "Yara"], "missed_by": ["Mirela"], "secret_witnesses": []}, {"step": "change", "who": "Emeka", "value": "wooden chest", "present": ["Emeka", "Ines", "Mirela", "Soren", "Yara"], "missed_by": ["Yara"], "secret_witnesses": ["Uma"]}, {"step": "change", "who": "Mirela", "value": "red box", "present": ["Ines", "Mirela", "Soren", "Yara"], "missed_by": [], "secret_witnesses": ["Uma"]}]`

## plan-L3-009 (workplace, seed 1530018)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Xavier, Keiko, Ines, Nadim, Uma and Yara work on the same team. This is what happened, in order.
1. Call with Xavier, Keiko, Ines, Nadim, Uma and Yara: Keiko sets the product release for Tuesday.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Monday", "Friday", "Thursday", "Tuesday"]. The names are: ["Ines", "Keiko", "Nadim", "Uma", "Xavier", "Yara"].

Targets. After your last step, all of these must be true:
1. The product release is really set for Friday.
2. Xavier thinks the product release is set for Friday.
3. Keiko thinks the product release is set for Friday.
4. Ines thinks the product release is set for Tuesday.
5. Nadim thinks the product release is set for Friday.
6. Uma thinks the product release is set for Tuesday.
7. Yara thinks the product release is set for Friday.
8. Nadim thinks that Yara thinks the product release is set for Friday.
9. Nadim thinks that Yara thinks that Keiko thinks the product release is set for Monday.
10. Nadim thinks that Yara thinks that Keiko thinks that Xavier thinks the product release is set for Tuesday.
11. Keiko thinks that Ines thinks the product release is set for Friday.
12. Keiko thinks that Ines thinks that Nadim thinks the product release is set for Friday.
13. Keiko thinks that Ines thinks that Nadim thinks that Xavier thinks the product release is set for Tuesday.
14. Xavier thinks that Nadim thinks the product release is set for Friday.
15. Xavier thinks that Nadim thinks that Ines thinks the product release is set for Friday.
16. Xavier thinks that Nadim thinks that Ines thinks that Keiko thinks the product release is set for Tuesday.

Write at least 1 and at most 6 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Nadim", "value": "Monday", "present": ["Ines", "Keiko", "Nadim", "Uma", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Uma", "value": "Tuesday", "present": ["Ines", "Nadim", "Uma", "Yara"], "missed_by": [], "secret_witnesses": ["Xavier"]}, {"step": "change", "who": "Yara", "value": "Friday", "present": ["Ines", "Nadim", "Yara"], "missed_by": [], "secret_witnesses": ["Keiko"]}, {"step": "say", "who": "Nadim", "value": "Friday", "present": ["Ines", "Nadim", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Ines", "value": "Tuesday", "present": ["Ines", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Keiko", "value": "Friday", "present": ["Keiko", "Xavier"], "missed_by": [], "secret_witnesses": ["Yara"]}]`

## plan-L4-000 (classic, seed 1540001)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Oksana, Keiko, Amara, Bruno, Nadim, Uma, Hana and Emeka share a house. The study has four closed containers that nobody can see into: the leather bag, the grey locker, the blue drawer and the wooden chest. This is what happened, in order.
1. Oksana, Keiko, Amara, Bruno, Nadim, Uma, Hana and Emeka are in the study. Amara takes a magnet out of a pocket and puts it in the blue drawer.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the study see and hear everything that happens there, unless the story says that a person missed it. People outside the study see and hear nothing of it, unless the story says so.
- Everyone in the study can see who else is in the study.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the magnet to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the study, which shows where the magnet really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the study that the magnet is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the magnet is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the study at that step, NAME included. "missed_by" lists people in the study who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the study who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the study freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["leather bag", "grey locker", "blue drawer", "wooden chest"]. The names are: ["Amara", "Bruno", "Emeka", "Hana", "Keiko", "Nadim", "Oksana", "Uma"].

Targets. After your last step, all of these must be true:
1. The magnet is really in the wooden chest.
2. Oksana thinks the magnet is in the blue drawer.
3. Keiko thinks the magnet is in the grey locker.
4. Amara thinks the magnet is in the wooden chest.
5. Bruno thinks the magnet is in the blue drawer.
6. Nadim thinks the magnet is in the blue drawer.
7. Uma thinks the magnet is in the wooden chest.
8. Hana thinks the magnet is in the grey locker.
9. Emeka thinks the magnet is in the wooden chest.
10. Uma thinks that Hana thinks the magnet is in the wooden chest.
11. Uma thinks that Hana thinks that Bruno thinks the magnet is in the blue drawer.
12. Uma thinks that Hana thinks that Bruno thinks that Uma thinks the magnet is in the blue drawer.
13. Uma thinks that Hana thinks that Bruno thinks that Uma thinks that Bruno thinks the magnet is in the blue drawer.
14. Uma thinks that Hana thinks that Bruno thinks that Uma thinks that Bruno thinks that Oksana thinks the magnet is in the leather bag.
15. Emeka thinks that Uma thinks the magnet is in the wooden chest.
16. Emeka thinks that Uma thinks that Hana thinks the magnet is in the wooden chest.
17. Emeka thinks that Uma thinks that Hana thinks that Emeka thinks the magnet is in the wooden chest.
18. Emeka thinks that Uma thinks that Hana thinks that Emeka thinks that Hana thinks the magnet is in the wooden chest.
19. Emeka thinks that Uma thinks that Hana thinks that Emeka thinks that Hana thinks that Keiko thinks the magnet is in the blue drawer.
20. Keiko thinks that Hana thinks the magnet is in the grey locker.
21. Keiko thinks that Hana thinks that Bruno thinks the magnet is in the blue drawer.
22. Keiko thinks that Hana thinks that Bruno thinks that Keiko thinks the magnet is in the blue drawer.
23. Keiko thinks that Hana thinks that Bruno thinks that Keiko thinks that Uma thinks the magnet is in the blue drawer.
24. Keiko thinks that Hana thinks that Bruno thinks that Keiko thinks that Uma thinks that Oksana thinks the magnet is in the leather bag.
25. Bruno thinks that Hana thinks the magnet is in the blue drawer.
26. Bruno thinks that Hana thinks that Amara thinks the magnet is in the blue drawer.
27. Bruno thinks that Hana thinks that Amara thinks that Hana thinks the magnet is in the blue drawer.
28. Bruno thinks that Hana thinks that Amara thinks that Hana thinks that Uma thinks the magnet is in the blue drawer.
29. Bruno thinks that Hana thinks that Amara thinks that Hana thinks that Uma thinks that Oksana thinks the magnet is in the leather bag.
30. Amara thinks that Hana thinks the magnet is in the wooden chest.
31. Amara thinks that Hana thinks that Amara thinks the magnet is in the grey locker.
32. Amara thinks that Hana thinks that Amara thinks that Uma thinks the magnet is in the grey locker.
33. Amara thinks that Hana thinks that Amara thinks that Uma thinks that Keiko thinks the magnet is in the grey locker.
34. Amara thinks that Hana thinks that Amara thinks that Uma thinks that Keiko thinks that Oksana thinks the magnet is in the leather bag.

Write at least 1 and at most 9 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Oksana", "value": "leather bag", "present": ["Amara", "Bruno", "Hana", "Keiko", "Oksana", "Uma"], "missed_by": ["Hana"], "secret_witnesses": []}, {"step": "change", "who": "Hana", "value": "grey locker", "present": ["Amara", "Bruno", "Emeka", "Hana", "Keiko"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Hana", "value": "leather bag", "present": ["Amara", "Bruno", "Emeka", "Hana"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Hana", "value": "grey locker", "present": ["Amara", "Emeka", "Hana", "Nadim"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Keiko", "to": "Oksana", "value": "blue drawer", "secret_readers": ["Uma"]}, {"step": "change", "who": "Bruno", "value": "leather bag", "present": ["Amara", "Bruno", "Emeka", "Hana", "Keiko", "Nadim", "Uma"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Uma", "value": "blue drawer", "present": ["Amara", "Bruno", "Emeka", "Hana", "Keiko", "Nadim", "Uma"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Keiko", "value": "grey locker", "present": ["Amara", "Emeka", "Hana", "Keiko", "Uma"], "missed_by": ["Emeka"], "secret_witnesses": []}, {"step": "change", "who": "Emeka", "value": "wooden chest", "present": ["Emeka", "Hana", "Uma"], "missed_by": ["Hana"], "secret_witnesses": ["Amara"]}]`

## plan-L4-001 (workplace, seed 1540002)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Soren, Xavier, Farah, Yara, Goran, Pablo, Emeka and Bruno work on the same team. This is what happened, in order.
1. Call with Soren, Xavier, Farah, Yara, Goran, Pablo, Emeka and Bruno: Farah fixes Leeds as the place for the team offsite.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the team offsite to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the travel plan and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the team offsite is in VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the team offsite is in VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Leeds", "Porto", "Graz", "Turin"]. The names are: ["Bruno", "Emeka", "Farah", "Goran", "Pablo", "Soren", "Xavier", "Yara"].

Targets. After your last step, all of these must be true:
1. The team offsite is really in Leeds.
2. Soren thinks the team offsite is in Turin.
3. Xavier thinks the team offsite is in Porto.
4. Farah thinks the team offsite is in Leeds.
5. Yara thinks the team offsite is in Turin.
6. Goran thinks the team offsite is in Graz.
7. Pablo thinks the team offsite is in Leeds.
8. Emeka thinks the team offsite is in Leeds.
9. Bruno thinks the team offsite is in Turin.
10. Farah thinks that Emeka thinks the team offsite is in Leeds.
11. Farah thinks that Emeka thinks that Pablo thinks the team offsite is in Leeds.
12. Farah thinks that Emeka thinks that Pablo thinks that Emeka thinks the team offsite is in Leeds.
13. Farah thinks that Emeka thinks that Pablo thinks that Emeka thinks that Pablo thinks the team offsite is in Leeds.
14. Farah thinks that Emeka thinks that Pablo thinks that Emeka thinks that Pablo thinks that Goran thinks the team offsite is in Turin.
15. Bruno thinks that Goran thinks the team offsite is in Porto.
16. Bruno thinks that Goran thinks that Pablo thinks the team offsite is in Porto.
17. Bruno thinks that Goran thinks that Pablo thinks that Farah thinks the team offsite is in Porto.
18. Bruno thinks that Goran thinks that Pablo thinks that Farah thinks that Pablo thinks the team offsite is in Porto.
19. Bruno thinks that Goran thinks that Pablo thinks that Farah thinks that Pablo thinks that Xavier thinks the team offsite is in Graz.
20. Emeka thinks that Goran thinks the team offsite is in Graz.
21. Emeka thinks that Goran thinks that Bruno thinks the team offsite is in Porto.
22. Emeka thinks that Goran thinks that Bruno thinks that Pablo thinks the team offsite is in Porto.
23. Emeka thinks that Goran thinks that Bruno thinks that Pablo thinks that Emeka thinks the team offsite is in Porto.
24. Emeka thinks that Goran thinks that Bruno thinks that Pablo thinks that Emeka thinks that Xavier thinks the team offsite is in Graz.
25. Pablo thinks that Emeka thinks the team offsite is in Leeds.
26. Pablo thinks that Emeka thinks that Farah thinks the team offsite is in Leeds.
27. Pablo thinks that Emeka thinks that Farah thinks that Emeka thinks the team offsite is in Leeds.
28. Pablo thinks that Emeka thinks that Farah thinks that Emeka thinks that Pablo thinks the team offsite is in Leeds.
29. Pablo thinks that Emeka thinks that Farah thinks that Emeka thinks that Pablo thinks that Bruno thinks the team offsite is in Graz.
30. Goran thinks that Pablo thinks the team offsite is in Graz.
31. Goran thinks that Pablo thinks that Farah thinks the team offsite is in Graz.
32. Goran thinks that Pablo thinks that Farah thinks that Emeka thinks the team offsite is in Graz.
33. Goran thinks that Pablo thinks that Farah thinks that Emeka thinks that Farah thinks the team offsite is in Graz.
34. Goran thinks that Pablo thinks that Farah thinks that Emeka thinks that Farah thinks that Bruno thinks the team offsite is in Porto.

Write at least 1 and at most 11 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Farah", "value": "Graz", "present": ["Bruno", "Emeka", "Farah", "Goran", "Pablo", "Soren", "Xavier", "Yara"], "missed_by": ["Goran"], "secret_witnesses": []}, {"step": "change", "who": "Emeka", "value": "Turin", "present": ["Bruno", "Emeka", "Farah", "Goran", "Pablo", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Bruno", "to": "Xavier", "value": "Porto", "secret_readers": []}, {"step": "change", "who": "Pablo", "value": "Graz", "present": ["Bruno", "Emeka", "Farah", "Goran", "Pablo", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Farah", "value": "Porto", "present": ["Bruno", "Emeka", "Farah", "Goran", "Pablo"], "missed_by": ["Pablo"], "secret_witnesses": []}, {"step": "change", "who": "Pablo", "value": "Turin", "present": ["Emeka", "Farah", "Goran", "Pablo"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Pablo", "value": "Graz", "present": ["Emeka", "Farah", "Goran", "Pablo"], "missed_by": ["Farah"], "secret_witnesses": []}, {"step": "message", "from": "Emeka", "to": "Bruno", "value": "Turin", "secret_readers": []}, {"step": "change", "who": "Pablo", "value": "Turin", "present": ["Emeka", "Farah", "Pablo"], "missed_by": [], "secret_witnesses": ["Soren"]}, {"step": "change", "who": "Pablo", "value": "Leeds", "present": ["Emeka", "Farah", "Pablo"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Soren", "to": "Yara", "value": "Turin", "secret_readers": []}]`

## plan-L4-002 (classic, seed 1540003)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Viktor, Zoltan, Oksana, Nadim, Xavier, Jonas, Amara and Farah share a house. The sunroom has four closed containers that nobody can see into: the blue drawer, the red box, the wooden chest and the leather bag. This is what happened, in order.
1. Viktor, Zoltan, Oksana, Nadim, Xavier, Jonas, Amara and Farah are in the sunroom. Jonas takes a brooch out of a pocket and puts it in the leather bag.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the sunroom see and hear everything that happens there, unless the story says that a person missed it. People outside the sunroom see and hear nothing of it, unless the story says so.
- Everyone in the sunroom can see who else is in the sunroom.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the brooch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the sunroom, which shows where the brooch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the sunroom that the brooch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the brooch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the sunroom at that step, NAME included. "missed_by" lists people in the sunroom who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the sunroom who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the sunroom freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["blue drawer", "red box", "wooden chest", "leather bag"]. The names are: ["Amara", "Farah", "Jonas", "Nadim", "Oksana", "Viktor", "Xavier", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The brooch is really in the blue drawer.
2. Viktor thinks the brooch is in the blue drawer.
3. Zoltan thinks the brooch is in the blue drawer.
4. Oksana thinks the brooch is in the blue drawer.
5. Nadim thinks the brooch is in the blue drawer.
6. Xavier thinks the brooch is in the blue drawer.
7. Jonas thinks the brooch is in the blue drawer.
8. Amara thinks the brooch is in the blue drawer.
9. Farah thinks the brooch is in the blue drawer.
10. Nadim thinks that Jonas thinks the brooch is in the blue drawer.
11. Nadim thinks that Jonas thinks that Amara thinks the brooch is in the leather bag.
12. Nadim thinks that Jonas thinks that Amara thinks that Oksana thinks the brooch is in the blue drawer.
13. Nadim thinks that Jonas thinks that Amara thinks that Oksana thinks that Amara thinks the brooch is in the blue drawer.
14. Nadim thinks that Jonas thinks that Amara thinks that Oksana thinks that Amara thinks that Viktor thinks the brooch is in the wooden chest.
15. Amara thinks that Viktor thinks the brooch is in the blue drawer.
16. Amara thinks that Viktor thinks that Jonas thinks the brooch is in the blue drawer.
17. Amara thinks that Viktor thinks that Jonas thinks that Amara thinks the brooch is in the blue drawer.
18. Amara thinks that Viktor thinks that Jonas thinks that Amara thinks that Jonas thinks the brooch is in the blue drawer.
19. Amara thinks that Viktor thinks that Jonas thinks that Amara thinks that Jonas thinks that Xavier thinks the brooch is in the wooden chest.
20. Xavier thinks that Jonas thinks the brooch is in the blue drawer.
21. Xavier thinks that Jonas thinks that Farah thinks the brooch is in the red box.
22. Xavier thinks that Jonas thinks that Farah thinks that Amara thinks the brooch is in the red box.
23. Xavier thinks that Jonas thinks that Farah thinks that Amara thinks that Farah thinks the brooch is in the red box.
24. Xavier thinks that Jonas thinks that Farah thinks that Amara thinks that Farah thinks that Viktor thinks the brooch is in the wooden chest.
25. Farah thinks that Viktor thinks the brooch is in the blue drawer.
26. Farah thinks that Viktor thinks that Amara thinks the brooch is in the blue drawer.
27. Farah thinks that Viktor thinks that Amara thinks that Oksana thinks the brooch is in the blue drawer.
28. Farah thinks that Viktor thinks that Amara thinks that Oksana thinks that Farah thinks the brooch is in the blue drawer.
29. Farah thinks that Viktor thinks that Amara thinks that Oksana thinks that Farah thinks that Xavier thinks the brooch is in the wooden chest.
30. Jonas thinks that Viktor thinks the brooch is in the blue drawer.
31. Jonas thinks that Viktor thinks that Jonas thinks the brooch is in the blue drawer.
32. Jonas thinks that Viktor thinks that Jonas thinks that Oksana thinks the brooch is in the blue drawer.
33. Jonas thinks that Viktor thinks that Jonas thinks that Oksana thinks that Farah thinks the brooch is in the blue drawer.
34. Jonas thinks that Viktor thinks that Jonas thinks that Oksana thinks that Farah thinks that Xavier thinks the brooch is in the wooden chest.

Write at least 1 and at most 9 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Xavier", "value": "wooden chest", "present": ["Amara", "Farah", "Jonas", "Nadim", "Oksana", "Viktor", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Oksana", "value": "blue drawer", "present": ["Amara", "Farah", "Jonas", "Nadim", "Oksana", "Xavier"], "missed_by": [], "secret_witnesses": ["Viktor"]}, {"step": "change", "who": "Xavier", "value": "red box", "present": ["Amara", "Farah", "Jonas", "Nadim", "Oksana", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Jonas", "value": "blue drawer", "present": ["Amara", "Farah", "Jonas", "Nadim", "Oksana"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Farah", "value": "leather bag", "present": ["Amara", "Farah", "Jonas", "Nadim"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Farah", "value": "blue drawer", "present": ["Amara", "Farah", "Jonas", "Oksana"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Jonas", "to": "Nadim", "value": "blue drawer", "secret_readers": ["Xavier"]}, {"step": "check", "who": "Amara", "present": ["Amara", "Farah", "Jonas", "Oksana", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Nadim", "to": "Zoltan", "value": "blue drawer", "secret_readers": []}]`

## plan-L4-003 (workplace, seed 1540006)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Jonas, Mirela, Yara, Hana, Goran, Viktor, Rania and Farah work on the same team. This is what happened, in order.
1. Call with Jonas, Mirela, Yara, Hana, Goran, Viktor, Rania and Farah: Mirela picks Halcyon as the packaging supplier.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME switches the packaging supplier to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the supplier register and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the packaging supplier is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the packaging supplier is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Ironbridge", "Sablewood", "Halcyon", "Brightwater"]. The names are: ["Farah", "Goran", "Hana", "Jonas", "Mirela", "Rania", "Viktor", "Yara"].

Targets. After your last step, all of these must be true:
1. The packaging supplier is really Sablewood.
2. Jonas thinks the packaging supplier is Sablewood.
3. Mirela thinks the packaging supplier is Sablewood.
4. Yara thinks the packaging supplier is Sablewood.
5. Hana thinks the packaging supplier is Sablewood.
6. Goran thinks the packaging supplier is Sablewood.
7. Viktor thinks the packaging supplier is Sablewood.
8. Rania thinks the packaging supplier is Sablewood.
9. Farah thinks the packaging supplier is Ironbridge.
10. Goran thinks that Mirela thinks the packaging supplier is Sablewood.
11. Goran thinks that Mirela thinks that Goran thinks the packaging supplier is Sablewood.
12. Goran thinks that Mirela thinks that Goran thinks that Mirela thinks the packaging supplier is Sablewood.
13. Goran thinks that Mirela thinks that Goran thinks that Mirela thinks that Goran thinks the packaging supplier is Sablewood.
14. Goran thinks that Mirela thinks that Goran thinks that Mirela thinks that Goran thinks that Yara thinks the packaging supplier is Halcyon.
15. Farah thinks that Yara thinks the packaging supplier is Brightwater.
16. Farah thinks that Yara thinks that Mirela thinks the packaging supplier is Halcyon.
17. Farah thinks that Yara thinks that Mirela thinks that Yara thinks the packaging supplier is Halcyon.
18. Farah thinks that Yara thinks that Mirela thinks that Yara thinks that Mirela thinks the packaging supplier is Halcyon.
19. Farah thinks that Yara thinks that Mirela thinks that Yara thinks that Mirela thinks that Rania thinks the packaging supplier is Ironbridge.
20. Hana thinks that Jonas thinks the packaging supplier is Sablewood.
21. Hana thinks that Jonas thinks that Viktor thinks the packaging supplier is Sablewood.
22. Hana thinks that Jonas thinks that Viktor thinks that Jonas thinks the packaging supplier is Sablewood.
23. Hana thinks that Jonas thinks that Viktor thinks that Jonas thinks that Viktor thinks the packaging supplier is Sablewood.
24. Hana thinks that Jonas thinks that Viktor thinks that Jonas thinks that Viktor thinks that Rania thinks the packaging supplier is Halcyon.
25. Jonas thinks that Mirela thinks the packaging supplier is Sablewood.
26. Jonas thinks that Mirela thinks that Rania thinks the packaging supplier is Sablewood.
27. Jonas thinks that Mirela thinks that Rania thinks that Yara thinks the packaging supplier is Sablewood.
28. Jonas thinks that Mirela thinks that Rania thinks that Yara thinks that Mirela thinks the packaging supplier is Sablewood.
29. Jonas thinks that Mirela thinks that Rania thinks that Yara thinks that Mirela thinks that Goran thinks the packaging supplier is Brightwater.
30. Viktor thinks that Rania thinks the packaging supplier is Ironbridge.
31. Viktor thinks that Rania thinks that Mirela thinks the packaging supplier is Ironbridge.
32. Viktor thinks that Rania thinks that Mirela thinks that Yara thinks the packaging supplier is Ironbridge.
33. Viktor thinks that Rania thinks that Mirela thinks that Yara thinks that Mirela thinks the packaging supplier is Ironbridge.
34. Viktor thinks that Rania thinks that Mirela thinks that Yara thinks that Mirela thinks that Goran thinks the packaging supplier is Brightwater.

Write at least 1 and at most 12 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Goran", "value": "Brightwater", "present": ["Farah", "Goran", "Jonas", "Mirela", "Rania", "Viktor", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Farah", "value": "Sablewood", "present": ["Farah", "Jonas", "Mirela", "Rania", "Viktor", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Mirela", "value": "Ironbridge", "present": ["Farah", "Mirela", "Rania", "Viktor", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Mirela", "value": "Halcyon", "present": ["Farah", "Mirela", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Yara", "value": "Sablewood", "present": ["Mirela", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Yara", "to": "Farah", "value": "Brightwater", "secret_readers": []}, {"step": "change", "who": "Mirela", "value": "Halcyon", "present": ["Goran", "Mirela", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Yara", "value": "Sablewood", "present": ["Goran", "Mirela", "Yara"], "missed_by": ["Goran"], "secret_witnesses": []}, {"step": "say", "who": "Mirela", "value": "Sablewood", "present": ["Goran", "Mirela", "Rania"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Goran", "to": "Jonas", "value": "Sablewood", "secret_readers": []}, {"step": "message", "from": "Hana", "to": "Farah", "value": "Ironbridge", "secret_readers": []}, {"step": "message", "from": "Jonas", "to": "Viktor", "value": "Sablewood", "secret_readers": ["Hana"]}]`

## plan-L4-004 (classic, seed 1540008)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Emeka, Jonas, Soren, Quinn, Hana, Rania, Tariq and Oksana share a house. The garage has four closed containers that nobody can see into: the wooden chest, the canvas sack, the red box and the black trunk. This is what happened, in order.
1. Emeka, Jonas, Soren, Quinn, Hana, Rania, Tariq and Oksana are in the garage. Tariq takes a padlock out of a pocket and puts it in the red box.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the garage see and hear everything that happens there, unless the story says that a person missed it. People outside the garage see and hear nothing of it, unless the story says so.
- Everyone in the garage can see who else is in the garage.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the padlock to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the garage, which shows where the padlock really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the garage that the padlock is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the padlock is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the garage at that step, NAME included. "missed_by" lists people in the garage who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the garage who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the garage freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["wooden chest", "canvas sack", "red box", "black trunk"]. The names are: ["Emeka", "Hana", "Jonas", "Oksana", "Quinn", "Rania", "Soren", "Tariq"].

Targets. After your last step, all of these must be true:
1. The padlock is really in the canvas sack.
2. Emeka thinks the padlock is in the canvas sack.
3. Jonas thinks the padlock is in the wooden chest.
4. Soren thinks the padlock is in the canvas sack.
5. Quinn thinks the padlock is in the canvas sack.
6. Hana thinks the padlock is in the canvas sack.
7. Rania thinks the padlock is in the canvas sack.
8. Tariq thinks the padlock is in the wooden chest.
9. Oksana thinks the padlock is in the canvas sack.
10. Hana thinks that Jonas thinks the padlock is in the wooden chest.
11. Hana thinks that Jonas thinks that Soren thinks the padlock is in the black trunk.
12. Hana thinks that Jonas thinks that Soren thinks that Jonas thinks the padlock is in the black trunk.
13. Hana thinks that Jonas thinks that Soren thinks that Jonas thinks that Soren thinks the padlock is in the black trunk.
14. Hana thinks that Jonas thinks that Soren thinks that Jonas thinks that Soren thinks that Emeka thinks the padlock is in the red box.
15. Tariq thinks that Rania thinks the padlock is in the red box.
16. Tariq thinks that Rania thinks that Emeka thinks the padlock is in the red box.
17. Tariq thinks that Rania thinks that Emeka thinks that Soren thinks the padlock is in the red box.
18. Tariq thinks that Rania thinks that Emeka thinks that Soren thinks that Rania thinks the padlock is in the red box.
19. Tariq thinks that Rania thinks that Emeka thinks that Soren thinks that Rania thinks that Quinn thinks the padlock is in the wooden chest.
20. Soren thinks that Hana thinks the padlock is in the canvas sack.
21. Soren thinks that Hana thinks that Emeka thinks the padlock is in the canvas sack.
22. Soren thinks that Hana thinks that Emeka thinks that Quinn thinks the padlock is in the canvas sack.
23. Soren thinks that Hana thinks that Emeka thinks that Quinn thinks that Rania thinks the padlock is in the canvas sack.
24. Soren thinks that Hana thinks that Emeka thinks that Quinn thinks that Rania thinks that Jonas thinks the padlock is in the black trunk.
25. Oksana thinks that Hana thinks the padlock is in the canvas sack.
26. Oksana thinks that Hana thinks that Oksana thinks the padlock is in the canvas sack.
27. Oksana thinks that Hana thinks that Oksana thinks that Emeka thinks the padlock is in the canvas sack.
28. Oksana thinks that Hana thinks that Oksana thinks that Emeka thinks that Hana thinks the padlock is in the canvas sack.
29. Oksana thinks that Hana thinks that Oksana thinks that Emeka thinks that Hana thinks that Jonas thinks the padlock is in the black trunk.
30. Quinn thinks that Hana thinks the padlock is in the canvas sack.
31. Quinn thinks that Hana thinks that Quinn thinks the padlock is in the canvas sack.
32. Quinn thinks that Hana thinks that Quinn thinks that Emeka thinks the padlock is in the canvas sack.
33. Quinn thinks that Hana thinks that Quinn thinks that Emeka thinks that Tariq thinks the padlock is in the wooden chest.
34. Quinn thinks that Hana thinks that Quinn thinks that Emeka thinks that Tariq thinks that Jonas thinks the padlock is in the black trunk.

Write at least 1 and at most 10 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Rania", "value": "canvas sack", "present": ["Emeka", "Hana", "Jonas", "Oksana", "Quinn", "Rania", "Soren", "Tariq"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Quinn", "value": "red box", "present": ["Emeka", "Hana", "Jonas", "Oksana", "Quinn", "Soren"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Rania", "value": "wooden chest", "present": ["Hana", "Jonas", "Oksana", "Quinn", "Rania", "Soren"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Quinn", "value": "black trunk", "present": ["Hana", "Jonas", "Oksana", "Quinn", "Rania", "Soren", "Tariq"], "missed_by": [], "secret_witnesses": []}, {"step": "check", "who": "Jonas", "present": ["Emeka", "Hana", "Jonas", "Oksana", "Quinn", "Rania", "Soren", "Tariq"], "missed_by": ["Hana"], "secret_witnesses": []}, {"step": "change", "who": "Soren", "value": "wooden chest", "present": ["Emeka", "Hana", "Oksana", "Quinn", "Rania", "Soren", "Tariq"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Hana", "value": "red box", "present": ["Emeka", "Hana", "Rania", "Soren", "Tariq"], "missed_by": ["Emeka"], "secret_witnesses": ["Quinn"]}, {"step": "change", "who": "Soren", "value": "canvas sack", "present": ["Emeka", "Hana", "Oksana", "Rania", "Soren"], "missed_by": ["Rania"], "secret_witnesses": []}, {"step": "check", "who": "Hana", "present": ["Emeka", "Hana", "Oksana", "Quinn", "Rania", "Soren"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Hana", "to": "Jonas", "value": "wooden chest", "secret_readers": ["Tariq"]}]`

## plan-L4-005 (workplace, seed 1540010)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Rania, Yara, Keiko, Soren, Zoltan, Wanjiru, Xavier and Luca work on the same team. This is what happened, in order.
1. Call with Rania, Yara, Keiko, Soren, Zoltan, Wanjiru, Xavier and Luca: Zoltan fixes Ghent as the place for the team offsite.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the team offsite to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the travel plan and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the team offsite is in VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the team offsite is in VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Graz", "Ghent", "Porto", "Leeds"]. The names are: ["Keiko", "Luca", "Rania", "Soren", "Wanjiru", "Xavier", "Yara", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The team offsite is really in Graz.
2. Rania thinks the team offsite is in Graz.
3. Yara thinks the team offsite is in Graz.
4. Keiko thinks the team offsite is in Graz.
5. Soren thinks the team offsite is in Graz.
6. Zoltan thinks the team offsite is in Graz.
7. Wanjiru thinks the team offsite is in Graz.
8. Xavier thinks the team offsite is in Graz.
9. Luca thinks the team offsite is in Graz.
10. Xavier thinks that Luca thinks the team offsite is in Graz.
11. Xavier thinks that Luca thinks that Rania thinks the team offsite is in Porto.
12. Xavier thinks that Luca thinks that Rania thinks that Soren thinks the team offsite is in Ghent.
13. Xavier thinks that Luca thinks that Rania thinks that Soren thinks that Yara thinks the team offsite is in Ghent.
14. Xavier thinks that Luca thinks that Rania thinks that Soren thinks that Yara thinks that Wanjiru thinks the team offsite is in Porto.
15. Wanjiru thinks that Yara thinks the team offsite is in Graz.
16. Wanjiru thinks that Yara thinks that Zoltan thinks the team offsite is in Graz.
17. Wanjiru thinks that Yara thinks that Zoltan thinks that Rania thinks the team offsite is in Graz.
18. Wanjiru thinks that Yara thinks that Zoltan thinks that Rania thinks that Xavier thinks the team offsite is in Graz.
19. Wanjiru thinks that Yara thinks that Zoltan thinks that Rania thinks that Xavier thinks that Soren thinks the team offsite is in Porto.
20. Keiko thinks that Rania thinks the team offsite is in Graz.
21. Keiko thinks that Rania thinks that Luca thinks the team offsite is in Graz.
22. Keiko thinks that Rania thinks that Luca thinks that Zoltan thinks the team offsite is in Graz.
23. Keiko thinks that Rania thinks that Luca thinks that Zoltan thinks that Wanjiru thinks the team offsite is in Graz.
24. Keiko thinks that Rania thinks that Luca thinks that Zoltan thinks that Wanjiru thinks that Xavier thinks the team offsite is in Porto.
25. Soren thinks that Zoltan thinks the team offsite is in Graz.
26. Soren thinks that Zoltan thinks that Rania thinks the team offsite is in Graz.
27. Soren thinks that Zoltan thinks that Rania thinks that Zoltan thinks the team offsite is in Graz.
28. Soren thinks that Zoltan thinks that Rania thinks that Zoltan thinks that Wanjiru thinks the team offsite is in Graz.
29. Soren thinks that Zoltan thinks that Rania thinks that Zoltan thinks that Wanjiru thinks that Xavier thinks the team offsite is in Porto.
30. Zoltan thinks that Rania thinks the team offsite is in Graz.
31. Zoltan thinks that Rania thinks that Yara thinks the team offsite is in Graz.
32. Zoltan thinks that Rania thinks that Yara thinks that Rania thinks the team offsite is in Graz.
33. Zoltan thinks that Rania thinks that Yara thinks that Rania thinks that Yara thinks the team offsite is in Graz.
34. Zoltan thinks that Rania thinks that Yara thinks that Rania thinks that Yara thinks that Wanjiru thinks the team offsite is in Leeds.

Write at least 1 and at most 10 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Soren", "value": "Porto", "present": ["Luca", "Rania", "Soren", "Wanjiru", "Xavier", "Yara", "Zoltan"], "missed_by": [], "secret_witnesses": ["Keiko"]}, {"step": "change", "who": "Soren", "value": "Ghent", "present": ["Luca", "Rania", "Soren", "Xavier", "Yara", "Zoltan"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Yara", "value": "Graz", "present": ["Luca", "Rania", "Soren", "Wanjiru", "Yara", "Zoltan"], "missed_by": [], "secret_witnesses": ["Keiko"]}, {"step": "check", "who": "Yara", "present": ["Luca", "Rania", "Wanjiru", "Xavier", "Yara", "Zoltan"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Luca", "value": "Leeds", "present": ["Luca", "Rania", "Wanjiru", "Xavier", "Yara"], "missed_by": [], "secret_witnesses": ["Zoltan"]}, {"step": "change", "who": "Yara", "value": "Porto", "present": ["Luca", "Rania", "Wanjiru", "Xavier", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Soren", "value": "Graz", "present": ["Rania", "Soren", "Yara"], "missed_by": ["Yara"], "secret_witnesses": ["Xavier"]}, {"step": "change", "who": "Soren", "value": "Leeds", "present": ["Rania", "Soren", "Yara", "Zoltan"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Zoltan", "value": "Graz", "present": ["Rania", "Soren", "Yara", "Zoltan"], "missed_by": [], "secret_witnesses": ["Wanjiru"]}, {"step": "message", "from": "Xavier", "to": "Luca", "value": "Graz", "secret_readers": []}]`

## plan-L4-006 (classic, seed 1540011)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Nadim, Luca, Ines, Farah, Hana, Jonas, Viktor and Mirela share a house. The sunroom has four closed containers that nobody can see into: the green cupboard, the wooden chest, the grey locker and the black trunk. This is what happened, in order.
1. Nadim, Luca, Ines, Farah, Hana, Jonas, Viktor and Mirela are in the sunroom. Nadim takes a marble out of a pocket and puts it in the green cupboard.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the sunroom see and hear everything that happens there, unless the story says that a person missed it. People outside the sunroom see and hear nothing of it, unless the story says so.
- Everyone in the sunroom can see who else is in the sunroom.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the marble to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the sunroom, which shows where the marble really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the sunroom that the marble is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the marble is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the sunroom at that step, NAME included. "missed_by" lists people in the sunroom who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the sunroom who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the sunroom freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["green cupboard", "wooden chest", "grey locker", "black trunk"]. The names are: ["Farah", "Hana", "Ines", "Jonas", "Luca", "Mirela", "Nadim", "Viktor"].

Targets. After your last step, all of these must be true:
1. The marble is really in the green cupboard.
2. Nadim thinks the marble is in the green cupboard.
3. Luca thinks the marble is in the green cupboard.
4. Ines thinks the marble is in the green cupboard.
5. Farah thinks the marble is in the green cupboard.
6. Hana thinks the marble is in the green cupboard.
7. Jonas thinks the marble is in the green cupboard.
8. Viktor thinks the marble is in the green cupboard.
9. Mirela thinks the marble is in the green cupboard.
10. Farah thinks that Jonas thinks the marble is in the grey locker.
11. Farah thinks that Jonas thinks that Farah thinks the marble is in the grey locker.
12. Farah thinks that Jonas thinks that Farah thinks that Viktor thinks the marble is in the grey locker.
13. Farah thinks that Jonas thinks that Farah thinks that Viktor thinks that Luca thinks the marble is in the grey locker.
14. Farah thinks that Jonas thinks that Farah thinks that Viktor thinks that Luca thinks that Hana thinks the marble is in the black trunk.
15. Hana thinks that Viktor thinks the marble is in the green cupboard.
16. Hana thinks that Viktor thinks that Luca thinks the marble is in the green cupboard.
17. Hana thinks that Viktor thinks that Luca thinks that Farah thinks the marble is in the green cupboard.
18. Hana thinks that Viktor thinks that Luca thinks that Farah thinks that Luca thinks the marble is in the green cupboard.
19. Hana thinks that Viktor thinks that Luca thinks that Farah thinks that Luca thinks that Jonas thinks the marble is in the black trunk.
20. Viktor thinks that Jonas thinks the marble is in the grey locker.
21. Viktor thinks that Jonas thinks that Luca thinks the marble is in the grey locker.
22. Viktor thinks that Jonas thinks that Luca thinks that Jonas thinks the marble is in the grey locker.
23. Viktor thinks that Jonas thinks that Luca thinks that Jonas thinks that Farah thinks the marble is in the grey locker.
24. Viktor thinks that Jonas thinks that Luca thinks that Jonas thinks that Farah thinks that Hana thinks the marble is in the black trunk.
25. Luca thinks that Viktor thinks the marble is in the green cupboard.
26. Luca thinks that Viktor thinks that Luca thinks the marble is in the green cupboard.
27. Luca thinks that Viktor thinks that Luca thinks that Farah thinks the marble is in the green cupboard.
28. Luca thinks that Viktor thinks that Luca thinks that Farah thinks that Viktor thinks the marble is in the green cupboard.
29. Luca thinks that Viktor thinks that Luca thinks that Farah thinks that Viktor thinks that Jonas thinks the marble is in the black trunk.
30. Jonas thinks that Luca thinks the marble is in the green cupboard.
31. Jonas thinks that Luca thinks that Farah thinks the marble is in the green cupboard.
32. Jonas thinks that Luca thinks that Farah thinks that Luca thinks the marble is in the green cupboard.
33. Jonas thinks that Luca thinks that Farah thinks that Luca thinks that Viktor thinks the marble is in the green cupboard.
34. Jonas thinks that Luca thinks that Farah thinks that Luca thinks that Viktor thinks that Jonas thinks the marble is in the grey locker.

Write at least 1 and at most 10 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Luca", "value": "black trunk", "present": ["Farah", "Hana", "Jonas", "Luca", "Mirela", "Viktor"], "missed_by": [], "secret_witnesses": ["Ines"]}, {"step": "change", "who": "Viktor", "value": "green cupboard", "present": ["Farah", "Hana", "Jonas", "Luca", "Mirela", "Viktor"], "missed_by": [], "secret_witnesses": ["Ines"]}, {"step": "change", "who": "Luca", "value": "black trunk", "present": ["Farah", "Hana", "Jonas", "Luca", "Viktor"], "missed_by": ["Jonas"], "secret_witnesses": []}, {"step": "change", "who": "Jonas", "value": "grey locker", "present": ["Farah", "Jonas", "Luca", "Viktor"], "missed_by": ["Luca"], "secret_witnesses": []}, {"step": "change", "who": "Hana", "value": "wooden chest", "present": ["Hana", "Luca", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Hana", "value": "grey locker", "present": ["Hana", "Luca", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Viktor", "value": "wooden chest", "present": ["Hana", "Luca", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Luca", "value": "black trunk", "present": ["Hana", "Ines", "Luca", "Mirela", "Nadim", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Luca", "value": "green cupboard", "present": ["Hana", "Ines", "Luca", "Nadim", "Viktor"], "missed_by": ["Hana"], "secret_witnesses": []}, {"step": "say", "who": "Ines", "value": "green cupboard", "present": ["Farah", "Hana", "Ines", "Luca", "Mirela", "Nadim", "Viktor"], "missed_by": [], "secret_witnesses": ["Jonas"]}]`

## plan-L4-007 (workplace, seed 1540012)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Rania, Jonas, Quinn, Keiko, Luca, Chidi, Amara and Ines work on the same team. This is what happened, in order.
1. Call with Rania, Jonas, Quinn, Keiko, Luca, Chidi, Amara and Ines: Chidi sets the product release for Friday.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Thursday", "Wednesday", "Friday", "Monday"]. The names are: ["Amara", "Chidi", "Ines", "Jonas", "Keiko", "Luca", "Quinn", "Rania"].

Targets. After your last step, all of these must be true:
1. The product release is really set for Monday.
2. Rania thinks the product release is set for Monday.
3. Jonas thinks the product release is set for Wednesday.
4. Quinn thinks the product release is set for Monday.
5. Keiko thinks the product release is set for Monday.
6. Luca thinks the product release is set for Thursday.
7. Chidi thinks the product release is set for Friday.
8. Amara thinks the product release is set for Friday.
9. Ines thinks the product release is set for Monday.
10. Luca thinks that Keiko thinks the product release is set for Wednesday.
11. Luca thinks that Keiko thinks that Quinn thinks the product release is set for Wednesday.
12. Luca thinks that Keiko thinks that Quinn thinks that Jonas thinks the product release is set for Wednesday.
13. Luca thinks that Keiko thinks that Quinn thinks that Jonas thinks that Luca thinks the product release is set for Wednesday.
14. Luca thinks that Keiko thinks that Quinn thinks that Jonas thinks that Luca thinks that Ines thinks the product release is set for Thursday.
15. Rania thinks that Keiko thinks the product release is set for Monday.
16. Rania thinks that Keiko thinks that Amara thinks the product release is set for Wednesday.
17. Rania thinks that Keiko thinks that Amara thinks that Keiko thinks the product release is set for Wednesday.
18. Rania thinks that Keiko thinks that Amara thinks that Keiko thinks that Jonas thinks the product release is set for Monday.
19. Rania thinks that Keiko thinks that Amara thinks that Keiko thinks that Jonas thinks that Ines thinks the product release is set for Thursday.
20. Chidi thinks that Keiko thinks the product release is set for Friday.
21. Chidi thinks that Keiko thinks that Rania thinks the product release is set for Friday.
22. Chidi thinks that Keiko thinks that Rania thinks that Keiko thinks the product release is set for Friday.
23. Chidi thinks that Keiko thinks that Rania thinks that Keiko thinks that Quinn thinks the product release is set for Friday.
24. Chidi thinks that Keiko thinks that Rania thinks that Keiko thinks that Quinn thinks that Amara thinks the product release is set for Wednesday.
25. Amara thinks that Keiko thinks the product release is set for Friday.
26. Amara thinks that Keiko thinks that Quinn thinks the product release is set for Friday.
27. Amara thinks that Keiko thinks that Quinn thinks that Jonas thinks the product release is set for Monday.
28. Amara thinks that Keiko thinks that Quinn thinks that Jonas thinks that Luca thinks the product release is set for Wednesday.
29. Amara thinks that Keiko thinks that Quinn thinks that Jonas thinks that Luca thinks that Ines thinks the product release is set for Thursday.
30. Quinn thinks that Keiko thinks the product release is set for Monday.
31. Quinn thinks that Keiko thinks that Jonas thinks the product release is set for Monday.
32. Quinn thinks that Keiko thinks that Jonas thinks that Luca thinks the product release is set for Wednesday.
33. Quinn thinks that Keiko thinks that Jonas thinks that Luca thinks that Quinn thinks the product release is set for Wednesday.
34. Quinn thinks that Keiko thinks that Jonas thinks that Luca thinks that Quinn thinks that Ines thinks the product release is set for Thursday.

Write at least 1 and at most 8 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Ines", "value": "Thursday", "present": ["Amara", "Ines", "Jonas", "Keiko", "Luca", "Quinn"], "missed_by": ["Keiko"], "secret_witnesses": ["Rania"]}, {"step": "change", "who": "Amara", "value": "Wednesday", "present": ["Amara", "Jonas", "Keiko", "Luca", "Quinn", "Rania"], "missed_by": [], "secret_witnesses": ["Chidi"]}, {"step": "message", "from": "Rania", "to": "Luca", "value": "Thursday", "secret_readers": []}, {"step": "change", "who": "Amara", "value": "Monday", "present": ["Amara", "Jonas", "Keiko", "Quinn", "Rania"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Amara", "value": "Wednesday", "present": ["Amara", "Keiko", "Quinn", "Rania"], "missed_by": [], "secret_witnesses": ["Jonas"]}, {"step": "change", "who": "Keiko", "value": "Friday", "present": ["Amara", "Keiko", "Quinn", "Rania"], "missed_by": ["Rania"], "secret_witnesses": []}, {"step": "check", "who": "Chidi", "present": ["Chidi", "Keiko", "Quinn", "Rania"], "missed_by": ["Keiko"], "secret_witnesses": []}, {"step": "change", "who": "Rania", "value": "Monday", "present": ["Ines", "Keiko", "Quinn", "Rania"], "missed_by": [], "secret_witnesses": []}]`

## plan-L4-008 (classic, seed 1540013)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Dalia, Keiko, Luca, Quinn, Farah, Zoltan, Chidi and Nadim share a house. The kitchen has four closed containers that nobody can see into: the black trunk, the wicker basket, the leather bag and the red box. This is what happened, in order.
1. Dalia, Keiko, Luca, Quinn, Farah, Zoltan, Chidi and Nadim are in the kitchen. Zoltan takes a token out of a pocket and puts it in the red box.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the kitchen see and hear everything that happens there, unless the story says that a person missed it. People outside the kitchen see and hear nothing of it, unless the story says so.
- Everyone in the kitchen can see who else is in the kitchen.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the token to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the kitchen, which shows where the token really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the kitchen that the token is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the token is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the kitchen at that step, NAME included. "missed_by" lists people in the kitchen who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the kitchen who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the kitchen freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["black trunk", "wicker basket", "leather bag", "red box"]. The names are: ["Chidi", "Dalia", "Farah", "Keiko", "Luca", "Nadim", "Quinn", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The token is really in the red box.
2. Dalia thinks the token is in the leather bag.
3. Keiko thinks the token is in the red box.
4. Luca thinks the token is in the red box.
5. Quinn thinks the token is in the red box.
6. Farah thinks the token is in the red box.
7. Zoltan thinks the token is in the red box.
8. Chidi thinks the token is in the red box.
9. Nadim thinks the token is in the red box.
10. Dalia thinks that Chidi thinks the token is in the leather bag.
11. Dalia thinks that Chidi thinks that Nadim thinks the token is in the leather bag.
12. Dalia thinks that Chidi thinks that Nadim thinks that Dalia thinks the token is in the black trunk.
13. Dalia thinks that Chidi thinks that Nadim thinks that Dalia thinks that Luca thinks the token is in the black trunk.
14. Dalia thinks that Chidi thinks that Nadim thinks that Dalia thinks that Luca thinks that Zoltan thinks the token is in the wicker basket.
15. Farah thinks that Luca thinks the token is in the red box.
16. Farah thinks that Luca thinks that Dalia thinks the token is in the black trunk.
17. Farah thinks that Luca thinks that Dalia thinks that Chidi thinks the token is in the black trunk.
18. Farah thinks that Luca thinks that Dalia thinks that Chidi thinks that Nadim thinks the token is in the black trunk.
19. Farah thinks that Luca thinks that Dalia thinks that Chidi thinks that Nadim thinks that Zoltan thinks the token is in the wicker basket.
20. Chidi thinks that Farah thinks the token is in the red box.
21. Chidi thinks that Farah thinks that Chidi thinks the token is in the red box.
22. Chidi thinks that Farah thinks that Chidi thinks that Luca thinks the token is in the red box.
23. Chidi thinks that Farah thinks that Chidi thinks that Luca thinks that Nadim thinks the token is in the red box.
24. Chidi thinks that Farah thinks that Chidi thinks that Luca thinks that Nadim thinks that Zoltan thinks the token is in the black trunk.
25. Nadim thinks that Farah thinks the token is in the red box.
26. Nadim thinks that Farah thinks that Luca thinks the token is in the red box.
27. Nadim thinks that Farah thinks that Luca thinks that Chidi thinks the token is in the red box.
28. Nadim thinks that Farah thinks that Luca thinks that Chidi thinks that Nadim thinks the token is in the red box.
29. Nadim thinks that Farah thinks that Luca thinks that Chidi thinks that Nadim thinks that Zoltan thinks the token is in the black trunk.
30. Keiko thinks that Dalia thinks the token is in the leather bag.
31. Keiko thinks that Dalia thinks that Chidi thinks the token is in the leather bag.
32. Keiko thinks that Dalia thinks that Chidi thinks that Nadim thinks the token is in the leather bag.
33. Keiko thinks that Dalia thinks that Chidi thinks that Nadim thinks that Luca thinks the token is in the leather bag.
34. Keiko thinks that Dalia thinks that Chidi thinks that Nadim thinks that Luca thinks that Farah thinks the token is in the black trunk.

Write at least 1 and at most 8 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "say", "who": "Luca", "value": "black trunk", "present": ["Chidi", "Dalia", "Farah", "Keiko", "Luca", "Nadim", "Zoltan"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Keiko", "value": "leather bag", "present": ["Chidi", "Dalia", "Keiko", "Luca", "Nadim", "Zoltan"], "missed_by": [], "secret_witnesses": ["Farah"]}, {"step": "change", "who": "Dalia", "value": "wicker basket", "present": ["Chidi", "Dalia", "Luca", "Nadim", "Zoltan"], "missed_by": [], "secret_witnesses": ["Farah"]}, {"step": "change", "who": "Chidi", "value": "leather bag", "present": ["Chidi", "Dalia", "Luca", "Nadim"], "missed_by": ["Dalia"], "secret_witnesses": []}, {"step": "change", "who": "Nadim", "value": "black trunk", "present": ["Chidi", "Dalia", "Farah", "Luca", "Nadim", "Quinn"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Nadim", "to": "Keiko", "value": "red box", "secret_readers": ["Zoltan"]}, {"step": "change", "who": "Quinn", "value": "leather bag", "present": ["Chidi", "Farah", "Luca", "Nadim", "Quinn"], "missed_by": [], "secret_witnesses": ["Dalia"]}, {"step": "change", "who": "Quinn", "value": "red box", "present": ["Chidi", "Farah", "Luca", "Nadim", "Quinn"], "missed_by": [], "secret_witnesses": []}]`

## plan-L4-009 (workplace, seed 1540014)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Soren, Hana, Oksana, Rania, Luca, Keiko, Viktor and Bruno work on the same team. This is what happened, in order.
1. Call with Soren, Hana, Oksana, Rania, Luca, Keiko, Viktor and Bruno: Keiko sets the product release for Friday.

Rules of the scene:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Thursday", "Wednesday", "Friday", "Tuesday"]. The names are: ["Bruno", "Hana", "Keiko", "Luca", "Oksana", "Rania", "Soren", "Viktor"].

Targets. After your last step, all of these must be true:
1. The product release is really set for Thursday.
2. Soren thinks the product release is set for Thursday.
3. Hana thinks the product release is set for Thursday.
4. Oksana thinks the product release is set for Thursday.
5. Rania thinks the product release is set for Thursday.
6. Luca thinks the product release is set for Thursday.
7. Keiko thinks the product release is set for Thursday.
8. Viktor thinks the product release is set for Thursday.
9. Bruno thinks the product release is set for Thursday.
10. Bruno thinks that Viktor thinks the product release is set for Thursday.
11. Bruno thinks that Viktor thinks that Luca thinks the product release is set for Thursday.
12. Bruno thinks that Viktor thinks that Luca thinks that Rania thinks the product release is set for Thursday.
13. Bruno thinks that Viktor thinks that Luca thinks that Rania thinks that Bruno thinks the product release is set for Thursday.
14. Bruno thinks that Viktor thinks that Luca thinks that Rania thinks that Bruno thinks that Hana thinks the product release is set for Friday.
15. Oksana thinks that Keiko thinks the product release is set for Wednesday.
16. Oksana thinks that Keiko thinks that Rania thinks the product release is set for Wednesday.
17. Oksana thinks that Keiko thinks that Rania thinks that Soren thinks the product release is set for Wednesday.
18. Oksana thinks that Keiko thinks that Rania thinks that Soren thinks that Bruno thinks the product release is set for Wednesday.
19. Oksana thinks that Keiko thinks that Rania thinks that Soren thinks that Bruno thinks that Viktor thinks the product release is set for Friday.
20. Keiko thinks that Viktor thinks the product release is set for Thursday.
21. Keiko thinks that Viktor thinks that Rania thinks the product release is set for Thursday.
22. Keiko thinks that Viktor thinks that Rania thinks that Bruno thinks the product release is set for Thursday.
23. Keiko thinks that Viktor thinks that Rania thinks that Bruno thinks that Rania thinks the product release is set for Thursday.
24. Keiko thinks that Viktor thinks that Rania thinks that Bruno thinks that Rania thinks that Hana thinks the product release is set for Friday.
25. Rania thinks that Viktor thinks the product release is set for Thursday.
26. Rania thinks that Viktor thinks that Bruno thinks the product release is set for Thursday.
27. Rania thinks that Viktor thinks that Bruno thinks that Soren thinks the product release is set for Thursday.
28. Rania thinks that Viktor thinks that Bruno thinks that Soren thinks that Keiko thinks the product release is set for Thursday.
29. Rania thinks that Viktor thinks that Bruno thinks that Soren thinks that Keiko thinks that Hana thinks the product release is set for Friday.
30. Soren thinks that Viktor thinks the product release is set for Thursday.
31. Soren thinks that Viktor thinks that Keiko thinks the product release is set for Thursday.
32. Soren thinks that Viktor thinks that Keiko thinks that Soren thinks the product release is set for Thursday.
33. Soren thinks that Viktor thinks that Keiko thinks that Soren thinks that Luca thinks the product release is set for Thursday.
34. Soren thinks that Viktor thinks that Keiko thinks that Soren thinks that Luca thinks that Hana thinks the product release is set for Friday.

Write at least 1 and at most 7 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Luca", "value": "Wednesday", "present": ["Bruno", "Hana", "Keiko", "Luca", "Rania", "Soren"], "missed_by": ["Soren"], "secret_witnesses": ["Oksana"]}, {"step": "change", "who": "Soren", "value": "Friday", "present": ["Bruno", "Hana", "Keiko", "Luca", "Rania", "Soren"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Viktor", "to": "Oksana", "value": "Thursday", "secret_readers": []}, {"step": "change", "who": "Luca", "value": "Wednesday", "present": ["Bruno", "Hana", "Luca", "Rania", "Soren"], "missed_by": ["Bruno"], "secret_witnesses": []}, {"step": "change", "who": "Soren", "value": "Thursday", "present": ["Bruno", "Keiko", "Rania", "Soren"], "missed_by": ["Bruno"], "secret_witnesses": ["Luca"]}, {"step": "check", "who": "Soren", "present": ["Bruno", "Keiko", "Luca", "Rania", "Soren", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Bruno", "to": "Hana", "value": "Thursday", "secret_readers": ["Keiko"]}]`

## explain-L1-000 (classic, seed 1710004)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the cellar see and hear everything that happens there, unless the story says that a person missed it. People outside the cellar see and hear nothing of it, unless the story says so.
- Everyone in the cellar can see who else is in the cellar.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Yara, Quinn, Hana and Zoltan share a house. The cellar has four closed containers that nobody can see into: the leather bag, the white cabinet, the grey locker and the green cupboard. This is what happened, in order.
1. Yara, Quinn, Hana and Zoltan are in the cellar. Zoltan takes a thimble out of a pocket and puts it in the grey locker.
2. Yara, Hana and Zoltan are in the cellar. Hana moves the thimble to the white cabinet. Quinn is outside but watches all of this through the window. Nobody knows that Quinn is watching.
3. Hana sends Quinn a private text message: “The thimble is in the white cabinet.”
4. Yara and Hana are in the cellar. Yara moves the thimble to the green cupboard. Zoltan is outside but watches all of this through the window. Nobody knows that Zoltan is watching.
5. Yara and Hana are in the cellar. Hana moves the thimble to the leather bag. Quinn is outside but watches all of this through the window. Nobody knows that Quinn is watching.
6. [A step is missing here.]
7. Zoltan sends Quinn a private text message: “The thimble is in the leather bag.”

Facts at the end of the story:
1. The thimble is really in the leather bag.
2. Zoltan thinks that Yara thinks the thimble is in the green cupboard.
3. Hana thinks that Zoltan thinks the thimble is in the leather bag.
4. Hana thinks that Quinn thinks the thimble is in the white cabinet.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the thimble to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the cellar, which shows where the thimble really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the cellar that the thimble is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the thimble is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the cellar at that step, NAME included. "missed_by" lists people in the cellar who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the cellar who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the cellar freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["leather bag", "white cabinet", "grey locker", "green cupboard"]. The names are: ["Hana", "Quinn", "Yara", "Zoltan"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Hana", "to": "Zoltan", "value": "leather bag", "secret_readers": []}]`

## explain-L1-001 (workplace, seed 1710005)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Jonas, Quinn, Nadim and Xavier work on the same team. This is what happened, in order.
1. Call with Jonas, Quinn, Nadim and Xavier: Nadim picks Sablewood as the packaging supplier.
2. Call with Jonas, Quinn and Nadim: Nadim switches the packaging supplier to Ironbridge. Jonas is on the call but has stepped away from the desk and misses this. Nobody realises that Jonas missed it.
3. Nadim sends Xavier a direct message: “The packaging supplier is Ironbridge.”
4. Call with Jonas, Quinn and Nadim: Quinn opens the supplier register and reads it out: “The packaging supplier is Ironbridge.” Nadim is on the call but has stepped away from the desk and misses this. Nobody realises that Nadim missed it. Xavier is not on the call but secretly listens in, and can see who is on it. Nobody knows that Xavier is listening.
5. [A step is missing here.]
6. Nadim sends Quinn a direct message: “The packaging supplier is Sablewood.”
7. Call with Quinn and Nadim: Nadim switches the packaging supplier to Brightwater. Jonas is not on the call but secretly listens in, and can see who is on it. Nobody knows that Jonas is listening.

Facts at the end of the story:
1. The packaging supplier is really Brightwater.
2. Nadim thinks that Xavier thinks the packaging supplier is Ironbridge.
3. Xavier thinks that Jonas thinks the packaging supplier is Sablewood.
4. Quinn thinks that Jonas thinks the packaging supplier is Ironbridge.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME switches the packaging supplier to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the supplier register and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the packaging supplier is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the packaging supplier is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Brightwater", "Ironbridge", "Halcyon", "Sablewood"]. The names are: ["Jonas", "Nadim", "Quinn", "Xavier"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Nadim", "value": "Sablewood", "present": ["Jonas", "Nadim"], "missed_by": [], "secret_witnesses": ["Xavier"]}]`

## explain-L1-002 (classic, seed 1710006)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the pantry see and hear everything that happens there, unless the story says that a person missed it. People outside the pantry see and hear nothing of it, unless the story says so.
- Everyone in the pantry can see who else is in the pantry.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Wanjiru, Oksana, Farah and Mirela share a house. The pantry has four closed containers that nobody can see into: the wicker basket, the red box, the blue drawer and the leather bag. This is what happened, in order.
1. Wanjiru, Oksana, Farah and Mirela are in the pantry. Mirela takes a marble out of a pocket and puts it in the red box.
2. Wanjiru, Farah and Mirela are in the pantry. Wanjiru moves the marble to the wicker basket. Oksana is outside but watches all of this through the window. Nobody knows that Oksana is watching.
3. Farah sends Oksana a private text message: “The marble is in the wicker basket.”
4. Farah and Mirela are in the pantry. Mirela moves the marble to the leather bag. Farah is in the pantry but is absorbed in a phone and does not notice this. Nobody realises that Farah missed it.
5. Wanjiru sends Oksana a private text message: “The marble is in the wicker basket.”
6. [A step is missing here.]
7. Mirela wants to mislead Oksana, so Mirela sends Oksana a private text message: “The marble is in the wicker basket.”

Facts at the end of the story:
1. The marble is really in the blue drawer.
2. Wanjiru thinks that Mirela thinks the marble is in the blue drawer.
3. Mirela thinks that Farah thinks the marble is in the blue drawer.
4. Farah thinks that Mirela thinks the marble is in the wicker basket.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the marble to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the pantry, which shows where the marble really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the pantry that the marble is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the marble is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the pantry at that step, NAME included. "missed_by" lists people in the pantry who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the pantry who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the pantry freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["wicker basket", "red box", "blue drawer", "leather bag"]. The names are: ["Farah", "Mirela", "Oksana", "Wanjiru"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Wanjiru", "value": "blue drawer", "present": ["Farah", "Mirela", "Wanjiru"], "missed_by": ["Farah"], "secret_witnesses": []}]`

## explain-L1-003 (workplace, seed 1710007)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Wanjiru, Xavier, Amara and Luca work on the same team. This is what happened, in order.
1. Call with Wanjiru, Xavier, Amara and Luca: Luca picks Sablewood as the packaging supplier.
2. Call with Wanjiru, Xavier, Amara and Luca: Wanjiru switches the packaging supplier to Halcyon.
3. [A step is missing here.]
4. Amara sends Luca a direct message: “The packaging supplier is Sablewood.”
5. Wanjiru sends Luca a direct message: “The packaging supplier is Sablewood.”
6. Xavier sends Luca a direct message: “The packaging supplier is Sablewood.”
7. Call with Wanjiru and Amara: Amara switches the packaging supplier to Ironbridge. Wanjiru is on the call but has stepped away from the desk and misses this. Nobody realises that Wanjiru missed it.

Facts at the end of the story:
1. The packaging supplier is really Ironbridge.
2. Amara thinks that Xavier thinks the packaging supplier is Sablewood.
3. Xavier thinks that Amara thinks the packaging supplier is Sablewood.
4. Xavier thinks that Wanjiru thinks the packaging supplier is Sablewood.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME switches the packaging supplier to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the supplier register and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the packaging supplier is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the packaging supplier is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Ironbridge", "Halcyon", "Sablewood", "Northwind"]. The names are: ["Amara", "Luca", "Wanjiru", "Xavier"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Xavier", "value": "Sablewood", "present": ["Amara", "Wanjiru", "Xavier"], "missed_by": [], "secret_witnesses": ["Luca"]}]`

## explain-L1-004 (classic, seed 1710009)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the study see and hear everything that happens there, unless the story says that a person missed it. People outside the study see and hear nothing of it, unless the story says so.
- Everyone in the study can see who else is in the study.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Zoltan, Tariq, Keiko and Pablo share a house. The study has four closed containers that nobody can see into: the leather bag, the black trunk, the canvas sack and the wicker basket. This is what happened, in order.
1. Zoltan, Tariq, Keiko and Pablo are in the study. Keiko takes a padlock out of a pocket and puts it in the leather bag.
2. Zoltan, Tariq, Keiko and Pablo are in the study. Pablo moves the padlock to the black trunk.
3. Zoltan, Tariq and Pablo are in the study. Pablo moves the padlock to the canvas sack.
4. Zoltan, Tariq, Keiko and Pablo are in the study. Keiko opens every container in full view of the study, showing that the padlock is in the canvas sack.
5. [A step is missing here.]
6. Zoltan sends Tariq a private text message: “The padlock is in the wicker basket.”
7. Pablo sends Tariq a private text message: “The padlock is in the wicker basket.”

Facts at the end of the story:
1. The padlock is really in the wicker basket.
2. Tariq thinks that Keiko thinks the padlock is in the wicker basket.
3. Keiko thinks that Pablo thinks the padlock is in the wicker basket.
4. Keiko thinks that Tariq thinks the padlock is in the canvas sack.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the padlock to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the study, which shows where the padlock really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the study that the padlock is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the padlock is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the study at that step, NAME included. "missed_by" lists people in the study who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the study who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the study freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["leather bag", "black trunk", "canvas sack", "wicker basket"]. The names are: ["Keiko", "Pablo", "Tariq", "Zoltan"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Keiko", "value": "wicker basket", "present": ["Keiko", "Pablo", "Zoltan"], "missed_by": [], "secret_witnesses": ["Tariq"]}]`

## explain-L1-005 (workplace, seed 1710010)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Uma, Zoltan, Dalia and Bruno work on the same team. This is what happened, in order.
1. Call with Uma, Zoltan, Dalia and Bruno: Uma sets the product release for Thursday.
2. Call with Uma, Zoltan and Dalia: Dalia moves the product release to Wednesday.
3. Call with Uma and Dalia: Dalia moves the product release to Tuesday. Bruno is not on the call but secretly listens in, and can see who is on it. Nobody knows that Bruno is listening.
4. Call with Uma and Dalia: Uma moves the product release to Friday.
5. [A step is missing here.]
6. Dalia sends Zoltan a direct message: “The product release is set for Tuesday.”
7. Dalia sends Uma a direct message: “The product release is set for Tuesday.”

Facts at the end of the story:
1. The product release is really set for Tuesday.
2. Dalia thinks that Bruno thinks the product release is set for Tuesday.
3. Zoltan thinks that Bruno thinks the product release is set for Thursday.
4. Uma thinks that Bruno thinks the product release is set for Thursday.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Friday", "Thursday", "Wednesday", "Tuesday"]. The names are: ["Bruno", "Dalia", "Uma", "Zoltan"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Dalia", "value": "Tuesday", "present": ["Bruno", "Dalia"], "missed_by": [], "secret_witnesses": []}]`

## explain-L1-006 (classic, seed 1710011)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the pantry see and hear everything that happens there, unless the story says that a person missed it. People outside the pantry see and hear nothing of it, unless the story says so.
- Everyone in the pantry can see who else is in the pantry.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Bruno, Pablo, Emeka and Quinn share a house. The pantry has four closed containers that nobody can see into: the red box, the leather bag, the black trunk and the white cabinet. This is what happened, in order.
1. Bruno, Pablo, Emeka and Quinn are in the pantry. Quinn takes a compass out of a pocket and puts it in the black trunk.
2. Bruno and Pablo are in the pantry. Pablo moves the compass to the red box.
3. Bruno wants to mislead Emeka, so Bruno sends Emeka a private text message: “The compass is in the white cabinet.” Quinn secretly reads this message on Emeka's phone. Neither Bruno nor Emeka ever knows that Quinn read it.
4. Bruno is alone in the pantry. Bruno moves the compass to the leather bag. Emeka is outside but watches all of this through the window. Nobody knows that Emeka is watching.
5. Bruno is alone in the pantry. Bruno moves the compass to the black trunk. Pablo is outside but watches all of this through the window. Nobody knows that Pablo is watching.
6. [A step is missing here.]
7. Bruno, Pablo and Quinn are in the pantry. Pablo moves the compass to the white cabinet.

Facts at the end of the story:
1. The compass is really in the white cabinet.
2. Emeka thinks that Quinn thinks the compass is in the red box.
3. Emeka thinks the compass is in the leather bag.
4. Bruno thinks that Emeka thinks the compass is in the white cabinet.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the compass to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the pantry, which shows where the compass really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the pantry that the compass is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the compass is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the pantry at that step, NAME included. "missed_by" lists people in the pantry who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the pantry who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the pantry freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["red box", "leather bag", "black trunk", "white cabinet"]. The names are: ["Bruno", "Emeka", "Pablo", "Quinn"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Emeka", "to": "Quinn", "value": "red box", "secret_readers": []}]`

## explain-L1-007 (workplace, seed 1710012)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Soren, Viktor, Emeka and Mirela work on the same team. This is what happened, in order.
1. Call with Soren, Viktor, Emeka and Mirela: Soren fixes Turin as the place for the team offsite.
2. Call with Viktor and Emeka: Emeka moves the team offsite to Ghent.
3. Call with Viktor and Emeka: Viktor moves the team offsite to Turin.
4. Emeka, working alone, moves the team offsite to Leeds and tells nobody.
5. Emeka, working alone, moves the team offsite to Ghent and tells nobody.
6. [A step is missing here.]
7. Emeka, working alone, moves the team offsite to Graz and tells nobody.

Facts at the end of the story:
1. The team offsite is really in Graz.
2. Soren thinks that Viktor thinks the team offsite is in Graz.
3. Viktor thinks that Emeka thinks the team offsite is in Graz.
4. Mirela thinks that Viktor thinks the team offsite is in Turin.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the team offsite to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the travel plan and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the team offsite is in VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the team offsite is in VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Turin", "Leeds", "Ghent", "Graz"]. The names are: ["Emeka", "Mirela", "Soren", "Viktor"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Emeka", "to": "Viktor", "value": "Graz", "secret_readers": ["Soren"]}]`

## explain-L1-008 (classic, seed 1710013)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the greenhouse see and hear everything that happens there, unless the story says that a person missed it. People outside the greenhouse see and hear nothing of it, unless the story says so.
- Everyone in the greenhouse can see who else is in the greenhouse.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Soren, Quinn, Bruno and Viktor share a house. The greenhouse has four closed containers that nobody can see into: the wicker basket, the black trunk, the leather bag and the grey locker. This is what happened, in order.
1. Soren, Quinn, Bruno and Viktor are in the greenhouse. Viktor takes a torch out of a pocket and puts it in the wicker basket.
2. Soren, Quinn and Viktor are in the greenhouse. Soren moves the torch to the black trunk.
3. Soren, Quinn and Viktor are in the greenhouse. Soren moves the torch to the wicker basket.
4. Soren, Quinn and Viktor are in the greenhouse. Soren moves the torch to the grey locker. Bruno is outside but watches all of this through the window. Nobody knows that Bruno is watching.
5. [A step is missing here.]
6. Soren sends Viktor a private text message: “The torch is in the leather bag.” Quinn secretly reads this message on Viktor's phone. Neither Soren nor Viktor ever knows that Quinn read it.
7. Soren is alone in the greenhouse. Soren moves the torch to the grey locker.

Facts at the end of the story:
1. The torch is really in the grey locker.
2. Bruno thinks the torch is in the grey locker.
3. Soren thinks that Quinn thinks the torch is in the grey locker.
4. Soren thinks that Bruno thinks the torch is in the wicker basket.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the torch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the greenhouse, which shows where the torch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the greenhouse that the torch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the torch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the greenhouse at that step, NAME included. "missed_by" lists people in the greenhouse who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the greenhouse who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the greenhouse freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["wicker basket", "black trunk", "leather bag", "grey locker"]. The names are: ["Bruno", "Quinn", "Soren", "Viktor"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Soren", "value": "leather bag", "present": ["Soren"], "missed_by": [], "secret_witnesses": []}]`

## explain-L1-009 (workplace, seed 1710014)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Keiko, Mirela, Goran and Bruno work on the same team. This is what happened, in order.
1. Call with Keiko, Mirela, Goran and Bruno: Bruno picks Brightwater as the packaging supplier.
2. Call with Mirela, Goran and Bruno: Goran switches the packaging supplier to Ironbridge.
3. Call with Mirela, Goran and Bruno: Goran opens the supplier register and reads it out: “The packaging supplier is Ironbridge.” Keiko is not on the call but secretly listens in, and can see who is on it. Nobody knows that Keiko is listening.
4. Call with Mirela, Goran and Bruno: Goran switches the packaging supplier to Brightwater.
5. Call with Keiko, Mirela, Goran and Bruno: Keiko switches the packaging supplier to Ironbridge.
6. [A step is missing here.]
7. Call with Mirela, Goran and Bruno: Mirela switches the packaging supplier to Ironbridge.

Facts at the end of the story:
1. The packaging supplier is really Ironbridge.
2. Mirela thinks that Keiko thinks the packaging supplier is Sablewood.
3. Keiko thinks that Bruno thinks the packaging supplier is Sablewood.
4. Goran thinks that Keiko thinks the packaging supplier is Sablewood.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME switches the packaging supplier to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the supplier register and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the packaging supplier is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the packaging supplier is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Ironbridge", "Brightwater", "Halcyon", "Sablewood"]. The names are: ["Bruno", "Goran", "Keiko", "Mirela"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Goran", "value": "Sablewood", "present": ["Bruno", "Goran", "Keiko", "Mirela"], "missed_by": [], "secret_witnesses": []}]`

## explain-L2-000 (classic, seed 1720001)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the workshop see and hear everything that happens there, unless the story says that a person missed it. People outside the workshop see and hear nothing of it, unless the story says so.
- Everyone in the workshop can see who else is in the workshop.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Bruno, Hana, Goran, Pablo and Luca share a house. The workshop has four closed containers that nobody can see into: the green cupboard, the leather bag, the wicker basket and the red box. This is what happened, in order.
1. Bruno, Hana, Goran, Pablo and Luca are in the workshop. Goran takes a medal out of a pocket and puts it in the wicker basket.
2. Bruno, Goran, Pablo and Luca are in the workshop. Pablo moves the medal to the green cupboard.
3. Luca sends Hana a private text message: “The medal is in the green cupboard.”
4. Bruno, Goran, Pablo and Luca are in the workshop. Pablo moves the medal to the red box.
5. [A step is missing here.]
6. Hana wants to mislead Goran, so Hana sends Goran a private text message: “The medal is in the red box.”
7. Pablo sends Hana a private text message: “The medal is in the red box.” Goran secretly reads this message on Hana's phone. Neither Pablo nor Hana ever knows that Goran read it.
8. Hana sends Luca a private text message: “The medal is in the red box.”
9. Bruno, Goran, Pablo and Luca are in the workshop. Goran moves the medal to the wicker basket. Hana is outside but watches all of this through the window. Nobody knows that Hana is watching.

Facts at the end of the story:
1. The medal is really in the wicker basket.
2. Hana thinks that Bruno thinks that Hana thinks the medal is in the red box.
3. Luca thinks that Hana thinks that Bruno thinks the medal is in the wicker basket.
4. Goran thinks that Hana thinks that Bruno thinks the medal is in the red box.
5. Pablo thinks that Hana thinks that Bruno thinks the medal is in the wicker basket.
6. Goran thinks that Hana thinks that Luca thinks the medal is in the wicker basket.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the medal to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the workshop, which shows where the medal really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the workshop that the medal is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the medal is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the workshop at that step, NAME included. "missed_by" lists people in the workshop who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the workshop who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the workshop freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["green cupboard", "leather bag", "wicker basket", "red box"]. The names are: ["Bruno", "Goran", "Hana", "Luca", "Pablo"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Hana", "to": "Bruno", "value": "red box", "secret_readers": ["Goran"]}]`

## explain-L2-001 (workplace, seed 1720003)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Tariq, Luca, Hana, Goran and Viktor work on the same team. This is what happened, in order.
1. Call with Tariq, Luca, Hana, Goran and Viktor: Luca sets the product release for Monday.
2. Call with Tariq, Hana, Goran and Viktor: Goran moves the product release to Friday.
3. Call with Tariq, Hana, Goran and Viktor: Tariq moves the product release to Tuesday. Luca is not on the call but secretly listens in, and can see who is on it. Nobody knows that Luca is listening.
4. Goran sends Luca a direct message: “The product release is set for Tuesday.”
5. Call with Tariq, Hana, Goran and Viktor: Goran moves the product release to Monday.
6. Call with Tariq, Hana and Goran: Tariq moves the product release to Tuesday.
7. [A step is missing here.]
8. Hana sends Luca a direct message: “The product release is set for Tuesday.” Tariq secretly reads this message on Luca's screen. Neither Hana nor Luca ever knows that Tariq read it.
9. Goran wants to mislead Viktor, so Goran sends Viktor a direct message: “The product release is set for Friday.”

Facts at the end of the story:
1. The product release is really set for Tuesday.
2. Hana thinks that Viktor thinks the product release is set for Friday.
3. Luca thinks that Viktor thinks the product release is set for Tuesday.
4. Tariq thinks that Hana thinks that Viktor thinks the product release is set for Monday.
5. Hana thinks that Tariq thinks the product release is set for Tuesday.
6. Hana thinks that Viktor thinks that Luca thinks the product release is set for Monday.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Monday", "Friday", "Wednesday", "Tuesday"]. The names are: ["Goran", "Hana", "Luca", "Tariq", "Viktor"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Hana", "to": "Viktor", "value": "Friday", "secret_readers": []}]`

## explain-L2-002 (classic, seed 1720005)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the pantry see and hear everything that happens there, unless the story says that a person missed it. People outside the pantry see and hear nothing of it, unless the story says so.
- Everyone in the pantry can see who else is in the pantry.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Nadim, Dalia, Uma, Chidi and Yara share a house. The pantry has four closed containers that nobody can see into: the green cupboard, the black trunk, the canvas sack and the leather bag. This is what happened, in order.
1. Nadim, Dalia, Uma, Chidi and Yara are in the pantry. Dalia takes a magnet out of a pocket and puts it in the canvas sack.
2. [A step is missing here.]
3. Nadim sends Yara a private text message: “The magnet is in the green cupboard.” Uma secretly reads this message on Yara's phone. Neither Nadim nor Yara ever knows that Uma read it.
4. Yara sends Dalia a private text message: “The magnet is in the green cupboard.”
5. Nadim and Chidi are in the pantry. Nadim moves the magnet to the black trunk.
6. Nadim is alone in the pantry. Nadim moves the magnet to the leather bag.
7. Nadim is alone in the pantry. Nadim moves the magnet to the black trunk.
8. Nadim sends Uma a private text message: “The magnet is in the black trunk.” Chidi secretly reads this message on Uma's phone. Neither Nadim nor Uma ever knows that Chidi read it.
9. Nadim and Dalia are in the pantry. Dalia moves the magnet to the green cupboard. Yara is outside but watches all of this through the window. Nobody knows that Yara is watching.

Facts at the end of the story:
1. The magnet is really in the green cupboard.
2. Chidi thinks that Dalia thinks that Uma thinks the magnet is in the green cupboard.
3. Dalia thinks that Chidi thinks that Nadim thinks the magnet is in the green cupboard.
4. Nadim thinks that Uma thinks that Yara thinks the magnet is in the canvas sack.
5. Yara thinks that Chidi thinks the magnet is in the canvas sack.
6. Uma thinks that Dalia thinks the magnet is in the green cupboard.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the magnet to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the pantry, which shows where the magnet really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the pantry that the magnet is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the magnet is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the pantry at that step, NAME included. "missed_by" lists people in the pantry who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the pantry who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the pantry freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["green cupboard", "black trunk", "canvas sack", "leather bag"]. The names are: ["Chidi", "Dalia", "Nadim", "Uma", "Yara"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Nadim", "value": "green cupboard", "present": ["Chidi", "Dalia", "Nadim", "Uma"], "missed_by": [], "secret_witnesses": []}]`

## explain-L2-003 (workplace, seed 1720007)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Chidi, Tariq, Pablo, Viktor and Uma work on the same team. This is what happened, in order.
1. Call with Chidi, Tariq, Pablo, Viktor and Uma: Chidi sets the discount on the Fenwick quote at 5%.
2. Call with Chidi, Tariq and Pablo: Chidi changes the discount on the Fenwick quote to 15%. Viktor is not on the call but secretly listens in, and can see who is on it. Nobody knows that Viktor is listening.
3. Chidi sends Viktor a direct message: “The discount on the Fenwick quote is 15%.”
4. Pablo sends Uma a direct message: “The discount on the Fenwick quote is 15%.”
5. Tariq sends Uma a direct message: “The discount on the Fenwick quote is 15%.”
6. Call with Chidi, Tariq and Pablo: Tariq changes the discount on the Fenwick quote to 5%. Viktor is not on the call but secretly listens in, and can see who is on it. Nobody knows that Viktor is listening.
7. [A step is missing here.]
8. Call with Tariq and Pablo: Tariq changes the discount on the Fenwick quote to 5%. Pablo is on the call but has stepped away from the desk and misses this. Nobody realises that Pablo missed it. Viktor is not on the call but secretly listens in, and can see who is on it. Nobody knows that Viktor is listening.
9. Tariq, working alone, changes the discount on the Fenwick quote to 15% and tells nobody. Viktor secretly watches Tariq's screen as this happens. Nobody knows that Viktor is watching.

Facts at the end of the story:
1. The discount on the Fenwick quote is really 15%.
2. Chidi thinks that Pablo thinks that Tariq thinks the discount on the Fenwick quote is 10%.
3. Tariq thinks that Chidi thinks that Pablo thinks the discount on the Fenwick quote is 10%.
4. Viktor thinks that Chidi thinks that Tariq thinks the discount on the Fenwick quote is 5%.
5. Tariq thinks that Chidi thinks that Uma thinks the discount on the Fenwick quote is 5%.
6. Uma thinks that Pablo thinks that Tariq thinks the discount on the Fenwick quote is 5%.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME changes the discount on the Fenwick quote to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the quote record and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the discount on the Fenwick quote is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the discount on the Fenwick quote is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["25%", "15%", "10%", "5%"]. The names are: ["Chidi", "Pablo", "Tariq", "Uma", "Viktor"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Pablo", "value": "10%", "present": ["Chidi", "Pablo", "Tariq"], "missed_by": [], "secret_witnesses": []}]`

## explain-L2-004 (classic, seed 1720008)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the garage see and hear everything that happens there, unless the story says that a person missed it. People outside the garage see and hear nothing of it, unless the story says so.
- Everyone in the garage can see who else is in the garage.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Amara, Hana, Yara, Oksana and Tariq share a house. The garage has four closed containers that nobody can see into: the green cupboard, the wicker basket, the black trunk and the red box. This is what happened, in order.
1. Amara, Hana, Yara, Oksana and Tariq are in the garage. Hana takes a thimble out of a pocket and puts it in the black trunk.
2. Amara, Hana, Oksana and Tariq are in the garage. Hana moves the thimble to the wicker basket.
3. Amara, Oksana and Tariq are in the garage. Oksana moves the thimble to the red box. Hana is outside but watches all of this through the window. Nobody knows that Hana is watching.
4. Amara, Oksana and Tariq are in the garage. Tariq moves the thimble to the green cupboard. Oksana is in the garage but is absorbed in a phone and does not notice this. Nobody realises that Oksana missed it.
5. Amara, Oksana and Tariq are in the garage. Amara moves the thimble to the black trunk.
6. Amara, Oksana and Tariq are in the garage. Amara moves the thimble to the red box.
7. Hana wants to mislead Yara, so Hana sends Yara a private text message: “The thimble is in the green cupboard.”
8. [A step is missing here.]
9. Yara wants to mislead Amara, so Yara sends Amara a private text message: “The thimble is in the wicker basket.”

Facts at the end of the story:
1. The thimble is really in the wicker basket.
2. Tariq thinks that Amara thinks that Oksana thinks the thimble is in the wicker basket.
3. Amara thinks that Tariq thinks the thimble is in the wicker basket.
4. Hana thinks that Amara thinks that Oksana thinks the thimble is in the red box.
5. Amara thinks that Yara thinks that Oksana thinks the thimble is in the black trunk.
6. Oksana thinks that Tariq thinks that Oksana thinks the thimble is in the wicker basket.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the thimble to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the garage, which shows where the thimble really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the garage that the thimble is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the thimble is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the garage at that step, NAME included. "missed_by" lists people in the garage who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the garage who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the garage freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["green cupboard", "wicker basket", "black trunk", "red box"]. The names are: ["Amara", "Hana", "Oksana", "Tariq", "Yara"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Oksana", "value": "wicker basket", "present": ["Amara", "Oksana", "Tariq"], "missed_by": [], "secret_witnesses": []}]`

## explain-L2-005 (workplace, seed 1720009)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Bruno, Rania, Zoltan, Wanjiru and Keiko work on the same team. This is what happened, in order.
1. Call with Bruno, Rania, Zoltan, Wanjiru and Keiko: Keiko books the client workshop into Room Fir.
2. Call with Rania, Zoltan, Wanjiru and Keiko: Zoltan moves the client workshop to Room Elm. Wanjiru is on the call but has stepped away from the desk and misses this. Nobody realises that Wanjiru missed it.
3. [A step is missing here.]
4. Keiko wants to mislead Bruno, so Keiko sends Bruno a direct message: “The client workshop is booked in Room Elm.”
5. Zoltan sends Bruno a direct message: “The client workshop is booked in Room Birch.”
6. Bruno sends Keiko a direct message: “The client workshop is booked in Room Birch.”
7. Bruno sends Rania a direct message: “The client workshop is booked in Room Birch.” Keiko secretly reads this message on Rania's screen. Neither Bruno nor Rania ever knows that Keiko read it.
8. Call with Zoltan, Wanjiru and Keiko: Zoltan moves the client workshop to Room Elm.
9. Wanjiru sends Bruno a direct message: “The client workshop is booked in Room Elm.” Zoltan secretly reads this message on Bruno's screen. Neither Wanjiru nor Bruno ever knows that Zoltan read it.

Facts at the end of the story:
1. The client workshop is really booked in Room Elm.
2. Rania thinks that Wanjiru thinks that Rania thinks the client workshop is booked in Room Birch.
3. Wanjiru thinks that Keiko thinks that Rania thinks the client workshop is booked in Room Birch.
4. Rania thinks that Wanjiru thinks that Bruno thinks the client workshop is booked in Room Fir.
5. Bruno thinks that Rania thinks that Keiko thinks the client workshop is booked in Room Fir.
6. Zoltan thinks that Rania thinks that Zoltan thinks the client workshop is booked in Room Birch.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the client workshop to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the booking system and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the client workshop is booked in VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the client workshop is booked in VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Room Fir", "Room Dogwood", "Room Birch", "Room Elm"]. The names are: ["Bruno", "Keiko", "Rania", "Wanjiru", "Zoltan"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Keiko", "value": "Room Birch", "present": ["Keiko", "Rania", "Wanjiru", "Zoltan"], "missed_by": [], "secret_witnesses": []}]`

## explain-L2-006 (classic, seed 1720010)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the boathouse see and hear everything that happens there, unless the story says that a person missed it. People outside the boathouse see and hear nothing of it, unless the story says so.
- Everyone in the boathouse can see who else is in the boathouse.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Nadim, Amara, Goran, Quinn and Pablo share a house. The boathouse has four closed containers that nobody can see into: the grey locker, the leather bag, the white cabinet and the canvas sack. This is what happened, in order.
1. Nadim, Amara, Goran, Quinn and Pablo are in the boathouse. Amara takes a whistle out of a pocket and puts it in the grey locker.
2. [A step is missing here.]
3. Nadim, Amara and Quinn are in the boathouse. Nadim moves the whistle to the white cabinet.
4. Quinn wants to mislead Goran, so Quinn sends Goran a private text message: “The whistle is in the canvas sack.”
5. Nadim, Amara and Quinn are in the boathouse. Quinn moves the whistle to the leather bag. Amara is in the boathouse but is absorbed in a phone and does not notice this. Nobody realises that Amara missed it.
6. Nadim, Amara and Quinn are in the boathouse. Nadim moves the whistle to the canvas sack.
7. Goran sends Amara a private text message: “The whistle is in the canvas sack.” Pablo secretly reads this message on Amara's phone. Neither Goran nor Amara ever knows that Pablo read it.
8. Quinn sends Pablo a private text message: “The whistle is in the canvas sack.” Amara secretly reads this message on Pablo's phone. Neither Quinn nor Pablo ever knows that Amara read it.
9. Pablo sends Nadim a private text message: “The whistle is in the canvas sack.”

Facts at the end of the story:
1. The whistle is really in the canvas sack.
2. Goran thinks that Quinn thinks that Pablo thinks the whistle is in the leather bag.
3. Nadim thinks that Goran thinks that Amara thinks the whistle is in the leather bag.
4. Pablo thinks that Quinn thinks that Nadim thinks the whistle is in the leather bag.
5. Amara thinks that Goran thinks that Pablo thinks the whistle is in the leather bag.
6. Quinn thinks that Pablo thinks that Goran thinks the whistle is in the leather bag.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the whistle to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the boathouse, which shows where the whistle really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the boathouse that the whistle is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the whistle is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the boathouse at that step, NAME included. "missed_by" lists people in the boathouse who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the boathouse who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the boathouse freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["grey locker", "leather bag", "white cabinet", "canvas sack"]. The names are: ["Amara", "Goran", "Nadim", "Pablo", "Quinn"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Pablo", "value": "leather bag", "present": ["Amara", "Goran", "Nadim", "Pablo", "Quinn"], "missed_by": [], "secret_witnesses": []}]`

## explain-L2-007 (workplace, seed 1720011)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Tariq, Nadim, Oksana, Luca and Xavier work on the same team. This is what happened, in order.
1. Call with Tariq, Nadim, Oksana, Luca and Xavier: Xavier sets the product release for Wednesday.
2. [A step is missing here.]
3. Call with Tariq, Nadim, Luca and Xavier: Luca moves the product release to Thursday.
4. Call with Nadim, Luca and Xavier: Luca moves the product release to Tuesday.
5. Call with Nadim, Luca and Xavier: Nadim moves the product release to Friday. Tariq is not on the call but secretly listens in, and can see who is on it. Nobody knows that Tariq is listening.
6. Call with Nadim, Luca and Xavier: Luca moves the product release to Tuesday.
7. Luca wants to mislead Tariq, so Luca sends Tariq a direct message: “The product release is set for Wednesday.”
8. Xavier sends Tariq a direct message: “The product release is set for Tuesday.”
9. Call with Nadim, Oksana, Luca and Xavier: Nadim moves the product release to Friday. Oksana is on the call but has stepped away from the desk and misses this. Nobody realises that Oksana missed it.

Facts at the end of the story:
1. The product release is really set for Friday.
2. Xavier thinks that Oksana thinks that Tariq thinks the product release is set for Friday.
3. Oksana thinks that Nadim thinks that Luca thinks the product release is set for Friday.
4. Tariq thinks that Oksana thinks that Xavier thinks the product release is set for Friday.
5. Nadim thinks that Tariq thinks that Oksana thinks the product release is set for Friday.
6. Luca thinks that Oksana thinks that Tariq thinks the product release is set for Friday.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Wednesday", "Thursday", "Tuesday", "Friday"]. The names are: ["Luca", "Nadim", "Oksana", "Tariq", "Xavier"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Luca", "value": "Friday", "present": ["Luca", "Nadim", "Oksana", "Tariq", "Xavier"], "missed_by": [], "secret_witnesses": []}]`

## explain-L2-008 (classic, seed 1720012)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the cellar see and hear everything that happens there, unless the story says that a person missed it. People outside the cellar see and hear nothing of it, unless the story says so.
- Everyone in the cellar can see who else is in the cellar.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Pablo, Tariq, Xavier, Dalia and Quinn share a house. The cellar has four closed containers that nobody can see into: the canvas sack, the red box, the blue drawer and the leather bag. This is what happened, in order.
1. Pablo, Tariq, Xavier, Dalia and Quinn are in the cellar. Pablo takes a thimble out of a pocket and puts it in the leather bag.
2. Tariq, Xavier, Dalia and Quinn are in the cellar. Quinn moves the thimble to the red box.
3. Tariq wants to mislead Pablo, so Tariq sends Pablo a private text message: “The thimble is in the blue drawer.”
4. Dalia sends Pablo a private text message: “The thimble is in the red box.” Xavier secretly reads this message on Pablo's phone. Neither Dalia nor Pablo ever knows that Xavier read it.
5. Quinn sends Pablo a private text message: “The thimble is in the red box.”
6. Pablo, Tariq, Xavier and Dalia are in the cellar. Pablo says out loud to everyone in the cellar: “The thimble is in the red box.”
7. Pablo, Tariq, Xavier and Dalia are in the cellar. Tariq moves the thimble to the leather bag. Pablo is in the cellar but is absorbed in a phone and does not notice this. Nobody realises that Pablo missed it.
8. [A step is missing here.]
9. Pablo, Xavier and Dalia are in the cellar. Pablo moves the thimble to the leather bag.

Facts at the end of the story:
1. The thimble is really in the leather bag.
2. Tariq thinks that Dalia thinks that Xavier thinks the thimble is in the canvas sack.
3. Dalia thinks that Tariq thinks that Pablo thinks the thimble is in the canvas sack.
4. Quinn thinks that Dalia thinks that Xavier thinks the thimble is in the red box.
5. Tariq thinks that Quinn thinks that Xavier thinks the thimble is in the red box.
6. Xavier thinks that Tariq thinks that Pablo thinks the thimble is in the canvas sack.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the thimble to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the cellar, which shows where the thimble really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the cellar that the thimble is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the thimble is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the cellar at that step, NAME included. "missed_by" lists people in the cellar who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the cellar who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the cellar freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["canvas sack", "red box", "blue drawer", "leather bag"]. The names are: ["Dalia", "Pablo", "Quinn", "Tariq", "Xavier"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Tariq", "value": "canvas sack", "present": ["Dalia", "Pablo", "Tariq", "Xavier"], "missed_by": [], "secret_witnesses": []}]`

## explain-L2-009 (workplace, seed 1720014)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Viktor, Xavier, Keiko, Luca and Rania work on the same team. This is what happened, in order.
1. Call with Viktor, Xavier, Keiko, Luca and Rania: Rania sets the discount on the Fenwick quote at 5%.
2. [A step is missing here.]
3. Xavier wants to mislead Luca, so Xavier sends Luca a direct message: “The discount on the Fenwick quote is 10%.”
4. Viktor sends Luca a direct message: “The discount on the Fenwick quote is 15%.” Keiko secretly reads this message on Luca's screen. Neither Viktor nor Luca ever knows that Keiko read it.
5. Luca sends Xavier a direct message: “The discount on the Fenwick quote is 15%.”
6. Call with Xavier, Keiko and Rania: Xavier changes the discount on the Fenwick quote to 5%.
7. Xavier sends Viktor a direct message: “The discount on the Fenwick quote is 5%.”
8. Viktor sends Keiko a direct message: “The discount on the Fenwick quote is 5%.”
9. Call with Xavier, Keiko and Rania: Keiko changes the discount on the Fenwick quote to 20%.

Facts at the end of the story:
1. The discount on the Fenwick quote is really 20%.
2. Rania thinks that Xavier thinks that Viktor thinks the discount on the Fenwick quote is 15%.
3. Viktor thinks that Rania thinks that Keiko thinks the discount on the Fenwick quote is 15%.
4. Luca thinks that Xavier thinks that Keiko thinks the discount on the Fenwick quote is 5%.
5. Rania thinks that Luca thinks that Xavier thinks the discount on the Fenwick quote is 5%.
6. Xavier thinks that Keiko thinks that Viktor thinks the discount on the Fenwick quote is 15%.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME changes the discount on the Fenwick quote to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the quote record and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the discount on the Fenwick quote is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the discount on the Fenwick quote is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["20%", "10%", "15%", "5%"]. The names are: ["Keiko", "Luca", "Rania", "Viktor", "Xavier"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Xavier", "value": "15%", "present": ["Keiko", "Rania", "Viktor", "Xavier"], "missed_by": [], "secret_witnesses": []}]`

## explain-L3-000 (classic, seed 1730003)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the cellar see and hear everything that happens there, unless the story says that a person missed it. People outside the cellar see and hear nothing of it, unless the story says so.
- Everyone in the cellar can see who else is in the cellar.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Amara, Quinn, Yara, Xavier and Luca share a house. The cellar has four closed containers that nobody can see into: the black trunk, the grey locker, the green cupboard and the canvas sack. This is what happened, in order.
1. Amara, Quinn, Yara, Xavier and Luca are in the cellar. Amara takes a stopwatch out of a pocket and puts it in the black trunk.
2. Amara, Quinn, Yara and Xavier are in the cellar. Yara moves the stopwatch to the green cupboard. Luca is outside but watches all of this through the window. Nobody knows that Luca is watching.
3. Amara sends Luca a private text message: “The stopwatch is in the green cupboard.”
4. Quinn sends Luca a private text message: “The stopwatch is in the green cupboard.”
5. Amara, Quinn, Yara and Xavier are in the cellar. Quinn moves the stopwatch to the grey locker. Yara is in the cellar but is absorbed in a phone and does not notice this. Nobody realises that Yara missed it.
6. Amara, Quinn, Yara and Xavier are in the cellar. Amara opens every container in full view of the cellar, showing that the stopwatch is in the grey locker.
7. Amara, Quinn, Yara and Xavier are in the cellar. Quinn moves the stopwatch to the black trunk.
8. Amara, Quinn, Yara and Xavier are in the cellar. Quinn moves the stopwatch to the green cupboard. Luca is outside but watches all of this through the window. Nobody knows that Luca is watching.
9. Amara and Quinn are in the cellar. Amara moves the stopwatch to the black trunk.
10. [A step is missing here.]
11. Luca wants to mislead Xavier, so Luca sends Xavier a private text message: “The stopwatch is in the black trunk.”

Facts at the end of the story:
1. The stopwatch is really in the grey locker.
2. Luca thinks that Amara thinks that Luca thinks that Quinn thinks the stopwatch is in the grey locker.
3. Yara thinks that Luca thinks that Amara thinks the stopwatch is in the black trunk.
4. Xavier thinks that Luca thinks that Amara thinks that Quinn thinks the stopwatch is in the black trunk.
5. Luca thinks that Amara thinks that Yara thinks that Quinn thinks the stopwatch is in the green cupboard.
6. Luca thinks that Amara thinks that Luca thinks that Xavier thinks the stopwatch is in the black trunk.
7. Amara thinks that Luca thinks the stopwatch is in the grey locker.
8. Quinn thinks the stopwatch is in the grey locker.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the stopwatch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the cellar, which shows where the stopwatch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the cellar that the stopwatch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the stopwatch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the cellar at that step, NAME included. "missed_by" lists people in the cellar who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the cellar who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the cellar freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["black trunk", "grey locker", "green cupboard", "canvas sack"]. The names are: ["Amara", "Luca", "Quinn", "Xavier", "Yara"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Luca", "value": "grey locker", "present": ["Amara", "Luca", "Quinn"], "missed_by": [], "secret_witnesses": []}]`

## explain-L3-001 (workplace, seed 1730006)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Wanjiru, Goran, Yara, Jonas and Dalia work on the same team. This is what happened, in order.
1. Call with Wanjiru, Goran, Yara, Jonas and Dalia: Jonas books the client workshop into Room Cedar.
2. Call with Wanjiru, Goran, Yara and Jonas: Jonas moves the client workshop to Room Alder. Dalia is not on the call but secretly listens in, and can see who is on it. Nobody knows that Dalia is listening.
3. Call with Wanjiru, Goran, Yara and Jonas: Wanjiru moves the client workshop to Room Elm.
4. Call with Wanjiru, Goran, Yara and Jonas: Jonas moves the client workshop to Room Cedar.
5. Call with Wanjiru, Goran and Jonas: Wanjiru moves the client workshop to Room Dogwood. Yara is not on the call but secretly listens in, and can see who is on it. Nobody knows that Yara is listening.
6. Goran sends Dalia a direct message: “The client workshop is booked in Room Dogwood.”
7. [A step is missing here.]
8. Wanjiru sends Goran a direct message: “The client workshop is booked in Room Elm.” Yara secretly reads this message on Goran's screen. Neither Wanjiru nor Goran ever knows that Yara read it.
9. Call with Jonas and Dalia: Jonas opens the booking system and reads it out: “The client workshop is booked in Room Elm.” Goran is not on the call but secretly listens in, and can see who is on it. Nobody knows that Goran is listening.
10. Wanjiru sends Yara a direct message: “The client workshop is booked in Room Elm.”
11. Yara sends Dalia a direct message: “The client workshop is booked in Room Elm.”

Facts at the end of the story:
1. The client workshop is really booked in Room Elm.
2. Jonas thinks that Wanjiru thinks the client workshop is booked in Room Elm.
3. Wanjiru thinks that Dalia thinks the client workshop is booked in Room Cedar.
4. Jonas thinks that Goran thinks that Wanjiru thinks that Goran thinks the client workshop is booked in Room Dogwood.
5. Jonas thinks that Yara thinks the client workshop is booked in Room Cedar.
6. Dalia thinks that Wanjiru thinks the client workshop is booked in Room Alder.
7. Yara thinks that Wanjiru thinks that Jonas thinks that Wanjiru thinks the client workshop is booked in Room Dogwood.
8. Wanjiru thinks that Jonas thinks the client workshop is booked in Room Elm.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the client workshop to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the booking system and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the client workshop is booked in VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the client workshop is booked in VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Room Dogwood", "Room Elm", "Room Alder", "Room Cedar"]. The names are: ["Dalia", "Goran", "Jonas", "Wanjiru", "Yara"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Jonas", "value": "Room Elm", "present": ["Jonas", "Wanjiru"], "missed_by": [], "secret_witnesses": []}]`

## explain-L3-002 (classic, seed 1730010)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the sunroom see and hear everything that happens there, unless the story says that a person missed it. People outside the sunroom see and hear nothing of it, unless the story says so.
- Everyone in the sunroom can see who else is in the sunroom.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Jonas, Goran, Soren, Quinn and Emeka share a house. The sunroom has four closed containers that nobody can see into: the white cabinet, the wooden chest, the grey locker and the black trunk. This is what happened, in order.
1. Jonas, Goran, Soren, Quinn and Emeka are in the sunroom. Quinn takes a thimble out of a pocket and puts it in the wooden chest.
2. Jonas, Goran, Soren, Quinn and Emeka are in the sunroom. Jonas moves the thimble to the black trunk.
3. Goran, Soren, Quinn and Emeka are in the sunroom. Emeka moves the thimble to the grey locker. Jonas is outside but watches all of this through the window. Nobody knows that Jonas is watching.
4. Soren sends Jonas a private text message: “The thimble is in the grey locker.”
5. Goran, Soren, Quinn and Emeka are in the sunroom. Goran moves the thimble to the black trunk. Quinn is in the sunroom but is absorbed in a phone and does not notice this. Nobody realises that Quinn missed it. Jonas is outside but watches all of this through the window. Nobody knows that Jonas is watching.
6. Goran and Emeka are in the sunroom. Emeka moves the thimble to the white cabinet. Goran is in the sunroom but is absorbed in a phone and does not notice this. Nobody realises that Goran missed it. Soren is outside but watches all of this through the window. Nobody knows that Soren is watching.
7. Jonas and Goran are in the sunroom. Jonas moves the thimble to the black trunk.
8. Soren sends Quinn a private text message: “The thimble is in the white cabinet.”
9. [A step is missing here.]
10. Quinn wants to mislead Goran, so Quinn sends Goran a private text message: “The thimble is in the black trunk.” Jonas secretly reads this message on Goran's phone. Neither Quinn nor Goran ever knows that Jonas read it.
11. Jonas and Goran are in the sunroom. Goran moves the thimble to the white cabinet. Jonas is in the sunroom but is absorbed in a phone and does not notice this. Nobody realises that Jonas missed it. Emeka is outside but watches all of this through the window. Nobody knows that Emeka is watching.

Facts at the end of the story:
1. The thimble is really in the white cabinet.
2. Quinn thinks that Emeka thinks the thimble is in the wooden chest.
3. Quinn thinks the thimble is in the white cabinet.
4. Soren thinks that Emeka thinks the thimble is in the white cabinet.
5. Goran thinks that Emeka thinks the thimble is in the black trunk.
6. Jonas thinks that Emeka thinks the thimble is in the black trunk.
7. Quinn thinks that Soren thinks the thimble is in the white cabinet.
8. Quinn thinks that Jonas thinks the thimble is in the black trunk.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the thimble to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the sunroom, which shows where the thimble really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the sunroom that the thimble is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the thimble is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the sunroom at that step, NAME included. "missed_by" lists people in the sunroom who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the sunroom who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the sunroom freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["white cabinet", "wooden chest", "grey locker", "black trunk"]. The names are: ["Emeka", "Goran", "Jonas", "Quinn", "Soren"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Quinn", "to": "Emeka", "value": "wooden chest", "secret_readers": []}]`

## explain-L3-003 (workplace, seed 1730011)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Viktor, Yara, Ines, Luca and Oksana work on the same team. This is what happened, in order.
1. Call with Viktor, Yara, Ines, Luca and Oksana: Yara picks Northwind as the packaging supplier.
2. Call with Viktor, Yara, Ines, Luca and Oksana: Oksana switches the packaging supplier to Brightwater.
3. Call with Viktor, Yara, Ines, Luca and Oksana: Oksana switches the packaging supplier to Northwind.
4. Call with Viktor, Yara, Ines, Luca and Oksana: Viktor switches the packaging supplier to Brightwater.
5. Call with Viktor, Yara and Luca: Yara switches the packaging supplier to Halcyon.
6. Call with Viktor, Luca and Oksana: Oksana switches the packaging supplier to Brightwater. Viktor is on the call but has stepped away from the desk and misses this. Nobody realises that Viktor missed it.
7. Luca sends Yara a direct message: “The packaging supplier is Brightwater.”
8. Yara sends Viktor a direct message: “The packaging supplier is Brightwater.”
9. Viktor sends Luca a direct message: “The packaging supplier is Brightwater.” Ines secretly reads this message on Luca's screen. Neither Viktor nor Luca ever knows that Ines read it.
10. [A step is missing here.]
11. Viktor wants to mislead Ines, so Viktor sends Ines a direct message: “The packaging supplier is Halcyon.” Luca secretly reads this message on Ines's screen. Neither Viktor nor Ines ever knows that Luca read it.

Facts at the end of the story:
1. The packaging supplier is really Northwind.
2. Viktor thinks that Oksana thinks the packaging supplier is Northwind.
3. Oksana thinks that Viktor thinks the packaging supplier is Northwind.
4. Oksana thinks that Yara thinks that Oksana thinks that Viktor thinks the packaging supplier is Brightwater.
5. Ines thinks that Oksana thinks the packaging supplier is Brightwater.
6. Oksana thinks that Luca thinks the packaging supplier is Brightwater.
7. Oksana thinks that Ines thinks the packaging supplier is Brightwater.
8. Yara thinks that Oksana thinks that Viktor thinks the packaging supplier is Brightwater.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME switches the packaging supplier to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the supplier register and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the packaging supplier is VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the packaging supplier is VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Ironbridge", "Brightwater", "Halcyon", "Northwind"]. The names are: ["Ines", "Luca", "Oksana", "Viktor", "Yara"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Oksana", "value": "Northwind", "present": ["Oksana", "Viktor"], "missed_by": [], "secret_witnesses": []}]`

## explain-L3-004 (classic, seed 1730012)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the kitchen see and hear everything that happens there, unless the story says that a person missed it. People outside the kitchen see and hear nothing of it, unless the story says so.
- Everyone in the kitchen can see who else is in the kitchen.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Nadim, Pablo, Mirela, Dalia and Quinn share a house. The kitchen has four closed containers that nobody can see into: the leather bag, the white cabinet, the blue drawer and the wicker basket. This is what happened, in order.
1. Nadim, Pablo, Mirela, Dalia and Quinn are in the kitchen. Pablo takes a torch out of a pocket and puts it in the blue drawer.
2. Nadim, Pablo, Mirela and Dalia are in the kitchen. Pablo moves the torch to the wicker basket.
3. Mirela sends Quinn a private text message: “The torch is in the wicker basket.”
4. Dalia sends Quinn a private text message: “The torch is in the wicker basket.”
5. Nadim, Pablo, Mirela and Dalia are in the kitchen. Dalia moves the torch to the blue drawer. Pablo is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Pablo missed it.
6. Quinn wants to mislead Pablo, so Quinn sends Pablo a private text message: “The torch is in the leather bag.”
7. Pablo and Dalia are in the kitchen. Dalia opens every container in full view of the kitchen, showing that the torch is in the blue drawer.
8. Pablo sends Quinn a private text message: “The torch is in the blue drawer.”
9. Pablo sends Mirela a private text message: “The torch is in the blue drawer.”
10. [A step is missing here.]
11. Quinn wants to mislead Mirela, so Quinn sends Mirela a private text message: “The torch is in the white cabinet.”

Facts at the end of the story:
1. The torch is really in the leather bag.
2. Quinn thinks the torch is in the blue drawer.
3. Nadim thinks the torch is in the blue drawer.
4. Pablo thinks the torch is in the blue drawer.
5. Dalia thinks that Mirela thinks the torch is in the blue drawer.
6. Mirela thinks that Dalia thinks the torch is in the blue drawer.
7. Dalia thinks the torch is in the leather bag.
8. Dalia thinks that Nadim thinks the torch is in the blue drawer.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the torch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the kitchen, which shows where the torch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the kitchen that the torch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the torch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the kitchen at that step, NAME included. "missed_by" lists people in the kitchen who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the kitchen who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the kitchen freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["leather bag", "white cabinet", "blue drawer", "wicker basket"]. The names are: ["Dalia", "Mirela", "Nadim", "Pablo", "Quinn"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Dalia", "value": "leather bag", "present": ["Dalia"], "missed_by": [], "secret_witnesses": []}]`

## explain-L3-005 (workplace, seed 1730013)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Amara, Bruno, Wanjiru, Goran and Dalia work on the same team. This is what happened, in order.
1. Call with Amara, Bruno, Wanjiru, Goran and Dalia: Wanjiru sets the product release for Wednesday.
2. Call with Amara, Bruno, Wanjiru, Goran and Dalia: Dalia moves the product release to Thursday.
3. Call with Amara, Bruno, Wanjiru, Goran and Dalia: Dalia moves the product release to Monday.
4. Call with Amara, Bruno, Wanjiru, Goran and Dalia: Amara moves the product release to Friday.
5. Call with Amara, Bruno, Goran and Dalia: Dalia moves the product release to Thursday. Wanjiru is not on the call but secretly listens in, and can see who is on it. Nobody knows that Wanjiru is listening.
6. Bruno sends Wanjiru a direct message: “The product release is set for Thursday.”
7. Call with Amara, Bruno and Dalia: Bruno moves the product release to Wednesday. Wanjiru is not on the call but secretly listens in, and can see who is on it. Nobody knows that Wanjiru is listening.
8. Wanjiru sends Goran a direct message: “The product release is set for Wednesday.”
9. Dalia sends Goran a direct message: “The product release is set for Wednesday.” Wanjiru secretly reads this message on Goran's screen. Neither Dalia nor Goran ever knows that Wanjiru read it.
10. [A step is missing here.]
11. Amara sends Wanjiru a direct message: “The product release is set for Wednesday.”

Facts at the end of the story:
1. The product release is really set for Thursday.
2. Bruno thinks that Amara thinks the product release is set for Thursday.
3. Bruno thinks that Dalia thinks the product release is set for Wednesday.
4. Bruno thinks that Wanjiru thinks that Amara thinks that Wanjiru thinks the product release is set for Friday.
5. Dalia thinks that Amara thinks the product release is set for Wednesday.
6. Wanjiru thinks that Amara thinks that Bruno thinks the product release is set for Wednesday.
7. Goran thinks the product release is set for Thursday.
8. Wanjiru thinks that Goran thinks the product release is set for Wednesday.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Friday", "Thursday", "Wednesday", "Monday"]. The names are: ["Amara", "Bruno", "Dalia", "Goran", "Wanjiru"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Bruno", "value": "Thursday", "present": ["Amara", "Bruno"], "missed_by": ["Amara"], "secret_witnesses": ["Goran"]}]`

## explain-L3-006 (classic, seed 1730016)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the kitchen see and hear everything that happens there, unless the story says that a person missed it. People outside the kitchen see and hear nothing of it, unless the story says so.
- Everyone in the kitchen can see who else is in the kitchen.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Luca, Wanjiru, Emeka, Tariq and Ines share a house. The kitchen has four closed containers that nobody can see into: the wooden chest, the wicker basket, the grey locker and the red box. This is what happened, in order.
1. Luca, Wanjiru, Emeka, Tariq and Ines are in the kitchen. Emeka takes a padlock out of a pocket and puts it in the wooden chest.
2. Luca, Wanjiru, Emeka and Tariq are in the kitchen. Tariq moves the padlock to the grey locker. Wanjiru is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Wanjiru missed it. Ines is outside but watches all of this through the window. Nobody knows that Ines is watching.
3. Luca, Emeka and Tariq are in the kitchen. Luca opens every container in full view of the kitchen, showing that the padlock is in the grey locker. Emeka is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Emeka missed it. Wanjiru is outside but watches all of this through the window. Nobody knows that Wanjiru is watching.
4. Luca, Emeka and Tariq are in the kitchen. Luca moves the padlock to the red box.
5. Tariq wants to mislead Wanjiru, so Tariq sends Wanjiru a private text message: “The padlock is in the wicker basket.” Ines secretly reads this message on Wanjiru's phone. Neither Tariq nor Wanjiru ever knows that Ines read it.
6. Ines wants to mislead Luca, so Ines sends Luca a private text message: “The padlock is in the red box.”
7. [A step is missing here.]
8. Emeka sends Ines a private text message: “The padlock is in the wicker basket.”
9. Wanjiru sends Ines a private text message: “The padlock is in the wicker basket.”
10. Emeka sends Wanjiru a private text message: “The padlock is in the wicker basket.”
11. Emeka is alone in the kitchen. Emeka moves the padlock to the grey locker.

Facts at the end of the story:
1. The padlock is really in the grey locker.
2. Luca thinks that Emeka thinks that Luca thinks that Emeka thinks the padlock is in the wicker basket.
3. Ines thinks that Luca thinks the padlock is in the red box.
4. Wanjiru thinks that Luca thinks the padlock is in the grey locker.
5. Tariq thinks that Emeka thinks the padlock is in the red box.
6. Luca thinks that Tariq thinks the padlock is in the red box.
7. Emeka thinks that Luca thinks that Wanjiru thinks that Emeka thinks the padlock is in the grey locker.
8. Luca thinks the padlock is in the wicker basket.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the padlock to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the kitchen, which shows where the padlock really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the kitchen that the padlock is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the padlock is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the kitchen at that step, NAME included. "missed_by" lists people in the kitchen who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the kitchen who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the kitchen freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["wooden chest", "wicker basket", "grey locker", "red box"]. The names are: ["Emeka", "Ines", "Luca", "Tariq", "Wanjiru"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Emeka", "value": "wicker basket", "present": ["Emeka", "Luca"], "missed_by": [], "secret_witnesses": []}]`

## explain-L3-007 (workplace, seed 1730019)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Tariq, Quinn, Dalia, Hana and Rania work on the same team. This is what happened, in order.
1. Call with Tariq, Quinn, Dalia, Hana and Rania: Hana sets the product release for Wednesday.
2. Call with Tariq, Quinn, Dalia, Hana and Rania: Tariq moves the product release to Thursday.
3. Call with Tariq, Quinn, Dalia, Hana and Rania: Dalia moves the product release to Tuesday.
4. Call with Tariq, Quinn, Dalia, Hana and Rania: Hana moves the product release to Friday.
5. Call with Tariq, Quinn, Hana and Rania: Quinn moves the product release to Thursday. Hana is on the call but has stepped away from the desk and misses this. Nobody realises that Hana missed it.
6. Call with Tariq, Quinn, Hana and Rania: Rania opens the release calendar and reads it out: “The product release is set for Thursday.” Quinn is on the call but has stepped away from the desk and misses this. Nobody realises that Quinn missed it.
7. Tariq wants to mislead Dalia, so Tariq sends Dalia a direct message: “The product release is set for Tuesday.”
8. Hana wants to mislead Dalia, so Hana sends Dalia a direct message: “The product release is set for Tuesday.”
9. Call with Tariq, Quinn and Hana: Quinn moves the product release to Friday.
10. [A step is missing here.]
11. Call with Tariq, Quinn and Hana: Quinn moves the product release to Tuesday.

Facts at the end of the story:
1. The product release is really set for Tuesday.
2. Dalia thinks that Rania thinks the product release is set for Tuesday.
3. Rania thinks the product release is set for Tuesday.
4. Tariq thinks that Rania thinks the product release is set for Thursday.
5. Quinn thinks that Rania thinks the product release is set for Thursday.
6. Hana thinks that Rania thinks the product release is set for Thursday.
7. Rania thinks that Hana thinks the product release is set for Thursday.
8. Dalia thinks that Rania thinks that Tariq thinks the product release is set for Friday.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Thursday", "Friday", "Wednesday", "Tuesday"]. The names are: ["Dalia", "Hana", "Quinn", "Rania", "Tariq"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Dalia", "to": "Rania", "value": "Tuesday", "secret_readers": []}]`

## explain-L3-008 (classic, seed 1730022)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the study see and hear everything that happens there, unless the story says that a person missed it. People outside the study see and hear nothing of it, unless the story says so.
- Everyone in the study can see who else is in the study.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Amara, Yara, Xavier, Emeka and Bruno share a house. The study has four closed containers that nobody can see into: the wicker basket, the green cupboard, the red box and the wooden chest. This is what happened, in order.
1. Amara, Yara, Xavier, Emeka and Bruno are in the study. Bruno takes a compass out of a pocket and puts it in the green cupboard.
2. Amara, Yara, Xavier, Emeka and Bruno are in the study. Bruno moves the compass to the wooden chest. Xavier is in the study but is absorbed in a phone and does not notice this. Nobody realises that Xavier missed it.
3. Amara, Xavier and Bruno are in the study. Xavier moves the compass to the wicker basket.
4. Amara, Xavier and Bruno are in the study. Xavier moves the compass to the wooden chest.
5. Amara, Xavier and Bruno are in the study. Xavier moves the compass to the red box.
6. [A step is missing here.]
7. Amara sends Yara a private text message: “The compass is in the wicker basket.”
8. Amara wants to mislead Xavier, so Amara sends Xavier a private text message: “The compass is in the green cupboard.”
9. Bruno is alone in the study. Bruno moves the compass to the red box.
10. Bruno is alone in the study. Bruno opens every container and sees that the compass is in the red box. Yara is outside but watches all of this through the window. Nobody knows that Yara is watching.
11. Bruno is alone in the study. Bruno moves the compass to the wicker basket. Yara is outside but watches all of this through the window. Nobody knows that Yara is watching.

Facts at the end of the story:
1. The compass is really in the wicker basket.
2. Bruno thinks that Amara thinks the compass is in the wicker basket.
3. Bruno thinks that Emeka thinks the compass is in the wooden chest.
4. Bruno thinks that Yara thinks that Amara thinks the compass is in the wooden chest.
5. Bruno thinks that Amara thinks that Xavier thinks that Amara thinks the compass is in the red box.
6. Emeka thinks the compass is in the wooden chest.
7. Xavier thinks that Bruno thinks the compass is in the red box.
8. Amara thinks that Bruno thinks the compass is in the wicker basket.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the compass to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the study, which shows where the compass really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the study that the compass is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the compass is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the study at that step, NAME included. "missed_by" lists people in the study who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the study who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the study freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["wicker basket", "green cupboard", "red box", "wooden chest"]. The names are: ["Amara", "Bruno", "Emeka", "Xavier", "Yara"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Amara", "value": "wicker basket", "present": ["Amara", "Bruno"], "missed_by": [], "secret_witnesses": []}]`

## explain-L3-009 (workplace, seed 1730023)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- A person learns a fact only by being on a call where it is set, read out or said, by checking a system, or by being told.
- People on a call hear everything that happens on it, unless the story says that a person missed it. People who are not on a call learn nothing about it, unless the story says so.
- Everyone on a call can see who else is on it.
- Direct messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Soren, Uma, Keiko, Chidi and Ines work on the same team. This is what happened, in order.
1. Call with Soren, Uma, Keiko, Chidi and Ines: Keiko sets the product release for Friday.
2. Call with Soren, Uma, Keiko, Chidi and Ines: Keiko moves the product release to Thursday.
3. Call with Uma, Keiko and Chidi: Chidi moves the product release to Tuesday. Soren is not on the call but secretly listens in, and can see who is on it. Nobody knows that Soren is listening.
4. Uma sends Ines a direct message: “The product release is set for Tuesday.” Keiko secretly reads this message on Ines's screen. Neither Uma nor Ines ever knows that Keiko read it.
5. Call with Uma and Chidi: Uma moves the product release to Friday.
6. Call with Uma and Chidi: Chidi moves the product release to Monday.
7. [A step is missing here.]
8. Ines sends Soren a direct message: “The product release is set for Monday.”
9. Uma sends Soren a direct message: “The product release is set for Monday.”
10. Call with Uma and Keiko: Keiko moves the product release to Thursday. Uma is on the call but has stepped away from the desk and misses this. Nobody realises that Uma missed it.
11. Chidi wants to mislead Keiko, so Chidi sends Keiko a direct message: “The product release is set for Thursday.”

Facts at the end of the story:
1. The product release is really set for Thursday.
2. Soren thinks that Ines thinks that Chidi thinks the product release is set for Monday.
3. Ines thinks that Soren thinks that Chidi thinks the product release is set for Thursday.
4. Uma thinks that Ines thinks the product release is set for Tuesday.
5. Keiko thinks that Ines thinks the product release is set for Tuesday.
6. Soren thinks that Ines thinks that Uma thinks that Ines thinks the product release is set for Thursday.
7. Ines thinks that Keiko thinks the product release is set for Thursday.
8. Chidi thinks that Ines thinks the product release is set for Monday.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the product release to VALUE, which must not be the value it already has.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens the release calendar and reads it out, which shows the true value.
- {"step": "say", "who": NAME, "value": VALUE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says on a call that the product release is set for VALUE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": VALUE, "secret_readers": [NAMES]}
  One person sends another a direct message that says the product release is set for VALUE.

Notes on the steps:
- "present" lists everyone on the call at that step, NAME included. A "present" list with only NAME means that NAME works alone. "missed_by" lists people on the call who have stepped away and miss the step, while nobody realises that they missed it. "secret_witnesses" lists people not on the call who secretly listen in and can see who is on it (or who secretly watch the screen of a person who works alone), while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's screen, while the sender and the receiver never know.
- Every call is a new call with its own list of people.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["Thursday", "Tuesday", "Friday", "Monday"]. The names are: ["Chidi", "Ines", "Keiko", "Soren", "Uma"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Chidi", "to": "Ines", "value": "Monday", "secret_readers": ["Soren"]}]`
