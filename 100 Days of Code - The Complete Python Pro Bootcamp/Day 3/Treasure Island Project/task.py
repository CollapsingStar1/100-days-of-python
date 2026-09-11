print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("=== WELCOME TO THE CURSED SHORES OF TREASURE ISLAND ===")
print("You wake up on a foggy beach with a rusted knife and a strange coin in your pocket.\n")

print("Before you lies a fork in the path:")
print("1. 'left'  -> A winding track into the misty mangrove swamp.")
print("2. 'right' -> A steep rocky path leading toward a dark cave.")
choice1 = input("> ").lower().strip()

# ==================== BRANCH 1: THE MANGROVE SWAMP (LEFT) ====================
if choice1 == "left":
    print("\nYou push through the dense mangroves and arrive at a wide, murky lake.")
    print("In the distance sits a ruined temple island.")
    print("Choices: 'wait' for a passing vessel, 'swim' across, or 'raft' (build a raft from bamboo).")
    choice2 = input("> ").lower().strip()

    if choice2 == "wait":
        print("\nYou wait quietly. An old cloaked ferryman approaches silently in a gondola.")
        print("He extends his hand and rasps: 'One coin, traveler, or your soul.'")
        print("Choices: 'pay' with your strange coin, or 'attack' the ferryman.")
        choice3 = input("> ").lower().strip()

        if choice3 == "pay":
            print("\nThe ferryman nods and rows you safely to the ancient temple steps.")
            print("Three stone doors stand before you: 'red', 'yellow', and 'blue'.")
            door = input("> ").lower().strip()

            if door == "yellow":
                print("\n[ENDING: THE GOLDEN HEIR]")
                print("The door slides open to reveal chests overflowing with pirate gold and jewels.")
                print("You leave the island a wealthy legend!")
            elif door == "red":
                print("\n[ENDING: ASHES TO ASHES]")
                print("Lava surges from the ceiling the moment the door opens. Game Over.")
            elif door == "blue":
                print("\n[ENDING: BEAST FEAST]")
                print("A pack of starved cave basilisks tear through the doorway. Game Over.")
            else:
                print("\nYou hesitate too long. The temple ceiling collapses. Game Over.")

        elif choice3 == "attack":
            print("\n[ENDING: CURSE OF THE FERRYMAN]")
            print("Your knife passes right through his spectral form. He banishes your soul to the lake. Game Over.")
        else:
            print("\nInvalid choice. The ferryman departs, stranding you forever in the fog. Game Over.")

    elif choice2 == "swim":
        print("\nYou dive into the black water. Halfway across, giant tentacles ripple beneath you.")
        print("Choices: 'fight' with your knife, or 'dive' deeper to evade.")
        choice3 = input("> ").lower().strip()

        if choice3 == "fight":
            print("\n[ENDING: KRAKEN SNACK]")
            print("A small knife is no match for the Leviathan of the Deep. Game Over.")
        elif choice3 == "dive":
            print("\nYou spot an underwater tunnel glowing with bioluminescent moss!")
            print("You surface inside an underground grotto containing a locked crystal chest.")
            print("Choices: 'smash' the lock with a stone, or 'inspect' the mechanism.")
            choice4 = input("> ").lower().strip()

            if choice4 == "inspect":
                print("\n[ENDING: MASTER THIEF]")
                print("You find a hidden release latch. The chest opens to reveal the Lost Heart of the Ocean pearl!")
                print("You swim out through a secret exit to freedom!")
            elif choice4 == "smash":
                print("\n[ENDING: POISON CLOUD]")
                print("Smashing the chest triggers a poison dart trap. Game Over.")
            else:
                print("\nYou run out of air while pondering. Game Over.")
        else:
            print("\nYou freeze up in fear and drown. Game Over.")

    elif choice2 == "raft":
        print("\nYou tie bamboo together and begin paddling.")
        print("A sudden storm hits! Your raft starts breaking apart.")
        print("Choices: 'jump' towards a nearby buoy, or 'hold' onto the remaining logs.")
        choice3 = input("> ").lower().strip()

        if choice3 == "jump":
            print("\n[ENDING: STRANDED CASTAWAY]")
            print("You grab the buoy, but you're swept out into the open sea with no rescue in sight. Game Over.")
        elif choice3 == "hold":
            print("\n[ENDING: ACCIDENTAL CAPTAIN]")
            print("The current washes your broken raft directly into the hidden cove of an abandoned pirate galleon!")
            print("You claim the entire ship and its treasure as your own!")
        else:
            print("\nYou panic and slip under the waves. Game Over.")
    else:
        print("\nYou wander aimlessly in the swamp until quicksand claims you. Game Over.")

# ==================== BRANCH 2: THE ROCKY CAVE (RIGHT) ====================
elif choice1 == "right":
    print("\nYou climb the jagged rocks and stand at the mouth of a cavern.")
    print("A sleeping stone golem blocks the entrance, holding a glowing lantern.")
    print("Choices: 'sneak' past the golem, 'take' the lantern, or 'climb' above the cave entrance.")
    choice2 = input("> ").lower().strip()

    if choice2 == "sneak":
        print("\nYou slip past the golem and enter a tunnel lit by torches.")
        print("The tunnel splits into two: 'left' smells of ozone and sulfur, 'right' echoes with chanting.")
        choice3 = input("> ").lower().strip()

        if choice3 == "left":
            print("\nYou enter an ancient alchemy lab with two vials: 'green' and 'purple'.")
            vial = input("Which vial do you drink? > ").lower().strip()
            if vial == "green":
                print("\n[ENDING: IMMORTAL GUARDIAN]")
                print("Your body transforms into living diamond! You become the immortal protector of the island.")
            elif vial == "purple":
                print("\n[ENDING: INSTANT DECOMPOSITION]")
                print("The purple liquid was acid. Game Over.")
            else:
                print("\nYou drop both vials, igniting the lab. Game Over.")

        elif choice3 == "right":
            print("\nYou find a cult of skeleton warriors worshipping a massive ruby altar.")
            print("Choices: 'toss' your coin as a distraction, or 'charge' them with your knife.")
            choice4 = input("> ").lower().strip()

            if choice4 == "toss":
                print("\n[ENDING: SHADOW HEIST]")
                print("The skeletons rush toward the clinking coin. You grab the ruby altar and slip away unseen!")
            elif choice4 == "charge":
                print("\n[ENDING: OVERWHELMED]")
                print("Ten skeletal swords strike at once. Game Over.")
            else:
                print("\nYour hesitation gives away your position. Game Over.")
        else:
            print("\nYou stumble into a bottomless pit in the dark. Game Over.")

    elif choice2 == "take":
        print("\nYou try to pry the lantern from the golem's stone fingers.")
        print("The golem awakens with a roar and swings its stone fist!")
        print("Choices: 'dodge' left, or 'parry' with your knife.")
        choice3 = input("> ").lower().strip()

        if choice3 == "dodge":
            print("\nYou roll out of the way! The golem punches the rock wall, shattering it to reveal a hidden vault.")
            print("Inside sits an enchanted crown that commands the island's stone guardians.")
            print("\n[ENDING: KING OF THE GOLEMS]")
            print("The golem kneels before you. The entire island's treasure is now yours!")
        elif choice3 == "parry":
            print("\n[ENDING: CRUSHED FLAT]")
            print("Your knife shatters against stone, and so do your ribs. Game Over.")
        else:
            print("\nThe golem crushes you where you stand. Game Over.")

    elif choice2 == "climb":
        print("\nYou scale the cliffs above the cave and reach the island's volcano peak.")
        print("At the rim, a dragon slumbers on a mountain of diamonds.")
        print("Choices: 'steal' an egg, or 'sneak' a single diamond.")
        choice3 = input("> ").lower().strip()

        if choice3 == "sneak":
            print("\n[ENDING: HUMBLE FORTUNE]")
            print("You pocket a fist-sized diamond without waking the beast and safely rappel down to your escape raft!")
        elif choice3 == "steal":
            print("\n[ENDING: DRAGON'S ROAST]")
            print("The mother dragon immediately detects her moving egg and incinerates the summit. Game Over.")
        else:
            print("\nA loose rock alerts the dragon. Game Over.")
    else:
        print("\nYou fall from the slippery rocks onto the spikes below. Game Over.")

# ==================== INVALID START ====================
else:
    print("\nYou stand frozen on the beach until the incoming tide carries you away. Game Over.")