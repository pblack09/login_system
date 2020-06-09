inventory = []

def start():
    print("""\nYou find yourself locked in a dark and damp jail cell.
To your right is a skeleton slumped against the wall.
To your left is a small pile of hay.""")
    print("**What do you do?**")
    print("1. Try to open the door.")
    print("2. Search the pile of hay.")
    print("3. Accept your fate.")
    initial = input('> ')

    if initial == "1":
        door()

    elif initial == "2":
        hay()

    else:
        wait()

def door():
    print("\nThe door is securely locked.")
    print("You hear rustling further down the torch-lit hallway.")
    print("**What do you do?**")
    print("1. Shout down the hallway.")
    print("2. Search the pile of hay.")
    print("3. Attempt to use the skeleton's bones to pick the lock.")
    door = input('> ')

    if door == "1":
        guard()

    elif door == "3":
        guard()

    else:
        hay()

def hay():
    print("\nYou find an old wooden stick roughly widdled into a sharp point.")
    print("**What do you do?**")
    print("1. Take the stick and use it on the door.")
    print("2. Tell the guard about the stick.")
    print("3. Hide the shank in your waistband.")
    haypile = input('> ')

    if haypile == "1":
        print("\nThe guard opens your cell and smashes the side of your head with the butt of his sword.\n")
        start()

    elif haypile == "2":
        print("\nThe guard opens your cell and smashes the side of your head with the butt of his sword.\n")
        start()

    elif haypile == "3":
        inventory.append("shank")
        print("\n**You hide the wooden shank in your waistband.**")
        wait()

    else:
        print("\nI don't know what that means.")
        hay()

def wait():
    print("\nAfter what you assume to be an hour, you hear movement down the hallway.")
    print("'Oy! Your time is up. You're gonna meet your maker now.', says the guard with a grin.")
    print("He opens the door and says, 'Put this bag on your head.'")
    print("**What do you do?**")
    print("1. Put the bag on your head and wait.")
    print("2. Tell the guard to shove it.")
    print("3. Use your shank and attack the guard.")
    wait = input("> ")

    if wait == "1":
        print("\nYou put the bag on your head and hear the guard walk around you.")
        hallway()

    elif wait == "2":
        print("\nThe guard pulls back and punches you in the stomach.")
        print("Kneeling over from the blow, the guard forces the bag over your head.")
        hallway()

    else:
        print("\nYou begin to put the bag over your head as the guard walks towards you.")
        print("Once he's finally within range, you toss the bag at him, reach for the shank, and lunge to strike!")
        print("You trip on a rock...")
        print("The fall knocks you unconscious, and you when you wake up, you feel warm air against your skin and the sunlight hurts your eyes even through the bag.")
        gallows()

def guard():
    print("\nA guard comes down the hallway with his keys clanking on his hip.")
    print("The guard sternly states, 'Oy! You mess with that door anymore and I'll give ya another lickin'!'")
    print("**What do you do?**")
    print("1. Mess with the door.")
    print("2. Back up from the door.")
    print("3. Tell the guard, 'Shove that lickin' up your ***!")
    guard = input('> ')

    if guard == "1":
        print("\nThe guard opens the door and smashes the side of your head with the butt of his sword and knocks you unconscious.\n")
        start()

    elif guard == "3":
        print("\nThe guard opens the door and smashes the side of your head with the butt of his sword and knocks you unconscious.\n")
        start()

    else:
        print("\n'Smart move boy...', says the guard.")
        wait()

def hallway():
    print("\nThe guard firmly grasps your right arm and escorts you down a series of hallways blindly.")
    print("**What do you do?**")
    print("1. I can't see... Obviously I go along with it...")
    print("2. I attempt to run.")
    print("3. I go for the shank to attack the guard.")
    hallway = input("> ")

    if hallway == "1":
        print("\nSmart move.")
        last_chance()

    elif hallway == "2":
        print("\nYou can't see... You run into a wall almost immediately and the guard grabs you again.")
        last_chance()

    else:
        print("\nThe guard slaps your hand as you try to quickly move for your waistband.")
        print("**The guard sees the shank and confiscates it.**")

        if len(inventory) > 0:
            inventory.remove("shank")
            last_chance()

        else:
            last_chance()

def last_chance():
    print("\nYou hear a large and creaky door open in front of you.")
    print("The warm air immediately causes your skin to begin sweating.")
    gallows()

def gallows():
    print("\nYour arms tied together in front of you.")
    print("The bag is lifted off of your head and your eyes sting as your eyes adjust to the sunlight.")
    print("You hear screaming, chanting, and a roar of crazed citizens. In front of you, you see a sea of people calling for you to hang.")
    print("The rope around your neck tightly wraps around your neck.")
    print("'For the crimes of murdering the Prince and kidnapping his wife-to-be, we sentence you to hang until death.' says a heavy-set man with a white curly wig.")
    print("**What do you do?")
    print("1. Accept your punishment.")
    print("2. Beg for mercy.")
    print("3. Use your shank to cut the ropes and escape.")
    hang = input("> ")

    if len(inventory) > 0 and hang == "1":
        print("\nYou hear the creaking of wood as a lever is pulled and the floor beneath you disappears.")
        print("The last thing you hear is a loud snap as everything quickly fades to black.")
        end()

    elif len(inventory) > 0 and hang == "3":
        print("\nYou cut the ropes just as the floor below you falls.")
        print("You barely land on your feet and hear gasps throughout the crowd.")
        print("Run...")
        end()

    elif len(inventory) > 0 and hang == "2":
        print("\nI'll allow it..")
        print("You escape the ropes and everyone is frozen in confusion.")
        print("Run...")
        end()

    elif len(inventory) == 0 and hang == "2":
        print("\nYou hear the creaking of wood as a lever is pulled and the floor beneath you disappears.")
        print("The last thing you hear is a loud snap as everything quickly fades to black.")
        end()

    elif len(inventory) == 0 and hang == "3":
        print("\nYour shank was confiscated...")
        print("The guard notices and laughs as the floor beneath you drops and you hear a loud snap while everything fades to black.")
        end()

    else:
        print("\nI'll allow it..")
        print("You escape the ropes and everyone is frozen in confusion.")
        print("Run...")
        end()

def end():
    print("\n\n\t\tThank you for playing!")
    print("\tI hope you enjoyed this small game!")

print("********************************")
print("  Welcome to Escape from Death!")
print("********************************")
print("Would you like to play?")
prompt = input("Y or N: ")

if prompt == "Y":
    start()

else:
    import accounts
    accounts.options()
