
## plan-L1-000 (classic, seed 5510001)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Nadim, Mirela, Keiko and Xavier share a house. The study has four closed containers that nobody can see into: the wicker basket, the white cabinet, the canvas sack and the black trunk. This is what happened, in order.
1. Nadim, Mirela, Keiko and Xavier are in the study. Keiko takes a whistle out of a pocket and puts it in the white cabinet.

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
  NAME moves the whistle to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the study, which shows where the whistle really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the study that the whistle is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the whistle is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the study at that step, NAME included. "missed_by" lists people in the study who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the study who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the study freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["wicker basket", "white cabinet", "canvas sack", "black trunk"]. The names are: ["Keiko", "Mirela", "Nadim", "Xavier"].

Targets. After your last step, all of these must be true:
1. The whistle is really in the wicker basket.
2. Nadim thinks the whistle is in the wicker basket.
3. Mirela thinks the whistle is in the wicker basket.
4. Keiko thinks the whistle is in the wicker basket.
5. Xavier thinks the whistle is in the wicker basket.
6. Keiko thinks that Xavier thinks the whistle is in the white cabinet.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Xavier", "value": "canvas sack", "present": ["Keiko", "Mirela", "Nadim", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Xavier", "value": "white cabinet", "present": ["Keiko", "Mirela", "Nadim", "Xavier"], "missed_by": ["Nadim"], "secret_witnesses": []}, {"step": "change", "who": "Nadim", "value": "wicker basket", "present": ["Mirela", "Nadim", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Nadim", "to": "Keiko", "value": "wicker basket", "secret_readers": []}]`

## plan-L1-001 (workplace, seed 5510002)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Keiko, Chidi, Rania and Jonas work on the same team. This is what happened, in order.
1. Call with Keiko, Chidi, Rania and Jonas: Rania books the client workshop into Room Dogwood.

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
- The values are: ["Room Elm", "Room Fir", "Room Dogwood", "Room Alder"]. The names are: ["Chidi", "Jonas", "Keiko", "Rania"].

Targets. After your last step, all of these must be true:
1. The client workshop is really booked in Room Elm.
2. Keiko thinks the client workshop is booked in Room Elm.
3. Chidi thinks the client workshop is booked in Room Elm.
4. Rania thinks the client workshop is booked in Room Elm.
5. Jonas thinks the client workshop is booked in Room Elm.
6. Chidi thinks that Rania thinks the client workshop is booked in Room Dogwood.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Keiko", "value": "Room Fir", "present": ["Chidi", "Jonas", "Keiko", "Rania"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Keiko", "value": "Room Dogwood", "present": ["Chidi", "Jonas", "Keiko", "Rania"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Rania", "value": "Room Elm", "present": ["Jonas", "Keiko", "Rania"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Jonas", "to": "Chidi", "value": "Room Elm", "secret_readers": []}]`

## plan-L1-002 (classic, seed 5510005)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Farah, Yara, Xavier and Ines share a house. The boathouse has four closed containers that nobody can see into: the leather bag, the red box, the wicker basket and the wooden chest. This is what happened, in order.
1. Farah, Yara, Xavier and Ines are in the boathouse. Farah takes a padlock out of a pocket and puts it in the wooden chest.

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
  NAME moves the padlock to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the boathouse, which shows where the padlock really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the boathouse that the padlock is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the padlock is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the boathouse at that step, NAME included. "missed_by" lists people in the boathouse who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the boathouse who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the boathouse freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["leather bag", "red box", "wicker basket", "wooden chest"]. The names are: ["Farah", "Ines", "Xavier", "Yara"].

Targets. After your last step, all of these must be true:
1. The padlock is really in the leather bag.
2. Farah thinks the padlock is in the leather bag.
3. Yara thinks the padlock is in the leather bag.
4. Xavier thinks the padlock is in the wooden chest.
5. Ines thinks the padlock is in the wicker basket.
6. Xavier thinks that Farah thinks the padlock is in the wicker basket.

Write at least 1 and at most 3 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Yara", "value": "wicker basket", "present": ["Farah", "Ines", "Xavier", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Yara", "to": "Xavier", "value": "wooden chest", "secret_readers": []}, {"step": "change", "who": "Yara", "value": "leather bag", "present": ["Farah", "Yara"], "missed_by": [], "secret_witnesses": []}]`

## plan-L1-003 (workplace, seed 5510008)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Hana, Uma, Yara and Xavier work on the same team. This is what happened, in order.
1. Call with Hana, Uma, Yara and Xavier: Uma fixes Graz as the place for the team offsite.

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
- The values are: ["Leeds", "Porto", "Graz", "Turin"]. The names are: ["Hana", "Uma", "Xavier", "Yara"].

Targets. After your last step, all of these must be true:
1. The team offsite is really in Graz.
2. Hana thinks the team offsite is in Graz.
3. Uma thinks the team offsite is in Graz.
4. Yara thinks the team offsite is in Graz.
5. Xavier thinks the team offsite is in Graz.
6. Yara thinks that Hana thinks the team offsite is in Porto.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Hana", "value": "Porto", "present": ["Hana", "Uma", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Hana", "to": "Yara", "value": "Porto", "secret_readers": []}, {"step": "change", "who": "Xavier", "value": "Graz", "present": ["Hana", "Uma", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Uma", "to": "Yara", "value": "Graz", "secret_readers": []}]`

## plan-L1-004 (classic, seed 5510011)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Goran, Soren, Keiko and Quinn share a house. The boathouse has four closed containers that nobody can see into: the blue drawer, the wooden chest, the canvas sack and the wicker basket. This is what happened, in order.
1. Goran, Soren, Keiko and Quinn are in the boathouse. Goran takes a thimble out of a pocket and puts it in the blue drawer.

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
  NAME moves the thimble to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the boathouse, which shows where the thimble really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the boathouse that the thimble is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the thimble is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the boathouse at that step, NAME included. "missed_by" lists people in the boathouse who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the boathouse who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the boathouse freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["blue drawer", "wooden chest", "canvas sack", "wicker basket"]. The names are: ["Goran", "Keiko", "Quinn", "Soren"].

Targets. After your last step, all of these must be true:
1. The thimble is really in the blue drawer.
2. Goran thinks the thimble is in the wooden chest.
3. Soren thinks the thimble is in the blue drawer.
4. Keiko thinks the thimble is in the wicker basket.
5. Quinn thinks the thimble is in the blue drawer.
6. Goran thinks that Quinn thinks the thimble is in the wicker basket.

Write at least 1 and at most 3 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Goran", "value": "wicker basket", "present": ["Goran", "Keiko", "Quinn", "Soren"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Quinn", "value": "blue drawer", "present": ["Quinn", "Soren"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Soren", "to": "Goran", "value": "wooden chest", "secret_readers": []}]`

## plan-L1-005 (workplace, seed 5510012)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Amara, Quinn, Nadim and Wanjiru work on the same team. This is what happened, in order.
1. Call with Amara, Quinn, Nadim and Wanjiru: Wanjiru picks Sablewood as the packaging supplier.

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
- The values are: ["Halcyon", "Ironbridge", "Brightwater", "Sablewood"]. The names are: ["Amara", "Nadim", "Quinn", "Wanjiru"].

Targets. After your last step, all of these must be true:
1. The packaging supplier is really Brightwater.
2. Amara thinks the packaging supplier is Brightwater.
3. Quinn thinks the packaging supplier is Brightwater.
4. Nadim thinks the packaging supplier is Brightwater.
5. Wanjiru thinks the packaging supplier is Brightwater.
6. Quinn thinks that Nadim thinks the packaging supplier is Sablewood.

Write at least 1 and at most 3 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Amara", "value": "Brightwater", "present": ["Amara"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Amara", "to": "Nadim", "value": "Brightwater", "secret_readers": []}, {"step": "check", "who": "Amara", "present": ["Amara", "Quinn", "Wanjiru"], "missed_by": [], "secret_witnesses": []}]`

## plan-L2-000 (classic, seed 5520001)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Bruno, Amara, Dalia, Luca and Jonas share a house. The garage has four closed containers that nobody can see into: the blue drawer, the leather bag, the canvas sack and the grey locker. This is what happened, in order.
1. Bruno, Amara, Dalia, Luca and Jonas are in the garage. Dalia takes a whistle out of a pocket and puts it in the grey locker.

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
  NAME moves the whistle to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the garage, which shows where the whistle really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the garage that the whistle is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the whistle is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the garage at that step, NAME included. "missed_by" lists people in the garage who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the garage who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the garage freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["blue drawer", "leather bag", "canvas sack", "grey locker"]. The names are: ["Amara", "Bruno", "Dalia", "Jonas", "Luca"].

Targets. After your last step, all of these must be true:
1. The whistle is really in the blue drawer.
2. Bruno thinks the whistle is in the grey locker.
3. Amara thinks the whistle is in the blue drawer.
4. Dalia thinks the whistle is in the blue drawer.
5. Luca thinks the whistle is in the blue drawer.
6. Jonas thinks the whistle is in the blue drawer.
7. Jonas thinks that Amara thinks the whistle is in the blue drawer.
8. Jonas thinks that Amara thinks that Dalia thinks the whistle is in the leather bag.
9. Bruno thinks that Dalia thinks the whistle is in the grey locker.
10. Bruno thinks that Dalia thinks that Luca thinks the whistle is in the leather bag.

Write at least 1 and at most 3 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Bruno", "value": "leather bag", "present": ["Amara", "Bruno", "Dalia", "Jonas", "Luca"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Luca", "value": "blue drawer", "present": ["Amara", "Jonas", "Luca"], "missed_by": [], "secret_witnesses": ["Dalia"]}, {"step": "message", "from": "Dalia", "to": "Bruno", "value": "grey locker", "secret_readers": []}]`

## plan-L2-001 (workplace, seed 5520004)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Chidi, Viktor, Tariq, Rania and Luca work on the same team. This is what happened, in order.
1. Call with Chidi, Viktor, Tariq, Rania and Luca: Luca assigns the Marlow account to the Denver office.

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
- The values are: ["the Denver office", "the Nairobi office", "the Lisbon office", "the Osaka office"]. The names are: ["Chidi", "Luca", "Rania", "Tariq", "Viktor"].

Targets. After your last step, all of these must be true:
1. The Marlow account is really with the Denver office.
2. Chidi thinks the Marlow account is with the Osaka office.
3. Viktor thinks the Marlow account is with the Denver office.
4. Tariq thinks the Marlow account is with the Osaka office.
5. Rania thinks the Marlow account is with the Denver office.
6. Luca thinks the Marlow account is with the Denver office.
7. Tariq thinks that Rania thinks the Marlow account is with the Osaka office.
8. Tariq thinks that Rania thinks that Viktor thinks the Marlow account is with the Nairobi office.
9. Viktor thinks that Rania thinks the Marlow account is with the Denver office.
10. Viktor thinks that Rania thinks that Tariq thinks the Marlow account is with the Nairobi office.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Viktor", "value": "the Nairobi office", "present": ["Luca", "Rania", "Tariq", "Viktor"], "missed_by": ["Luca"], "secret_witnesses": []}, {"step": "change", "who": "Rania", "value": "the Osaka office", "present": ["Luca", "Rania", "Tariq"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Tariq", "to": "Chidi", "value": "the Osaka office", "secret_readers": []}, {"step": "change", "who": "Rania", "value": "the Denver office", "present": ["Luca", "Rania", "Viktor"], "missed_by": [], "secret_witnesses": []}]`

## plan-L2-002 (classic, seed 5520005)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Chidi, Luca, Zoltan, Farah and Nadim share a house. The cellar has four closed containers that nobody can see into: the canvas sack, the black trunk, the green cupboard and the leather bag. This is what happened, in order.
1. Chidi, Luca, Zoltan, Farah and Nadim are in the cellar. Zoltan takes a token out of a pocket and puts it in the leather bag.

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
  NAME moves the token to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the cellar, which shows where the token really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the cellar that the token is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the token is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the cellar at that step, NAME included. "missed_by" lists people in the cellar who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the cellar who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the cellar freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["canvas sack", "black trunk", "green cupboard", "leather bag"]. The names are: ["Chidi", "Farah", "Luca", "Nadim", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The token is really in the canvas sack.
2. Chidi thinks the token is in the canvas sack.
3. Luca thinks the token is in the canvas sack.
4. Zoltan thinks the token is in the canvas sack.
5. Farah thinks the token is in the canvas sack.
6. Nadim thinks the token is in the canvas sack.
7. Nadim thinks that Zoltan thinks the token is in the canvas sack.
8. Nadim thinks that Zoltan thinks that Nadim thinks the token is in the black trunk.
9. Luca thinks that Nadim thinks the token is in the green cupboard.
10. Luca thinks that Nadim thinks that Zoltan thinks the token is in the black trunk.

Write at least 1 and at most 3 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Zoltan", "value": "black trunk", "present": ["Chidi", "Farah", "Luca", "Nadim", "Zoltan"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Luca", "to": "Nadim", "value": "green cupboard", "secret_readers": ["Zoltan"]}, {"step": "change", "who": "Luca", "value": "canvas sack", "present": ["Chidi", "Farah", "Luca", "Zoltan"], "missed_by": [], "secret_witnesses": ["Nadim"]}]`

## plan-L2-003 (workplace, seed 5520006)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Hana, Ines, Soren, Jonas and Farah work on the same team. This is what happened, in order.
1. Call with Hana, Ines, Soren, Jonas and Farah: Farah sets the product release for Friday.

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
- The values are: ["Friday", "Thursday", "Monday", "Tuesday"]. The names are: ["Farah", "Hana", "Ines", "Jonas", "Soren"].

Targets. After your last step, all of these must be true:
1. The product release is really set for Tuesday.
2. Hana thinks the product release is set for Monday.
3. Ines thinks the product release is set for Tuesday.
4. Soren thinks the product release is set for Tuesday.
5. Jonas thinks the product release is set for Tuesday.
6. Farah thinks the product release is set for Tuesday.
7. Jonas thinks that Hana thinks the product release is set for Monday.
8. Jonas thinks that Hana thinks that Soren thinks the product release is set for Friday.
9. Soren thinks that Hana thinks the product release is set for Tuesday.
10. Soren thinks that Hana thinks that Jonas thinks the product release is set for Friday.

Write at least 1 and at most 5 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Farah", "value": "Tuesday", "present": ["Farah", "Hana", "Ines", "Jonas"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Farah", "value": "Friday", "present": ["Farah", "Ines"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Jonas", "to": "Hana", "value": "Monday", "secret_readers": []}, {"step": "change", "who": "Jonas", "value": "Tuesday", "present": ["Farah", "Ines", "Jonas"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Hana", "to": "Soren", "value": "Tuesday", "secret_readers": ["Ines"]}]`

## plan-L2-004 (classic, seed 5520007)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Xavier, Zoltan, Goran, Ines and Dalia share a house. The attic has four closed containers that nobody can see into: the white cabinet, the wicker basket, the wooden chest and the leather bag. This is what happened, in order.
1. Xavier, Zoltan, Goran, Ines and Dalia are in the attic. Goran takes a padlock out of a pocket and puts it in the white cabinet.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the attic see and hear everything that happens there, unless the story says that a person missed it. People outside the attic see and hear nothing of it, unless the story says so.
- Everyone in the attic can see who else is in the attic.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the padlock to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the attic, which shows where the padlock really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the attic that the padlock is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the padlock is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the attic at that step, NAME included. "missed_by" lists people in the attic who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the attic who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the attic freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["white cabinet", "wicker basket", "wooden chest", "leather bag"]. The names are: ["Dalia", "Goran", "Ines", "Xavier", "Zoltan"].

Targets. After your last step, all of these must be true:
1. The padlock is really in the leather bag.
2. Xavier thinks the padlock is in the white cabinet.
3. Zoltan thinks the padlock is in the leather bag.
4. Goran thinks the padlock is in the leather bag.
5. Ines thinks the padlock is in the wicker basket.
6. Dalia thinks the padlock is in the white cabinet.
7. Ines thinks that Xavier thinks the padlock is in the wicker basket.
8. Ines thinks that Xavier thinks that Goran thinks the padlock is in the white cabinet.
9. Goran thinks that Zoltan thinks the padlock is in the leather bag.
10. Goran thinks that Zoltan thinks that Ines thinks the padlock is in the white cabinet.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Zoltan", "value": "wicker basket", "present": ["Dalia", "Ines", "Xavier", "Zoltan"], "missed_by": ["Xavier"], "secret_witnesses": []}, {"step": "message", "from": "Zoltan", "to": "Goran", "value": "leather bag", "secret_readers": []}, {"step": "change", "who": "Dalia", "value": "white cabinet", "present": ["Dalia", "Zoltan"], "missed_by": [], "secret_witnesses": ["Xavier"]}, {"step": "change", "who": "Zoltan", "value": "leather bag", "present": ["Zoltan"], "missed_by": [], "secret_witnesses": []}]`

## plan-L2-005 (workplace, seed 5520008)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Emeka, Nadim, Hana, Jonas and Xavier work on the same team. This is what happened, in order.
1. Call with Emeka, Nadim, Hana, Jonas and Xavier: Hana assigns the Marlow account to the Nairobi office.

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
- The values are: ["the Denver office", "the Nairobi office", "the Lisbon office", "the Osaka office"]. The names are: ["Emeka", "Hana", "Jonas", "Nadim", "Xavier"].

Targets. After your last step, all of these must be true:
1. The Marlow account is really with the Osaka office.
2. Emeka thinks the Marlow account is with the Osaka office.
3. Nadim thinks the Marlow account is with the Denver office.
4. Hana thinks the Marlow account is with the Osaka office.
5. Jonas thinks the Marlow account is with the Osaka office.
6. Xavier thinks the Marlow account is with the Osaka office.
7. Xavier thinks that Emeka thinks the Marlow account is with the Osaka office.
8. Xavier thinks that Emeka thinks that Hana thinks the Marlow account is with the Denver office.
9. Nadim thinks that Xavier thinks the Marlow account is with the Denver office.
10. Nadim thinks that Xavier thinks that Hana thinks the Marlow account is with the Nairobi office.

Write at least 1 and at most 3 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Hana", "value": "the Denver office", "present": ["Emeka", "Hana", "Jonas", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Jonas", "value": "the Osaka office", "present": ["Emeka", "Jonas", "Xavier"], "missed_by": [], "secret_witnesses": ["Hana"]}, {"step": "message", "from": "Xavier", "to": "Nadim", "value": "the Denver office", "secret_readers": []}]`

## plan-L3-000 (classic, seed 5530001)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Keiko, Xavier, Amara, Viktor and Bruno share a house. The garage has four closed containers that nobody can see into: the leather bag, the canvas sack, the black trunk and the green cupboard. This is what happened, in order.
1. Keiko, Xavier, Amara, Viktor and Bruno are in the garage. Keiko takes a brooch out of a pocket and puts it in the leather bag.

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
  NAME moves the brooch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the garage, which shows where the brooch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the garage that the brooch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the brooch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the garage at that step, NAME included. "missed_by" lists people in the garage who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the garage who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the garage freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["leather bag", "canvas sack", "black trunk", "green cupboard"]. The names are: ["Amara", "Bruno", "Keiko", "Viktor", "Xavier"].

Targets. After your last step, all of these must be true:
1. The brooch is really in the leather bag.
2. Keiko thinks the brooch is in the leather bag.
3. Xavier thinks the brooch is in the canvas sack.
4. Amara thinks the brooch is in the leather bag.
5. Viktor thinks the brooch is in the leather bag.
6. Bruno thinks the brooch is in the leather bag.
7. Keiko thinks that Viktor thinks the brooch is in the leather bag.
8. Keiko thinks that Viktor thinks that Keiko thinks the brooch is in the leather bag.
9. Keiko thinks that Viktor thinks that Keiko thinks that Amara thinks the brooch is in the black trunk.
10. Bruno thinks that Viktor thinks the brooch is in the leather bag.
11. Bruno thinks that Viktor thinks that Keiko thinks the brooch is in the leather bag.
12. Bruno thinks that Viktor thinks that Keiko thinks that Amara thinks the brooch is in the black trunk.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Keiko", "value": "black trunk", "present": ["Amara", "Bruno", "Keiko", "Viktor", "Xavier"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Viktor", "to": "Xavier", "value": "canvas sack", "secret_readers": []}, {"step": "change", "who": "Viktor", "value": "leather bag", "present": ["Keiko", "Viktor"], "missed_by": [], "secret_witnesses": ["Bruno"]}, {"step": "message", "from": "Keiko", "to": "Amara", "value": "leather bag", "secret_readers": []}]`

## plan-L3-001 (workplace, seed 5530005)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Quinn, Amara, Uma, Mirela and Bruno work on the same team. This is what happened, in order.
1. Call with Quinn, Amara, Uma, Mirela and Bruno: Uma sets the discount on the Fenwick quote at 15%.

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
- The values are: ["20%", "10%", "25%", "15%"]. The names are: ["Amara", "Bruno", "Mirela", "Quinn", "Uma"].

Targets. After your last step, all of these must be true:
1. The discount on the Fenwick quote is really 25%.
2. Quinn thinks the discount on the Fenwick quote is 25%.
3. Amara thinks the discount on the Fenwick quote is 25%.
4. Uma thinks the discount on the Fenwick quote is 25%.
5. Mirela thinks the discount on the Fenwick quote is 20%.
6. Bruno thinks the discount on the Fenwick quote is 25%.
7. Quinn thinks that Amara thinks the discount on the Fenwick quote is 25%.
8. Quinn thinks that Amara thinks that Uma thinks the discount on the Fenwick quote is 25%.
9. Quinn thinks that Amara thinks that Uma thinks that Mirela thinks the discount on the Fenwick quote is 15%.
10. Mirela thinks that Uma thinks the discount on the Fenwick quote is 20%.
11. Mirela thinks that Uma thinks that Bruno thinks the discount on the Fenwick quote is 25%.
12. Mirela thinks that Uma thinks that Bruno thinks that Quinn thinks the discount on the Fenwick quote is 15%.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Amara", "value": "25%", "present": ["Amara", "Bruno", "Mirela", "Uma"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Amara", "value": "20%", "present": ["Amara", "Bruno", "Quinn", "Uma"], "missed_by": ["Quinn"], "secret_witnesses": []}, {"step": "message", "from": "Uma", "to": "Mirela", "value": "20%", "secret_readers": []}, {"step": "change", "who": "Amara", "value": "25%", "present": ["Amara", "Bruno", "Quinn", "Uma"], "missed_by": [], "secret_witnesses": []}]`

## plan-L3-002 (classic, seed 5530006)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Viktor, Chidi, Farah, Rania and Wanjiru share a house. The attic has four closed containers that nobody can see into: the canvas sack, the wooden chest, the leather bag and the blue drawer. This is what happened, in order.
1. Viktor, Chidi, Farah, Rania and Wanjiru are in the attic. Rania takes a marble out of a pocket and puts it in the wooden chest.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the attic see and hear everything that happens there, unless the story says that a person missed it. People outside the attic see and hear nothing of it, unless the story says so.
- Everyone in the attic can see who else is in the attic.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the marble to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the attic, which shows where the marble really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the attic that the marble is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the marble is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the attic at that step, NAME included. "missed_by" lists people in the attic who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the attic who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the attic freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["canvas sack", "wooden chest", "leather bag", "blue drawer"]. The names are: ["Chidi", "Farah", "Rania", "Viktor", "Wanjiru"].

Targets. After your last step, all of these must be true:
1. The marble is really in the leather bag.
2. Viktor thinks the marble is in the leather bag.
3. Chidi thinks the marble is in the leather bag.
4. Farah thinks the marble is in the leather bag.
5. Rania thinks the marble is in the leather bag.
6. Wanjiru thinks the marble is in the blue drawer.
7. Chidi thinks that Rania thinks the marble is in the leather bag.
8. Chidi thinks that Rania thinks that Wanjiru thinks the marble is in the leather bag.
9. Chidi thinks that Rania thinks that Wanjiru thinks that Farah thinks the marble is in the blue drawer.
10. Rania thinks that Chidi thinks the marble is in the leather bag.
11. Rania thinks that Chidi thinks that Rania thinks the marble is in the leather bag.
12. Rania thinks that Chidi thinks that Rania thinks that Farah thinks the marble is in the wooden chest.

Write at least 1 and at most 5 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Farah", "value": "leather bag", "present": ["Farah", "Rania", "Viktor", "Wanjiru"], "missed_by": ["Viktor"], "secret_witnesses": []}, {"step": "change", "who": "Farah", "value": "wooden chest", "present": ["Chidi", "Farah", "Rania", "Wanjiru"], "missed_by": ["Wanjiru"], "secret_witnesses": []}, {"step": "change", "who": "Farah", "value": "blue drawer", "present": ["Chidi", "Farah", "Rania", "Wanjiru"], "missed_by": ["Rania"], "secret_witnesses": []}, {"step": "change", "who": "Chidi", "value": "leather bag", "present": ["Chidi", "Rania", "Wanjiru"], "missed_by": ["Wanjiru"], "secret_witnesses": ["Farah"]}, {"step": "message", "from": "Farah", "to": "Viktor", "value": "leather bag", "secret_readers": []}]`

## plan-L3-003 (workplace, seed 5530009)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Quinn, Uma, Chidi, Mirela and Yara work on the same team. This is what happened, in order.
1. Call with Quinn, Uma, Chidi, Mirela and Yara: Mirela books the client workshop into Room Birch.

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
- The values are: ["Room Birch", "Room Fir", "Room Elm", "Room Alder"]. The names are: ["Chidi", "Mirela", "Quinn", "Uma", "Yara"].

Targets. After your last step, all of these must be true:
1. The client workshop is really booked in Room Fir.
2. Quinn thinks the client workshop is booked in Room Fir.
3. Uma thinks the client workshop is booked in Room Elm.
4. Chidi thinks the client workshop is booked in Room Fir.
5. Mirela thinks the client workshop is booked in Room Fir.
6. Yara thinks the client workshop is booked in Room Fir.
7. Chidi thinks that Mirela thinks the client workshop is booked in Room Fir.
8. Chidi thinks that Mirela thinks that Chidi thinks the client workshop is booked in Room Fir.
9. Chidi thinks that Mirela thinks that Chidi thinks that Yara thinks the client workshop is booked in Room Birch.
10. Uma thinks that Mirela thinks the client workshop is booked in Room Elm.
11. Uma thinks that Mirela thinks that Chidi thinks the client workshop is booked in Room Elm.
12. Uma thinks that Mirela thinks that Chidi thinks that Yara thinks the client workshop is booked in Room Birch.

Write at least 1 and at most 4 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Chidi", "value": "Room Fir", "present": ["Chidi", "Quinn", "Uma", "Yara"], "missed_by": ["Uma"], "secret_witnesses": []}, {"step": "change", "who": "Uma", "value": "Room Elm", "present": ["Chidi", "Mirela", "Quinn", "Uma"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Quinn", "value": "Room Fir", "present": ["Chidi", "Mirela", "Quinn"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Chidi", "to": "Yara", "value": "Room Fir", "secret_readers": ["Mirela"]}]`

## plan-L3-004 (classic, seed 5530010)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Chidi, Farah, Hana, Yara and Bruno share a house. The attic has four closed containers that nobody can see into: the blue drawer, the canvas sack, the white cabinet and the grey locker. This is what happened, in order.
1. Chidi, Farah, Hana, Yara and Bruno are in the attic. Hana takes a padlock out of a pocket and puts it in the canvas sack.

Rules of the scene:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the attic see and hear everything that happens there, unless the story says that a person missed it. People outside the attic see and hear nothing of it, unless the story says so.
- Everyone in the attic can see who else is in the attic.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Steps you can write, each as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the padlock to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the attic, which shows where the padlock really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the attic that the padlock is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the padlock is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the attic at that step, NAME included. "missed_by" lists people in the attic who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the attic who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the attic freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["blue drawer", "canvas sack", "white cabinet", "grey locker"]. The names are: ["Bruno", "Chidi", "Farah", "Hana", "Yara"].

Targets. After your last step, all of these must be true:
1. The padlock is really in the blue drawer.
2. Chidi thinks the padlock is in the blue drawer.
3. Farah thinks the padlock is in the blue drawer.
4. Hana thinks the padlock is in the blue drawer.
5. Yara thinks the padlock is in the white cabinet.
6. Bruno thinks the padlock is in the blue drawer.
7. Chidi thinks that Farah thinks the padlock is in the blue drawer.
8. Chidi thinks that Farah thinks that Chidi thinks the padlock is in the blue drawer.
9. Chidi thinks that Farah thinks that Chidi thinks that Yara thinks the padlock is in the canvas sack.
10. Yara thinks that Hana thinks the padlock is in the white cabinet.
11. Yara thinks that Hana thinks that Chidi thinks the padlock is in the white cabinet.
12. Yara thinks that Hana thinks that Chidi thinks that Farah thinks the padlock is in the canvas sack.

Write at least 1 and at most 5 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Chidi", "value": "grey locker", "present": ["Bruno", "Chidi", "Hana"], "missed_by": ["Bruno"], "secret_witnesses": []}, {"step": "change", "who": "Chidi", "value": "white cabinet", "present": ["Chidi"], "missed_by": [], "secret_witnesses": []}, {"step": "check", "who": "Yara", "present": ["Chidi", "Hana", "Yara"], "missed_by": ["Hana"], "secret_witnesses": []}, {"step": "change", "who": "Hana", "value": "blue drawer", "present": ["Chidi", "Hana"], "missed_by": [], "secret_witnesses": []}, {"step": "check", "who": "Hana", "present": ["Chidi", "Farah", "Hana"], "missed_by": [], "secret_witnesses": ["Bruno"]}]`

## plan-L3-005 (workplace, seed 5530011)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Goran, Pablo, Viktor, Hana and Mirela work on the same team. This is what happened, in order.
1. Call with Goran, Pablo, Viktor, Hana and Mirela: Hana assigns the Marlow account to the Denver office.

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
- The values are: ["the Denver office", "the Osaka office", "the Nairobi office", "the Lisbon office"]. The names are: ["Goran", "Hana", "Mirela", "Pablo", "Viktor"].

Targets. After your last step, all of these must be true:
1. The Marlow account is really with the Nairobi office.
2. Goran thinks the Marlow account is with the Nairobi office.
3. Pablo thinks the Marlow account is with the Nairobi office.
4. Viktor thinks the Marlow account is with the Lisbon office.
5. Hana thinks the Marlow account is with the Nairobi office.
6. Mirela thinks the Marlow account is with the Denver office.
7. Mirela thinks that Viktor thinks the Marlow account is with the Osaka office.
8. Mirela thinks that Viktor thinks that Hana thinks the Marlow account is with the Osaka office.
9. Mirela thinks that Viktor thinks that Hana thinks that Pablo thinks the Marlow account is with the Denver office.
10. Goran thinks that Pablo thinks the Marlow account is with the Nairobi office.
11. Goran thinks that Pablo thinks that Hana thinks the Marlow account is with the Nairobi office.
12. Goran thinks that Pablo thinks that Hana thinks that Viktor thinks the Marlow account is with the Osaka office.

Write at least 1 and at most 6 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Mirela", "value": "the Osaka office", "present": ["Goran", "Hana", "Mirela", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Goran", "value": "the Nairobi office", "present": ["Goran", "Hana", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Hana", "value": "the Osaka office", "present": ["Goran", "Hana", "Pablo", "Viktor"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Viktor", "value": "the Lisbon office", "present": ["Hana", "Pablo", "Viktor"], "missed_by": ["Hana"], "secret_witnesses": []}, {"step": "change", "who": "Pablo", "value": "the Denver office", "present": ["Hana", "Pablo"], "missed_by": ["Hana"], "secret_witnesses": ["Mirela"]}, {"step": "change", "who": "Hana", "value": "the Nairobi office", "present": ["Goran", "Hana", "Pablo"], "missed_by": [], "secret_witnesses": []}]`

## plan-L4-000 (classic, seed 5540001)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Jonas, Yara, Ines, Wanjiru, Keiko and Tariq share a house. The greenhouse has four closed containers that nobody can see into: the wicker basket, the black trunk, the green cupboard and the grey locker. This is what happened, in order.
1. Jonas, Yara, Ines, Wanjiru, Keiko and Tariq are in the greenhouse. Yara takes a torch out of a pocket and puts it in the black trunk.

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
- The values are: ["wicker basket", "black trunk", "green cupboard", "grey locker"]. The names are: ["Ines", "Jonas", "Keiko", "Tariq", "Wanjiru", "Yara"].

Targets. After your last step, all of these must be true:
1. The torch is really in the grey locker.
2. Jonas thinks the torch is in the grey locker.
3. Yara thinks the torch is in the grey locker.
4. Ines thinks the torch is in the grey locker.
5. Wanjiru thinks the torch is in the grey locker.
6. Keiko thinks the torch is in the grey locker.
7. Tariq thinks the torch is in the grey locker.
8. Tariq thinks that Yara thinks the torch is in the grey locker.
9. Tariq thinks that Yara thinks that Keiko thinks the torch is in the grey locker.
10. Tariq thinks that Yara thinks that Keiko thinks that Ines thinks the torch is in the wicker basket.
11. Jonas thinks that Tariq thinks the torch is in the grey locker.
12. Jonas thinks that Tariq thinks that Wanjiru thinks the torch is in the grey locker.
13. Jonas thinks that Tariq thinks that Wanjiru thinks that Ines thinks the torch is in the green cupboard.
14. Ines thinks that Tariq thinks the torch is in the grey locker.
15. Ines thinks that Tariq thinks that Ines thinks the torch is in the grey locker.
16. Ines thinks that Tariq thinks that Ines thinks that Jonas thinks the torch is in the green cupboard.

Write at least 1 and at most 5 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Wanjiru", "value": "green cupboard", "present": ["Ines", "Jonas", "Keiko", "Wanjiru", "Yara"], "missed_by": ["Yara"], "secret_witnesses": ["Tariq"]}, {"step": "change", "who": "Jonas", "value": "wicker basket", "present": ["Ines", "Jonas", "Keiko", "Tariq", "Wanjiru", "Yara"], "missed_by": ["Yara"], "secret_witnesses": []}, {"step": "change", "who": "Keiko", "value": "green cupboard", "present": ["Ines", "Jonas", "Keiko", "Tariq", "Wanjiru", "Yara"], "missed_by": ["Tariq"], "secret_witnesses": []}, {"step": "change", "who": "Wanjiru", "value": "grey locker", "present": ["Jonas", "Keiko", "Tariq", "Wanjiru", "Yara"], "missed_by": [], "secret_witnesses": ["Ines"]}, {"step": "message", "from": "Tariq", "to": "Ines", "value": "grey locker", "secret_readers": []}]`

## plan-L4-001 (workplace, seed 5540002)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Goran, Oksana, Quinn, Chidi, Uma and Ines work on the same team. This is what happened, in order.
1. Call with Goran, Oksana, Quinn, Chidi, Uma and Ines: Chidi fixes Graz as the place for the team offsite.

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
- The values are: ["Graz", "Turin", "Leeds", "Ghent"]. The names are: ["Chidi", "Goran", "Ines", "Oksana", "Quinn", "Uma"].

Targets. After your last step, all of these must be true:
1. The team offsite is really in Leeds.
2. Goran thinks the team offsite is in Leeds.
3. Oksana thinks the team offsite is in Leeds.
4. Quinn thinks the team offsite is in Leeds.
5. Chidi thinks the team offsite is in Leeds.
6. Uma thinks the team offsite is in Leeds.
7. Ines thinks the team offsite is in Leeds.
8. Quinn thinks that Uma thinks the team offsite is in Leeds.
9. Quinn thinks that Uma thinks that Quinn thinks the team offsite is in Leeds.
10. Quinn thinks that Uma thinks that Quinn thinks that Ines thinks the team offsite is in Turin.
11. Ines thinks that Chidi thinks the team offsite is in Leeds.
12. Ines thinks that Chidi thinks that Ines thinks the team offsite is in Leeds.
13. Ines thinks that Chidi thinks that Ines thinks that Quinn thinks the team offsite is in Turin.
14. Oksana thinks that Uma thinks the team offsite is in Turin.
15. Oksana thinks that Uma thinks that Goran thinks the team offsite is in Turin.
16. Oksana thinks that Uma thinks that Goran thinks that Chidi thinks the team offsite is in Graz.

Write at least 1 and at most 7 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Chidi", "value": "Turin", "present": ["Chidi", "Goran", "Ines", "Quinn", "Uma"], "missed_by": [], "secret_witnesses": []}, {"step": "check", "who": "Uma", "present": ["Goran", "Quinn", "Uma"], "missed_by": [], "secret_witnesses": ["Oksana"]}, {"step": "message", "from": "Goran", "to": "Oksana", "value": "Leeds", "secret_readers": []}, {"step": "message", "from": "Ines", "to": "Chidi", "value": "Leeds", "secret_readers": ["Quinn"]}, {"step": "message", "from": "Quinn", "to": "Uma", "value": "Leeds", "secret_readers": []}, {"step": "change", "who": "Quinn", "value": "Graz", "present": ["Goran", "Ines", "Quinn"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Quinn", "value": "Leeds", "present": ["Goran", "Ines", "Quinn"], "missed_by": [], "secret_witnesses": ["Chidi"]}]`

## plan-L4-002 (classic, seed 5540004)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Oksana, Bruno, Mirela, Luca, Ines and Keiko share a house. The study has four closed containers that nobody can see into: the canvas sack, the wicker basket, the red box and the wooden chest. This is what happened, in order.
1. Oksana, Bruno, Mirela, Luca, Ines and Keiko are in the study. Luca takes a token out of a pocket and puts it in the wicker basket.

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
  NAME moves the token to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the study, which shows where the token really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the study that the token is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the token is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the study at that step, NAME included. "missed_by" lists people in the study who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the study who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the study freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["canvas sack", "wicker basket", "red box", "wooden chest"]. The names are: ["Bruno", "Ines", "Keiko", "Luca", "Mirela", "Oksana"].

Targets. After your last step, all of these must be true:
1. The token is really in the red box.
2. Oksana thinks the token is in the red box.
3. Bruno thinks the token is in the red box.
4. Mirela thinks the token is in the red box.
5. Luca thinks the token is in the red box.
6. Ines thinks the token is in the red box.
7. Keiko thinks the token is in the red box.
8. Ines thinks that Oksana thinks the token is in the red box.
9. Ines thinks that Oksana thinks that Bruno thinks the token is in the red box.
10. Ines thinks that Oksana thinks that Bruno thinks that Luca thinks the token is in the wooden chest.
11. Mirela thinks that Bruno thinks the token is in the red box.
12. Mirela thinks that Bruno thinks that Oksana thinks the token is in the red box.
13. Mirela thinks that Bruno thinks that Oksana thinks that Ines thinks the token is in the wooden chest.
14. Luca thinks that Bruno thinks the token is in the red box.
15. Luca thinks that Bruno thinks that Oksana thinks the token is in the red box.
16. Luca thinks that Bruno thinks that Oksana thinks that Ines thinks the token is in the wooden chest.

Write at least 1 and at most 7 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Bruno", "value": "wooden chest", "present": ["Bruno", "Ines", "Keiko", "Luca", "Mirela", "Oksana"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Mirela", "value": "red box", "present": ["Bruno", "Keiko", "Luca", "Mirela", "Oksana"], "missed_by": ["Luca"], "secret_witnesses": []}, {"step": "check", "who": "Bruno", "present": ["Bruno", "Keiko", "Luca", "Mirela", "Oksana"], "missed_by": ["Keiko"], "secret_witnesses": []}, {"step": "change", "who": "Oksana", "value": "wooden chest", "present": ["Bruno", "Keiko", "Mirela", "Oksana"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Keiko", "value": "red box", "present": ["Bruno", "Keiko", "Oksana"], "missed_by": [], "secret_witnesses": []}, {"step": "check", "who": "Keiko", "present": ["Bruno", "Keiko", "Oksana"], "missed_by": [], "secret_witnesses": ["Mirela"]}, {"step": "check", "who": "Keiko", "present": ["Bruno", "Ines", "Keiko", "Oksana"], "missed_by": [], "secret_witnesses": []}]`

## plan-L4-003 (workplace, seed 5540006)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Ines, Luca, Yara, Bruno, Jonas and Mirela work on the same team. This is what happened, in order.
1. Call with Ines, Luca, Yara, Bruno, Jonas and Mirela: Ines assigns the Marlow account to the Osaka office.

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
- The values are: ["the Lisbon office", "the Denver office", "the Nairobi office", "the Osaka office"]. The names are: ["Bruno", "Ines", "Jonas", "Luca", "Mirela", "Yara"].

Targets. After your last step, all of these must be true:
1. The Marlow account is really with the Nairobi office.
2. Ines thinks the Marlow account is with the Osaka office.
3. Luca thinks the Marlow account is with the Nairobi office.
4. Yara thinks the Marlow account is with the Denver office.
5. Bruno thinks the Marlow account is with the Nairobi office.
6. Jonas thinks the Marlow account is with the Osaka office.
7. Mirela thinks the Marlow account is with the Nairobi office.
8. Bruno thinks that Jonas thinks the Marlow account is with the Nairobi office.
9. Bruno thinks that Jonas thinks that Yara thinks the Marlow account is with the Denver office.
10. Bruno thinks that Jonas thinks that Yara thinks that Mirela thinks the Marlow account is with the Lisbon office.
11. Jonas thinks that Luca thinks the Marlow account is with the Osaka office.
12. Jonas thinks that Luca thinks that Yara thinks the Marlow account is with the Denver office.
13. Jonas thinks that Luca thinks that Yara thinks that Mirela thinks the Marlow account is with the Osaka office.
14. Ines thinks that Jonas thinks the Marlow account is with the Osaka office.
15. Ines thinks that Jonas thinks that Ines thinks the Marlow account is with the Osaka office.
16. Ines thinks that Jonas thinks that Ines thinks that Yara thinks the Marlow account is with the Lisbon office.

Write at least 1 and at most 7 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Bruno", "value": "the Lisbon office", "present": ["Bruno", "Ines", "Jonas", "Luca", "Mirela", "Yara"], "missed_by": ["Jonas"], "secret_witnesses": []}, {"step": "message", "from": "Bruno", "to": "Mirela", "value": "the Nairobi office", "secret_readers": []}, {"step": "change", "who": "Luca", "value": "the Denver office", "present": ["Bruno", "Jonas", "Luca", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Luca", "to": "Ines", "value": "the Osaka office", "secret_readers": []}, {"step": "change", "who": "Bruno", "value": "the Osaka office", "present": ["Bruno", "Jonas", "Luca"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Ines", "to": "Jonas", "value": "the Osaka office", "secret_readers": []}, {"step": "change", "who": "Luca", "value": "the Nairobi office", "present": ["Bruno", "Jonas", "Luca"], "missed_by": ["Jonas"], "secret_witnesses": []}]`

## plan-L4-004 (classic, seed 5540008)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Hana, Yara, Keiko, Emeka, Oksana and Rania share a house. The garage has four closed containers that nobody can see into: the canvas sack, the blue drawer, the white cabinet and the red box. This is what happened, in order.
1. Hana, Yara, Keiko, Emeka, Oksana and Rania are in the garage. Keiko takes a brooch out of a pocket and puts it in the white cabinet.

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
  NAME moves the brooch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the garage, which shows where the brooch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the garage that the brooch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the brooch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the garage at that step, NAME included. "missed_by" lists people in the garage who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the garage who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the garage freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["canvas sack", "blue drawer", "white cabinet", "red box"]. The names are: ["Emeka", "Hana", "Keiko", "Oksana", "Rania", "Yara"].

Targets. After your last step, all of these must be true:
1. The brooch is really in the blue drawer.
2. Hana thinks the brooch is in the red box.
3. Yara thinks the brooch is in the canvas sack.
4. Keiko thinks the brooch is in the canvas sack.
5. Emeka thinks the brooch is in the blue drawer.
6. Oksana thinks the brooch is in the blue drawer.
7. Rania thinks the brooch is in the blue drawer.
8. Emeka thinks that Keiko thinks the brooch is in the red box.
9. Emeka thinks that Keiko thinks that Oksana thinks the brooch is in the red box.
10. Emeka thinks that Keiko thinks that Oksana thinks that Hana thinks the brooch is in the white cabinet.
11. Rania thinks that Oksana thinks the brooch is in the blue drawer.
12. Rania thinks that Oksana thinks that Emeka thinks the brooch is in the blue drawer.
13. Rania thinks that Oksana thinks that Emeka thinks that Hana thinks the brooch is in the white cabinet.
14. Oksana thinks that Keiko thinks the brooch is in the blue drawer.
15. Oksana thinks that Keiko thinks that Yara thinks the brooch is in the blue drawer.
16. Oksana thinks that Keiko thinks that Yara thinks that Hana thinks the brooch is in the white cabinet.

Write at least 1 and at most 9 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Hana", "value": "canvas sack", "present": ["Emeka", "Hana", "Keiko", "Oksana", "Rania", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Oksana", "value": "white cabinet", "present": ["Emeka", "Hana", "Keiko", "Oksana", "Rania", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Emeka", "value": "red box", "present": ["Emeka", "Hana", "Oksana", "Rania", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Oksana", "value": "white cabinet", "present": ["Emeka", "Hana", "Oksana", "Rania", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Yara", "value": "blue drawer", "present": ["Emeka", "Oksana", "Yara"], "missed_by": [], "secret_witnesses": ["Rania"]}, {"step": "say", "who": "Yara", "value": "blue drawer", "present": ["Emeka", "Keiko", "Oksana", "Yara"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Yara", "value": "red box", "present": ["Emeka", "Keiko", "Oksana", "Yara"], "missed_by": ["Oksana"], "secret_witnesses": ["Hana"]}, {"step": "change", "who": "Oksana", "value": "canvas sack", "present": ["Emeka", "Oksana", "Yara"], "missed_by": [], "secret_witnesses": ["Keiko"]}, {"step": "change", "who": "Oksana", "value": "blue drawer", "present": ["Emeka", "Oksana", "Yara"], "missed_by": ["Yara"], "secret_witnesses": []}]`

## plan-L4-005 (workplace, seed 5540009)

You direct a short scene. Write the steps that make a list of target beliefs come true.

Scene so far:
Emeka, Jonas, Mirela, Farah, Keiko and Ines work on the same team. This is what happened, in order.
1. Call with Emeka, Jonas, Mirela, Farah, Keiko and Ines: Jonas sets the discount on the Fenwick quote at 10%.

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
- The values are: ["5%", "25%", "10%", "20%"]. The names are: ["Emeka", "Farah", "Ines", "Jonas", "Keiko", "Mirela"].

Targets. After your last step, all of these must be true:
1. The discount on the Fenwick quote is really 25%.
2. Emeka thinks the discount on the Fenwick quote is 25%.
3. Jonas thinks the discount on the Fenwick quote is 25%.
4. Mirela thinks the discount on the Fenwick quote is 25%.
5. Farah thinks the discount on the Fenwick quote is 25%.
6. Keiko thinks the discount on the Fenwick quote is 25%.
7. Ines thinks the discount on the Fenwick quote is 25%.
8. Mirela thinks that Emeka thinks the discount on the Fenwick quote is 25%.
9. Mirela thinks that Emeka thinks that Mirela thinks the discount on the Fenwick quote is 25%.
10. Mirela thinks that Emeka thinks that Mirela thinks that Farah thinks the discount on the Fenwick quote is 10%.
11. Ines thinks that Emeka thinks the discount on the Fenwick quote is 25%.
12. Ines thinks that Emeka thinks that Mirela thinks the discount on the Fenwick quote is 25%.
13. Ines thinks that Emeka thinks that Mirela thinks that Farah thinks the discount on the Fenwick quote is 10%.
14. Keiko thinks that Emeka thinks the discount on the Fenwick quote is 25%.
15. Keiko thinks that Emeka thinks that Jonas thinks the discount on the Fenwick quote is 25%.
16. Keiko thinks that Emeka thinks that Jonas thinks that Farah thinks the discount on the Fenwick quote is 10%.

Write at least 1 and at most 7 steps. Any script that makes every target true is accepted.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array of your steps.

reference: `[{"step": "change", "who": "Emeka", "value": "20%", "present": ["Emeka", "Farah", "Ines", "Keiko", "Mirela"], "missed_by": ["Mirela"], "secret_witnesses": []}, {"step": "change", "who": "Jonas", "value": "10%", "present": ["Emeka", "Farah", "Ines", "Jonas", "Keiko", "Mirela"], "missed_by": ["Emeka"], "secret_witnesses": []}, {"step": "change", "who": "Jonas", "value": "20%", "present": ["Emeka", "Ines", "Jonas", "Keiko", "Mirela"], "missed_by": ["Mirela"], "secret_witnesses": []}, {"step": "change", "who": "Ines", "value": "5%", "present": ["Emeka", "Ines", "Jonas", "Keiko", "Mirela"], "missed_by": [], "secret_witnesses": ["Farah"]}, {"step": "change", "who": "Emeka", "value": "20%", "present": ["Emeka", "Ines", "Jonas", "Keiko", "Mirela"], "missed_by": [], "secret_witnesses": []}, {"step": "change", "who": "Keiko", "value": "25%", "present": ["Emeka", "Ines", "Jonas", "Keiko", "Mirela"], "missed_by": [], "secret_witnesses": []}, {"step": "message", "from": "Mirela", "to": "Farah", "value": "25%", "secret_readers": []}]`

## explain-L1-000 (classic, seed 5710001)

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
Ines, Quinn, Nadim and Rania share a house. The cellar has four closed containers that nobody can see into: the canvas sack, the blue drawer, the grey locker and the wicker basket. This is what happened, in order.
1. Ines, Quinn, Nadim and Rania are in the cellar. Nadim takes a brooch out of a pocket and puts it in the blue drawer.
2. Ines, Quinn and Rania are in the cellar. Rania moves the brooch to the wicker basket. Ines is in the cellar but is absorbed in a phone and does not notice this. Nobody realises that Ines missed it.
3. [A step is missing here.]
4. Ines, Quinn and Rania are in the cellar. Ines moves the brooch to the blue drawer.
5. Ines, Quinn and Rania are in the cellar. Ines moves the brooch to the wicker basket.
6. Ines sends Nadim a private text message: “The brooch is in the wicker basket.”
7. Ines, Quinn and Rania are in the cellar. Quinn moves the brooch to the canvas sack.

Facts at the end of the story:
1. The brooch is really in the canvas sack.
2. Quinn thinks that Nadim thinks the brooch is in the canvas sack.
3. Rania thinks that Nadim thinks the brooch is in the blue drawer.
4. Nadim thinks that Quinn thinks the brooch is in the canvas sack.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the brooch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the cellar, which shows where the brooch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the cellar that the brooch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the brooch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the cellar at that step, NAME included. "missed_by" lists people in the cellar who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the cellar who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the cellar freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["canvas sack", "blue drawer", "grey locker", "wicker basket"]. The names are: ["Ines", "Nadim", "Quinn", "Rania"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Quinn", "to": "Nadim", "value": "canvas sack", "secret_readers": []}]`

## explain-L1-001 (workplace, seed 5710003)

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
Emeka, Farah, Luca and Viktor work on the same team. This is what happened, in order.
1. Call with Emeka, Farah, Luca and Viktor: Luca sets the discount on the Fenwick quote at 5%.
2. Call with Emeka, Farah, Luca and Viktor: Farah changes the discount on the Fenwick quote to 15%.
3. Call with Emeka, Farah, Luca and Viktor: Farah changes the discount on the Fenwick quote to 25%.
4. Call with Emeka, Farah, Luca and Viktor: Viktor changes the discount on the Fenwick quote to 10%.
5. [A step is missing here.]
6. Call with Emeka and Luca: Luca changes the discount on the Fenwick quote to 25%. Emeka is on the call but has stepped away from the desk and misses this. Nobody realises that Emeka missed it.
7. Emeka sends Viktor a direct message: “The discount on the Fenwick quote is 5%.”

Facts at the end of the story:
1. The discount on the Fenwick quote is really 25%.
2. Luca thinks that Farah thinks the discount on the Fenwick quote is 5%.
3. Farah thinks that Emeka thinks the discount on the Fenwick quote is 5%.
4. Viktor thinks that Farah thinks the discount on the Fenwick quote is 10%.

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
- The values are: ["15%", "25%", "5%", "10%"]. The names are: ["Emeka", "Farah", "Luca", "Viktor"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Luca", "value": "5%", "present": ["Emeka", "Farah", "Luca"], "missed_by": [], "secret_witnesses": []}]`

## explain-L1-002 (classic, seed 5710004)

One step of this story is missing. Work out a step that fits the gap.

Rules of the story world:
- Nobody can see into a closed container. A person learns where a thing is only by watching it being put there, by seeing inside the containers, or by being told.
- People in the attic see and hear everything that happens there, unless the story says that a person missed it. People outside the attic see and hear nothing of it, unless the story says so.
- Everyone in the attic can see who else is in the attic.
- Text messages are private. The person who gets one reads it at once, and the sender knows this.
- People say what they believe, unless the story says that they want to mislead.
- People believe what they see. They also believe what they are told and what they overhear. Nobody suspects a lie or a mistake. Newer information replaces what a person believed before.
- Nobody learns, guesses, works out or passes on anything that the story does not describe. For example, a person who hears that something has changed does not work out who changed it or who else knows.

Story:
Xavier, Wanjiru, Soren and Yara share a house. The attic has four closed containers that nobody can see into: the grey locker, the wooden chest, the leather bag and the blue drawer. This is what happened, in order.
1. Xavier, Wanjiru, Soren and Yara are in the attic. Wanjiru takes a stopwatch out of a pocket and puts it in the wooden chest.
2. Xavier, Wanjiru, Soren and Yara are in the attic. Yara moves the stopwatch to the leather bag. Soren is in the attic but is absorbed in a phone and does not notice this. Nobody realises that Soren missed it.
3. Xavier, Wanjiru and Yara are in the attic. Xavier moves the stopwatch to the grey locker.
4. [A step is missing here.]
5. Xavier wants to mislead Soren, so Xavier sends Soren a private text message: “The stopwatch is in the blue drawer.”
6. Wanjiru sends Soren a private text message: “The stopwatch is in the grey locker.”
7. Xavier and Yara are in the attic. Yara moves the stopwatch to the wooden chest. Xavier is in the attic but is absorbed in a phone and does not notice this. Nobody realises that Xavier missed it.

Facts at the end of the story:
1. The stopwatch is really in the wooden chest.
2. Yara thinks that Soren thinks the stopwatch is in the wooden chest.
3. Yara thinks that Wanjiru thinks the stopwatch is in the grey locker.
4. Xavier thinks that Yara thinks the stopwatch is in the grey locker.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the stopwatch to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the attic, which shows where the stopwatch really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the attic that the stopwatch is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the stopwatch is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the attic at that step, NAME included. "missed_by" lists people in the attic who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the attic who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the attic freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["grey locker", "wooden chest", "leather bag", "blue drawer"]. The names are: ["Soren", "Wanjiru", "Xavier", "Yara"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Yara", "to": "Soren", "value": "wooden chest", "secret_readers": []}]`

## explain-L1-003 (workplace, seed 5710005)

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
Soren, Emeka, Yara and Xavier work on the same team. This is what happened, in order.
1. Call with Soren, Emeka, Yara and Xavier: Emeka assigns the Marlow account to the Lisbon office.
2. Call with Soren and Yara: Soren reassigns the Marlow account to the Osaka office. Yara is on the call but has stepped away from the desk and misses this. Nobody realises that Yara missed it.
3. [A step is missing here.]
4. Soren sends Emeka a direct message: “The Marlow account is with the Osaka office.”
5. Emeka wants to mislead Yara, so Emeka sends Yara a direct message: “The Marlow account is with the Nairobi office.”
6. Call with Soren, Emeka and Yara: Yara opens the account list and reads it out: “The Marlow account is with the Osaka office.”
7. Emeka sends Xavier a direct message: “The Marlow account is with the Osaka office.” Yara secretly reads this message on Xavier's screen. Neither Emeka nor Xavier ever knows that Yara read it.

Facts at the end of the story:
1. The Marlow account is really with the Osaka office.
2. Soren thinks that Xavier thinks the Marlow account is with the Denver office.
3. Xavier thinks that Soren thinks the Marlow account is with the Denver office.
4. Xavier thinks that Yara thinks the Marlow account is with the Lisbon office.

The missing step is one of these types, each written as one JSON object:
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
- The values are: ["the Osaka office", "the Lisbon office", "the Nairobi office", "the Denver office"]. The names are: ["Emeka", "Soren", "Xavier", "Yara"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Soren", "to": "Xavier", "value": "the Denver office", "secret_readers": []}]`

## explain-L1-004 (classic, seed 5710007)

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
Uma, Dalia, Hana and Soren share a house. The workshop has four closed containers that nobody can see into: the leather bag, the grey locker, the white cabinet and the red box. This is what happened, in order.
1. Uma, Dalia, Hana and Soren are in the workshop. Hana takes a torch out of a pocket and puts it in the grey locker.
2. [A step is missing here.]
3. Hana wants to mislead Uma, so Hana sends Uma a private text message: “The torch is in the red box.”
4. Dalia and Soren are in the workshop. Soren opens every container in full view of the workshop, showing that the torch is in the white cabinet.
5. Dalia and Soren are in the workshop. Dalia moves the torch to the red box. Soren is in the workshop but is absorbed in a phone and does not notice this. Nobody realises that Soren missed it.
6. Uma sends Soren a private text message: “The torch is in the red box.”
7. Uma sends Dalia a private text message: “The torch is in the red box.”

Facts at the end of the story:
1. The torch is really in the red box.
2. Hana thinks that Dalia thinks the torch is in the white cabinet.
3. Dalia thinks that Hana thinks the torch is in the white cabinet.
4. Hana thinks that Soren thinks the torch is in the grey locker.

The missing step is one of these types, each written as one JSON object:
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
- The values are: ["leather bag", "grey locker", "white cabinet", "red box"]. The names are: ["Dalia", "Hana", "Soren", "Uma"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Dalia", "value": "white cabinet", "present": ["Dalia", "Hana"], "missed_by": [], "secret_witnesses": []}]`

## explain-L1-005 (workplace, seed 5710008)

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
Ines, Hana, Farah and Luca work on the same team. This is what happened, in order.
1. Call with Ines, Hana, Farah and Luca: Farah picks Ironbridge as the packaging supplier.
2. Call with Ines, Hana, Farah and Luca: Ines switches the packaging supplier to Brightwater.
3. Call with Ines, Hana and Farah: Hana switches the packaging supplier to Halcyon. Farah is on the call but has stepped away from the desk and misses this. Nobody realises that Farah missed it.
4. Ines sends Luca a direct message: “The packaging supplier is Halcyon.”
5. Call with Hana and Farah: Hana opens the supplier register and reads it out: “The packaging supplier is Halcyon.”
6. [A step is missing here.]
7. Hana wants to mislead Ines, so Hana sends Ines a direct message: “The packaging supplier is Ironbridge.”

Facts at the end of the story:
1. The packaging supplier is really Brightwater.
2. Luca thinks the packaging supplier is Halcyon.
3. Farah thinks that Hana thinks the packaging supplier is Brightwater.
4. Hana thinks that Farah thinks the packaging supplier is Brightwater.

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
- The values are: ["Sablewood", "Brightwater", "Ironbridge", "Halcyon"]. The names are: ["Farah", "Hana", "Ines", "Luca"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Farah", "value": "Brightwater", "present": ["Farah", "Hana"], "missed_by": [], "secret_witnesses": []}]`

## explain-L2-000 (classic, seed 5720001)

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
Hana, Goran, Chidi, Yara and Keiko share a house. The garage has four closed containers that nobody can see into: the white cabinet, the wooden chest, the green cupboard and the black trunk. This is what happened, in order.
1. Hana, Goran, Chidi, Yara and Keiko are in the garage. Keiko takes a magnet out of a pocket and puts it in the wooden chest.
2. Goran, Yara and Keiko are in the garage. Yara moves the magnet to the white cabinet.
3. Goran, Yara and Keiko are in the garage. Yara moves the magnet to the black trunk.
4. [A step is missing here.]
5. Goran, Yara and Keiko are in the garage. Yara moves the magnet to the white cabinet.
6. Keiko is alone in the garage. Keiko moves the magnet to the green cupboard.
7. Keiko is alone in the garage. Keiko moves the magnet to the wooden chest. Hana is outside but watches all of this through the window. Nobody knows that Hana is watching.
8. Yara and Keiko are in the garage. Keiko opens every container in full view of the garage, showing that the magnet is in the wooden chest.
9. Keiko sends Goran a private text message: “The magnet is in the wooden chest.” Yara secretly reads this message on Goran's phone. Neither Keiko nor Goran ever knows that Yara read it.

Facts at the end of the story:
1. The magnet is really in the wooden chest.
2. Keiko thinks that Chidi thinks that Keiko thinks the magnet is in the white cabinet.
3. Chidi thinks the magnet is in the white cabinet.
4. Yara thinks that Chidi thinks that Keiko thinks the magnet is in the wooden chest.
5. Goran thinks that Chidi thinks the magnet is in the wooden chest.
6. Hana thinks that Chidi thinks the magnet is in the wooden chest.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the magnet to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the garage, which shows where the magnet really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the garage that the magnet is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the magnet is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the garage at that step, NAME included. "missed_by" lists people in the garage who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the garage who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the garage freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["white cabinet", "wooden chest", "green cupboard", "black trunk"]. The names are: ["Chidi", "Goran", "Hana", "Keiko", "Yara"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Keiko", "to": "Chidi", "value": "white cabinet", "secret_readers": []}]`

## explain-L2-001 (workplace, seed 5720003)

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
Soren, Keiko, Hana, Chidi and Nadim work on the same team. This is what happened, in order.
1. Call with Soren, Keiko, Hana, Chidi and Nadim: Keiko assigns the Marlow account to the Denver office.
2. Call with Soren, Keiko, Hana, Chidi and Nadim: Hana reassigns the Marlow account to the Lisbon office.
3. Call with Hana, Chidi and Nadim: Nadim reassigns the Marlow account to the Osaka office. Hana is on the call but has stepped away from the desk and misses this. Nobody realises that Hana missed it.
4. [A step is missing here.]
5. Nadim sends Soren a direct message: “The Marlow account is with the Osaka office.”
6. Keiko sends Chidi a direct message: “The Marlow account is with the Osaka office.”
7. Soren sends Hana a direct message: “The Marlow account is with the Osaka office.”
8. Soren sends Chidi a direct message: “The Marlow account is with the Osaka office.”
9. Call with Hana, Chidi and Nadim: Chidi reassigns the Marlow account to the Nairobi office.

Facts at the end of the story:
1. The Marlow account is really with the Nairobi office.
2. Soren thinks that Nadim thinks that Keiko thinks the Marlow account is with the Osaka office.
3. Soren thinks that Keiko thinks that Soren thinks the Marlow account is with the Lisbon office.
4. Chidi thinks that Keiko thinks that Nadim thinks the Marlow account is with the Lisbon office.
5. Hana thinks that Keiko thinks the Marlow account is with the Lisbon office.
6. Keiko thinks that Hana thinks that Keiko thinks the Marlow account is with the Lisbon office.

The missing step is one of these types, each written as one JSON object:
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
- The values are: ["the Nairobi office", "the Denver office", "the Lisbon office", "the Osaka office"]. The names are: ["Chidi", "Hana", "Keiko", "Nadim", "Soren"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Nadim", "to": "Keiko", "value": "the Osaka office", "secret_readers": ["Soren"]}]`

## explain-L2-002 (classic, seed 5720004)

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
Mirela, Pablo, Tariq, Xavier and Dalia share a house. The cellar has four closed containers that nobody can see into: the black trunk, the wicker basket, the red box and the grey locker. This is what happened, in order.
1. Mirela, Pablo, Tariq, Xavier and Dalia are in the cellar. Mirela takes a whistle out of a pocket and puts it in the grey locker.
2. Mirela, Pablo, Tariq, Xavier and Dalia are in the cellar. Mirela moves the whistle to the wicker basket.
3. Mirela, Pablo, Tariq, Xavier and Dalia are in the cellar. Pablo moves the whistle to the grey locker.
4. Mirela, Pablo, Tariq, Xavier and Dalia are in the cellar. Pablo moves the whistle to the wicker basket. Mirela is in the cellar but is absorbed in a phone and does not notice this. Nobody realises that Mirela missed it.
5. Mirela, Pablo, Tariq, Xavier and Dalia are in the cellar. Xavier opens every container in full view of the cellar, showing that the whistle is in the wicker basket.
6. Mirela, Pablo, Tariq, Xavier and Dalia are in the cellar. Dalia moves the whistle to the grey locker. Pablo is in the cellar but is absorbed in a phone and does not notice this. Nobody realises that Pablo missed it.
7. Pablo, Tariq and Dalia are in the cellar. Pablo moves the whistle to the black trunk. Tariq is in the cellar but is absorbed in a phone and does not notice this. Nobody realises that Tariq missed it. Xavier is outside but watches all of this through the window. Nobody knows that Xavier is watching.
8. [A step is missing here.]
9. Tariq sends Xavier a private text message: “The whistle is in the black trunk.” Pablo secretly reads this message on Xavier's phone. Neither Tariq nor Xavier ever knows that Pablo read it.

Facts at the end of the story:
1. The whistle is really in the black trunk.
2. Dalia thinks that Mirela thinks that Pablo thinks the whistle is in the black trunk.
3. Mirela thinks that Tariq thinks that Dalia thinks the whistle is in the black trunk.
4. Xavier thinks that Pablo thinks that Mirela thinks the whistle is in the grey locker.
5. Dalia thinks that Xavier thinks that Tariq thinks the whistle is in the grey locker.
6. Pablo thinks that Mirela thinks the whistle is in the black trunk.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the whistle to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the cellar, which shows where the whistle really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the cellar that the whistle is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the whistle is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the cellar at that step, NAME included. "missed_by" lists people in the cellar who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the cellar who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the cellar freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["black trunk", "wicker basket", "red box", "grey locker"]. The names are: ["Dalia", "Mirela", "Pablo", "Tariq", "Xavier"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "say", "who": "Pablo", "value": "black trunk", "present": ["Dalia", "Mirela", "Pablo", "Tariq"], "missed_by": [], "secret_witnesses": []}]`

## explain-L2-003 (workplace, seed 5720005)

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
Pablo, Yara, Xavier, Oksana and Quinn work on the same team. This is what happened, in order.
1. Call with Pablo, Yara, Xavier, Oksana and Quinn: Yara fixes Graz as the place for the team offsite.
2. Call with Pablo, Yara, Xavier, Oksana and Quinn: Oksana moves the team offsite to Leeds. Quinn is on the call but has stepped away from the desk and misses this. Nobody realises that Quinn missed it.
3. Call with Pablo, Xavier and Quinn: Quinn moves the team offsite to Turin. Pablo is on the call but has stepped away from the desk and misses this. Nobody realises that Pablo missed it. Yara is not on the call but secretly listens in, and can see who is on it. Nobody knows that Yara is listening.
4. Call with Pablo, Xavier and Quinn: Quinn moves the team offsite to Graz.
5. Xavier sends Yara a direct message: “The team offsite is in Graz.” Quinn secretly reads this message on Yara's screen. Neither Xavier nor Yara ever knows that Quinn read it.
6. Call with Pablo, Xavier and Quinn: Quinn moves the team offsite to Leeds.
7. [A step is missing here.]
8. Pablo, working alone, moves the team offsite to Leeds and tells nobody.
9. Call with Pablo and Quinn: Pablo moves the team offsite to Graz. Quinn is on the call but has stepped away from the desk and misses this. Nobody realises that Quinn missed it.

Facts at the end of the story:
1. The team offsite is really in Graz.
2. Quinn thinks that Pablo thinks that Quinn thinks the team offsite is in Porto.
3. Quinn thinks that Xavier thinks the team offsite is in Leeds.
4. Oksana thinks that Pablo thinks the team offsite is in Leeds.
5. Quinn thinks that Yara thinks the team offsite is in Graz.
6. Xavier thinks the team offsite is in Leeds.

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
- The values are: ["Turin", "Leeds", "Graz", "Porto"]. The names are: ["Oksana", "Pablo", "Quinn", "Xavier", "Yara"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Quinn", "value": "Porto", "present": ["Pablo", "Quinn"], "missed_by": [], "secret_witnesses": []}]`

## explain-L2-004 (classic, seed 5720006)

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
Tariq, Pablo, Hana, Goran and Oksana share a house. The boathouse has four closed containers that nobody can see into: the red box, the white cabinet, the blue drawer and the canvas sack. This is what happened, in order.
1. Tariq, Pablo, Hana, Goran and Oksana are in the boathouse. Goran takes a torch out of a pocket and puts it in the canvas sack.
2. Tariq, Pablo, Hana, Goran and Oksana are in the boathouse. Oksana moves the torch to the blue drawer.
3. [A step is missing here.]
4. Goran sends Hana a private text message: “The torch is in the white cabinet.”
5. Tariq, Pablo and Oksana are in the boathouse. Pablo moves the torch to the blue drawer.
6. Oksana sends Goran a private text message: “The torch is in the blue drawer.”
7. Goran sends Pablo a private text message: “The torch is in the blue drawer.”
8. Tariq, Pablo, Hana and Oksana are in the boathouse. Oksana moves the torch to the white cabinet. Goran is outside but watches all of this through the window. Nobody knows that Goran is watching.
9. Tariq sends Goran a private text message: “The torch is in the white cabinet.”

Facts at the end of the story:
1. The torch is really in the white cabinet.
2. Oksana thinks that Goran thinks that Pablo thinks the torch is in the white cabinet.
3. Hana thinks that Goran thinks that Pablo thinks the torch is in the blue drawer.
4. Oksana thinks that Goran thinks that Tariq thinks the torch is in the blue drawer.
5. Tariq thinks that Goran thinks that Pablo thinks the torch is in the blue drawer.
6. Oksana thinks that Goran thinks that Hana thinks the torch is in the blue drawer.

The missing step is one of these types, each written as one JSON object:
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
- The values are: ["red box", "white cabinet", "blue drawer", "canvas sack"]. The names are: ["Goran", "Hana", "Oksana", "Pablo", "Tariq"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Oksana", "value": "white cabinet", "present": ["Goran", "Oksana", "Pablo"], "missed_by": ["Pablo"], "secret_witnesses": []}]`

## explain-L2-005 (workplace, seed 5720007)

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
Viktor, Dalia, Soren, Mirela and Oksana work on the same team. This is what happened, in order.
1. Call with Viktor, Dalia, Soren, Mirela and Oksana: Mirela fixes Leeds as the place for the team offsite.
2. Call with Viktor, Dalia, Soren and Mirela: Viktor moves the team offsite to Porto.
3. Dalia sends Oksana a direct message: “The team offsite is in Porto.” Viktor secretly reads this message on Oksana's screen. Neither Dalia nor Oksana ever knows that Viktor read it.
4. Call with Viktor, Dalia, Soren, Mirela and Oksana: Soren says: “The team offsite is in Porto.”
5. Call with Viktor, Dalia, Soren and Oksana: Dalia moves the team offsite to Turin.
6. [A step is missing here.]
7. Dalia sends Mirela a direct message: “The team offsite is in Graz.”
8. Call with Dalia, Soren and Oksana: Oksana moves the team offsite to Leeds.
9. Call with Dalia, Soren, Mirela and Oksana: Dalia moves the team offsite to Graz.

Facts at the end of the story:
1. The team offsite is really in Graz.
2. Soren thinks that Viktor thinks that Oksana thinks the team offsite is in Graz.
3. Oksana thinks that Viktor thinks that Dalia thinks the team offsite is in Graz.
4. Viktor thinks that Dalia thinks that Oksana thinks the team offsite is in Turin.
5. Mirela thinks that Viktor thinks that Dalia thinks the team offsite is in Porto.
6. Oksana thinks that Mirela thinks that Viktor thinks the team offsite is in Porto.

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
- The values are: ["Graz", "Turin", "Porto", "Leeds"]. The names are: ["Dalia", "Mirela", "Oksana", "Soren", "Viktor"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Soren", "value": "Graz", "present": ["Dalia", "Oksana", "Soren", "Viktor"], "missed_by": ["Viktor"], "secret_witnesses": []}]`

## explain-L3-000 (classic, seed 5730001)

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
Quinn, Jonas, Farah, Tariq and Keiko share a house. The kitchen has four closed containers that nobody can see into: the green cupboard, the red box, the canvas sack and the grey locker. This is what happened, in order.
1. Quinn, Jonas, Farah, Tariq and Keiko are in the kitchen. Farah takes a magnet out of a pocket and puts it in the grey locker.
2. Quinn, Jonas, Farah, Tariq and Keiko are in the kitchen. Quinn moves the magnet to the green cupboard.
3. Quinn, Jonas, Farah, Tariq and Keiko are in the kitchen. Tariq moves the magnet to the grey locker.
4. Quinn, Farah and Keiko are in the kitchen. Farah moves the magnet to the green cupboard. Tariq is outside but watches all of this through the window. Nobody knows that Tariq is watching.
5. Quinn, Jonas, Farah and Keiko are in the kitchen. Farah moves the magnet to the grey locker. Jonas is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Jonas missed it.
6. Quinn, Jonas, Farah, Tariq and Keiko are in the kitchen. Farah moves the magnet to the canvas sack.
7. Quinn, Jonas, Tariq and Keiko are in the kitchen. Quinn moves the magnet to the grey locker.
8. Quinn, Jonas and Keiko are in the kitchen. Jonas moves the magnet to the canvas sack. Quinn is in the kitchen but is absorbed in a phone and does not notice this. Nobody realises that Quinn missed it.
9. Jonas sends Tariq a private text message: “The magnet is in the canvas sack.”
10. [A step is missing here.]
11. Quinn wants to mislead Farah, so Quinn sends Farah a private text message: “The magnet is in the red box.”

Facts at the end of the story:
1. The magnet is really in the grey locker.
2. Jonas thinks that Keiko thinks the magnet is in the grey locker.
3. Keiko thinks that Jonas thinks the magnet is in the grey locker.
4. Tariq thinks the magnet is in the canvas sack.
5. Farah thinks that Keiko thinks that Jonas thinks that Keiko thinks the magnet is in the canvas sack.
6. Jonas thinks that Keiko thinks that Quinn thinks the magnet is in the canvas sack.
7. Jonas thinks that Tariq thinks the magnet is in the canvas sack.
8. Keiko thinks that Farah thinks the magnet is in the canvas sack.

The missing step is one of these types, each written as one JSON object:
- {"step": "change", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME moves the magnet to PLACE, which must not be the place where it already is.
- {"step": "check", "who": NAME, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME opens every container in full view of the kitchen, which shows where the magnet really is.
- {"step": "say", "who": NAME, "value": PLACE, "present": [NAMES], "missed_by": [NAMES], "secret_witnesses": [NAMES]}
  NAME says out loud to everyone in the kitchen that the magnet is in PLACE. At least one other person must be present.
- {"step": "message", "from": NAME, "to": NAME, "value": PLACE, "secret_readers": [NAMES]}
  One person sends another a private text message that says the magnet is in PLACE.

Notes on the steps:
- "present" lists everyone who is in the kitchen at that step, NAME included. "missed_by" lists people in the kitchen who do not notice the step, while nobody realises that they missed it. "secret_witnesses" lists people outside the kitchen who watch and hear the step through the window, while nobody knows that they do. "secret_readers" lists people who read a message on the receiver's phone, while the sender and the receiver never know.
- Between steps, people go in and out of the kitchen freely. That is not a step and nobody learns anything from it.
- A "say" step or a "message" step whose value is not what the speaker believes is a deliberate lie. The people who hear or read it believe it all the same.
- The values are: ["green cupboard", "red box", "canvas sack", "grey locker"]. The names are: ["Farah", "Jonas", "Keiko", "Quinn", "Tariq"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Keiko", "value": "grey locker", "present": ["Jonas", "Keiko"], "missed_by": [], "secret_witnesses": []}]`

## explain-L3-001 (workplace, seed 5730002)

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
Quinn, Emeka, Tariq, Farah and Keiko work on the same team. This is what happened, in order.
1. Call with Quinn, Emeka, Tariq, Farah and Keiko: Farah fixes Turin as the place for the team offsite.
2. Call with Quinn, Emeka, Tariq, Farah and Keiko: Keiko moves the team offsite to Leeds.
3. Call with Emeka, Tariq and Farah: Tariq moves the team offsite to Ghent. Keiko is not on the call but secretly listens in, and can see who is on it. Nobody knows that Keiko is listening.
4. Call with Emeka, Tariq and Farah: Tariq moves the team offsite to Turin.
5. Call with Emeka, Tariq and Farah: Emeka moves the team offsite to Ghent. Quinn is not on the call but secretly listens in, and can see who is on it. Nobody knows that Quinn is listening.
6. [A step is missing here.]
7. Farah sends Keiko a direct message: “The team offsite is in Graz.”
8. Call with Tariq and Farah: Farah opens the travel plan and reads it out: “The team offsite is in Graz.”
9. Farah sends Quinn a direct message: “The team offsite is in Graz.”
10. Call with Tariq, Farah and Keiko: Farah moves the team offsite to Leeds. Keiko is on the call but has stepped away from the desk and misses this. Nobody realises that Keiko missed it.
11. Call with Farah and Keiko: Keiko moves the team offsite to Graz.

Facts at the end of the story:
1. The team offsite is really in Graz.
2. Emeka thinks that Farah thinks the team offsite is in Graz.
3. Emeka thinks that Keiko thinks the team offsite is in Leeds.
4. Emeka thinks that Farah thinks that Quinn thinks the team offsite is in Leeds.
5. Emeka thinks that Tariq thinks the team offsite is in Ghent.
6. Keiko thinks that Emeka thinks that Farah thinks the team offsite is in Ghent.
7. Farah thinks that Emeka thinks the team offsite is in Graz.
8. Tariq thinks that Emeka thinks the team offsite is in Ghent.

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
- The values are: ["Graz", "Ghent", "Turin", "Leeds"]. The names are: ["Emeka", "Farah", "Keiko", "Quinn", "Tariq"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Emeka", "value": "Graz", "present": ["Emeka", "Farah"], "missed_by": [], "secret_witnesses": []}]`

## explain-L3-002 (classic, seed 5730003)

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
Dalia, Zoltan, Mirela, Ines and Quinn share a house. The boathouse has four closed containers that nobody can see into: the red box, the green cupboard, the blue drawer and the grey locker. This is what happened, in order.
1. Dalia, Zoltan, Mirela, Ines and Quinn are in the boathouse. Zoltan takes a torch out of a pocket and puts it in the blue drawer.
2. Dalia, Zoltan, Mirela and Quinn are in the boathouse. Quinn moves the torch to the red box.
3. Dalia, Zoltan, Mirela, Ines and Quinn are in the boathouse. Zoltan moves the torch to the green cupboard.
4. Dalia, Mirela, Ines and Quinn are in the boathouse. Mirela moves the torch to the red box.
5. Dalia, Mirela, Ines and Quinn are in the boathouse. Mirela moves the torch to the green cupboard. Zoltan is outside but watches all of this through the window. Nobody knows that Zoltan is watching.
6. Dalia, Mirela, Ines and Quinn are in the boathouse. Dalia moves the torch to the red box.
7. [A step is missing here.]
8. Dalia sends Mirela a private text message: “The torch is in the grey locker.”
9. Quinn sends Zoltan a private text message: “The torch is in the red box.”
10. Ines is alone in the boathouse. Ines moves the torch to the green cupboard.
11. Ines sends Quinn a private text message: “The torch is in the green cupboard.”

Facts at the end of the story:
1. The torch is really in the green cupboard.
2. Ines thinks that Dalia thinks the torch is in the grey locker.
3. Zoltan thinks that Dalia thinks the torch is in the green cupboard.
4. Ines thinks that Dalia thinks that Quinn thinks the torch is in the red box.
5. Ines thinks that Dalia thinks that Mirela thinks that Dalia thinks the torch is in the red box.
6. Ines thinks that Zoltan thinks that Dalia thinks that Zoltan thinks the torch is in the green cupboard.
7. Mirela thinks that Ines thinks the torch is in the red box.
8. Dalia thinks that Ines thinks the torch is in the grey locker.

The missing step is one of these types, each written as one JSON object:
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
- The values are: ["red box", "green cupboard", "blue drawer", "grey locker"]. The names are: ["Dalia", "Ines", "Mirela", "Quinn", "Zoltan"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Ines", "value": "grey locker", "present": ["Dalia", "Ines"], "missed_by": [], "secret_witnesses": []}]`

## explain-L3-003 (workplace, seed 5730004)

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
Jonas, Soren, Bruno, Oksana and Quinn work on the same team. This is what happened, in order.
1. Call with Jonas, Soren, Bruno, Oksana and Quinn: Quinn sets the discount on the Fenwick quote at 25%.
2. Call with Jonas, Soren, Bruno, Oksana and Quinn: Oksana changes the discount on the Fenwick quote to 10%.
3. Call with Jonas, Soren, Bruno and Quinn: Soren changes the discount on the Fenwick quote to 5%. Bruno is on the call but has stepped away from the desk and misses this. Nobody realises that Bruno missed it. Oksana is not on the call but secretly listens in, and can see who is on it. Nobody knows that Oksana is listening.
4. Call with Jonas, Soren, Bruno and Quinn: Soren changes the discount on the Fenwick quote to 25%.
5. Call with Jonas, Soren, Bruno and Quinn: Soren changes the discount on the Fenwick quote to 15%.
6. Bruno wants to mislead Oksana, so Bruno sends Oksana a direct message: “The discount on the Fenwick quote is 25%.”
7. Call with Jonas, Soren, Bruno and Quinn: Soren changes the discount on the Fenwick quote to 5%. Oksana is not on the call but secretly listens in, and can see who is on it. Nobody knows that Oksana is listening.
8. Quinn sends Oksana a direct message: “The discount on the Fenwick quote is 5%.”
9. Call with Jonas, Soren, Bruno and Quinn: Quinn changes the discount on the Fenwick quote to 10%.
10. [A step is missing here.]
11. Jonas, working alone, changes the discount on the Fenwick quote to 5% and tells nobody.

Facts at the end of the story:
1. The discount on the Fenwick quote is really 5%.
2. Bruno thinks that Jonas thinks that Bruno thinks that Soren thinks the discount on the Fenwick quote is 15%.
3. Bruno thinks that Oksana thinks that Bruno thinks that Jonas thinks the discount on the Fenwick quote is 10%.
4. Quinn thinks that Soren thinks that Jonas thinks that Bruno thinks the discount on the Fenwick quote is 10%.
5. Oksana thinks the discount on the Fenwick quote is 5%.
6. Soren thinks the discount on the Fenwick quote is 15%.
7. Soren thinks that Quinn thinks the discount on the Fenwick quote is 10%.
8. Jonas thinks that Soren thinks the discount on the Fenwick quote is 15%.

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
- The values are: ["5%", "25%", "10%", "15%"]. The names are: ["Bruno", "Jonas", "Oksana", "Quinn", "Soren"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Bruno", "value": "15%", "present": ["Bruno", "Jonas", "Soren"], "missed_by": [], "secret_witnesses": []}]`

## explain-L3-004 (classic, seed 5730005)

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
Goran, Zoltan, Emeka, Rania and Dalia share a house. The sunroom has four closed containers that nobody can see into: the red box, the blue drawer, the wicker basket and the grey locker. This is what happened, in order.
1. Goran, Zoltan, Emeka, Rania and Dalia are in the sunroom. Rania takes a padlock out of a pocket and puts it in the red box.
2. Goran, Emeka, Rania and Dalia are in the sunroom. Goran moves the padlock to the grey locker. Rania is in the sunroom but is absorbed in a phone and does not notice this. Nobody realises that Rania missed it.
3. Goran, Emeka and Rania are in the sunroom. Rania moves the padlock to the red box.
4. Goran wants to mislead Dalia, so Goran sends Dalia a private text message: “The padlock is in the blue drawer.”
5. Emeka sends Dalia a private text message: “The padlock is in the red box.”
6. Zoltan, Emeka and Rania are in the sunroom. Emeka moves the padlock to the wicker basket. Zoltan is in the sunroom but is absorbed in a phone and does not notice this. Nobody realises that Zoltan missed it.
7. Rania sends Goran a private text message: “The padlock is in the wicker basket.”
8. Zoltan and Rania are in the sunroom. Rania opens every container in full view of the sunroom, showing that the padlock is in the wicker basket.
9. [A step is missing here.]
10. Rania sends Emeka a private text message: “The padlock is in the red box.”
11. Emeka sends Zoltan a private text message: “The padlock is in the red box.” Goran secretly reads this message on Zoltan's phone. Neither Emeka nor Zoltan ever knows that Goran read it.

Facts at the end of the story:
1. The padlock is really in the red box.
2. Dalia thinks that Goran thinks the padlock is in the red box.
3. Zoltan thinks that Rania thinks the padlock is in the red box.
4. Dalia thinks that Goran thinks that Dalia thinks that Rania thinks the padlock is in the grey locker.
5. Dalia thinks that Emeka thinks that Rania thinks the padlock is in the grey locker.
6. Rania thinks that Zoltan thinks the padlock is in the red box.
7. Emeka thinks that Rania thinks that Zoltan thinks the padlock is in the wicker basket.
8. Goran thinks that Rania thinks the padlock is in the red box.

The missing step is one of these types, each written as one JSON object:
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
- The values are: ["red box", "blue drawer", "wicker basket", "grey locker"]. The names are: ["Dalia", "Emeka", "Goran", "Rania", "Zoltan"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "change", "who": "Rania", "value": "red box", "present": ["Goran", "Rania", "Zoltan"], "missed_by": [], "secret_witnesses": ["Dalia"]}]`

## explain-L3-005 (workplace, seed 5730009)

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
Amara, Xavier, Mirela, Keiko and Chidi work on the same team. This is what happened, in order.
1. Call with Amara, Xavier, Mirela, Keiko and Chidi: Keiko picks Brightwater as the packaging supplier.
2. Call with Amara, Xavier, Mirela and Chidi: Amara switches the packaging supplier to Halcyon.
3. Chidi sends Keiko a direct message: “The packaging supplier is Halcyon.”
4. Mirela sends Keiko a direct message: “The packaging supplier is Halcyon.”
5. Call with Amara, Xavier and Mirela: Amara switches the packaging supplier to Ironbridge.
6. Mirela sends Chidi a direct message: “The packaging supplier is Ironbridge.”
7. Call with Amara and Mirela: Amara switches the packaging supplier to Northwind.
8. Call with Amara and Mirela: Amara switches the packaging supplier to Ironbridge.
9. Chidi sends Xavier a direct message: “The packaging supplier is Ironbridge.”
10. [A step is missing here.]
11. Call with Amara and Chidi: Amara switches the packaging supplier to Northwind.

Facts at the end of the story:
1. The packaging supplier is really Northwind.
2. Xavier thinks that Keiko thinks that Xavier thinks that Keiko thinks the packaging supplier is Halcyon.
3. Xavier thinks the packaging supplier is Ironbridge.
4. Amara thinks that Keiko thinks the packaging supplier is Brightwater.
5. Mirela thinks the packaging supplier is Ironbridge.
6. Chidi thinks that Xavier thinks the packaging supplier is Ironbridge.
7. Xavier thinks that Amara thinks the packaging supplier is Ironbridge.
8. Xavier thinks that Mirela thinks the packaging supplier is Ironbridge.

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
- The values are: ["Brightwater", "Ironbridge", "Northwind", "Halcyon"]. The names are: ["Amara", "Chidi", "Keiko", "Mirela", "Xavier"].

Your step is accepted if, with it in the gap, every step of the story can happen as told under the rules and every fact above is true. For example, a person who tells something without wanting to mislead must believe it at that moment.

Work it out, then finish with a line that says SCRIPT: followed by a JSON array that holds the one missing step.

reference: `[{"step": "message", "from": "Xavier", "to": "Keiko", "value": "Halcyon", "secret_readers": []}]`
