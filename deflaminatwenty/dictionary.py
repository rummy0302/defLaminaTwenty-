import tkinter as tk
from time import sleep

# dictionary with question statement
question_dict = {1: 'Ostriches have 2 stomachs.', 2: 'Penguins evolved to fly underwater.', 
3: 'Eagles eyesight are around 3 times better \nthan a regular human vision.', 4: 'Owls can rotate their necks 255 degrees.', 
5: 'Unlike other mammals, the duck-billed platypus lays eggs.', 6: "Echidna's spines are actually modified hairs.", 
7: "A lion's roar can be heard up to 8 kilometres away.", 8: "An elephants' tusks are actually teeth.", 
9: 'All sharks are cold-blooded.', 10: 'Seahorses have a hard exoskeleton rather than scales.', 
11: 'Blue whales are the largest animals ever to live on Earth.', 
12:  'The long tails of stingrays usually have a venomous spine.', 13: 'There are about 2,700 species of mosquito.', 
14: 'A cockroach can live up to 2 weeks without its head.', 15: 'Female tarantulas can lay up to 1000 eggs.', 
16: 'Scorpions glow in UV light.', 17: 'King Cobras are the only snake that builds nests for its eggs.', 
18: 'Lizards can detach their tails.', 19: "Komodo dragon's can consume 50 percent of their body weight in one sitting.", 
20: "A crocodile's jaws can apply 2,000 pounds of pressure per square inch."}

# dictionary with answers
answer_dict = {1: 'False', 2: 'True', 3: 'False', 4: 'False', 5: 'True', 6: 'True', 7: 'True', 8: 'True', 9: 'False', 10: 'True', 
11: 'True', 12: 'True', 13: 'True', 14: 'False', 15: 'False', 16: 'True', 17: 'True', 18: 'True', 19: 'False', 20: 'False'}

#on wrong answer > displays these results
ifwrong_dict = {1: 'The correct answer is False. Ostriches have 3 stomachs.', 
2: 'The correct answer is True. Penguins evolved to fly underwater \nhence losing the capability to fly on air as a result.', 
3: 'The correct answer is False. Eagle has an eyesight that is around 5 times \nbetter than the human vision.', 
4: 'The correct answer is False. Owls can rotate their necks 270 degrees.', 
5: 'The correct answer is True. Duck-billed platypus do lay eggs unlike other \nmammals.', 
6: 'The correct answer is True. Echidnas spines are modified hairs which acts \nas its defense mechanism.', 
7: 'The correct answer is True. The roar of a lion can be heard up to 8 \nkilometres away.', 
8: 'The correct answer is True. The tusk of the elephant is actually its teeth.', 
9: 'The correct answer is False. Not all sharks are cold-blooded such as\n the Tresher shark.', 
10: 'The correct answer is True. The seahorses have a hard exoskeleton \nto protect itself from its predators.', 
11: 'The correct answer is True. They are the largest animals to live on Earth \nwhere they can grow to lengths of more than 30 metres.', 
12: 'The correct answer is True. The long tail of the stingray contains its \nvenomous spine that is used to fend of predators.', 
13: 'The correct answer is True. There are approximately 2,700 species of mosquitoes.', 
14: 'The correct answer is False. A cockroach can live up to 1 week without its head.', 
15: 'The correct answer is False. The female tarantula can lay up to 2000 eggs.', 
16: 'The correct anser is True. The hyaline layer in the scorpions exoskeleton\n reacts with UV light to produce its glow.', 
17: 'The correct answer is True. The cobras are the only snakes to build a nest \nfor its eggs to keep the eggs safe.', 
18:  'The correct answer is True. The lizards can detach their tails as a defense\n mechanism to escape from predators.', 
19: 'The correct answer is False. The komodo dragon can consume 80 percent of their \nbody weight in one sitting.', 
20: 'The correct answer is False. The jaw of the crocodile can apply 3,700 pounds of\n pressure per square inch.'    }

#on press hint
hint_dict={1:"They need to metabolize the tough plant matter that they eat, which \nthey can't do in just a single stomach.",
2:"Early lineages of penguins had feathered wings and were gifted \nwith the ability of flight.",
3:"‘Good’ vision for a human is 20/20,Eagles has a vision of 20/4",
4:"Owls are more flexible than humans because a bird’s head is only\n connected by one socket pivot.",
5:"Egg-laying mammals still exist today may be because their ancestors took to the water.",
6:"Spiny hairs are echidna's main defence.",
7:" Lions roar as a means of communication with other lions",
8:"Much of the tusk is made up of dentine, a hard, dense, bony tissue.",
9:"Warmer muscles tend to be more powerful.",
10:"Seahorses have a swim bladder for buoyancy, gills to breathe, and fins to help them swim.",
11:"Blue whales weigh as much as 33 elephants!",
12:"Every year, about 1,500-2,000 stingray injuries are reported in the US.",
13:"We have 110 trillion mosquitoes across nearly all of the planet, and \nwe've had them for over 100 million years.",
14:"Cockroaches are infamous for their tenacity, and are often cited as \nthe most likely survivors of a nuclear war.",
15:"According to National Geographic, it is common for a single tarantula\n egg sac to contain anywhere from 500 to 1,000 babies",
16:"Scorpions are nocturnal hunters.",
17:"King cobras generally take shelter in animal burrows, under fallen trees and among rock.",
18:"Autotomy refers to the ability to self-amputate and release a part of\n the body. It is used by animals as a means of survival when under attack by a predator.",
19:"Not only are Komodo dragons big, but they have an appetite to match.",
20:"A crocodile can easily crush a human skull."}











