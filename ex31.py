# In this script I will ask the user questions and make decisions based on their answers.

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")


    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job.")
else:
    print("You stumble around and fall on a knife and die.  Good job!")

# America the beautiful
print("""You are America, choose a country to invade. Invade Iraq #1, or Iran #2, even Qatar #3?""")

invade = input("> ")

if invade == "1":
    print("No weapons of mass destruction here, however lots of oil.")
    print("What do you do?")
    print("1. Leave the country.")
    print("2. Stay, take the oil.")

    oil = input("> ")

    if oil == "1":
        print("You go home, good choice")
    elif oil == "2":
        print("You stay, now stuck in the country with no exit plan. Scum.")
    else:
        print(f"Please make a decision {oil}, the world is watching.")
        print("Land of the beautiful home of the brave.")

elif invade == "2":
    print("Trump becomes president.")
    print("1. Bleach your skin orange.")
    print("2. Get the trump wig.")
    print("3. Catch the next flight home.")

    trump = input("> ")

    if trump == "1" or trump == "2":
        print("You get into serious twitter beef.")
        print("C'mon lad.")
    else:
        print("Twitter cancels your account and you are banned.")
        print("Build another trump hotel.")
else:
    print("Your son stabs you in the back while you have your legs waxed.")

# Penalty shootout scenario
print("""You are taking a penalty for England, which way do you go? Do you go left #1, right #2 or middle #3?""")

penalty = input("> ")

if penalty == "1":
    print("Congratulations your team has won! Well done!")
elif penalty == "2":
    print("Saved. The keep dived the correct way. Unlucky.")
else:
    print("You chipped it down the middle!? Cheeky.")


# Lord of the rings Character
print("""It's Lord of the Rings, you are about to enter a battle to save middle earth.
Which weapon do you choose?
Long sword and grit #1,
Bow& arrow and cunning #2,
or battle axe and stubborness #3?""")

battle = input("> ")

if battle == "1":
    print("You are aragorn, the future King.")
elif battle == "2":
    print("You are Legolas, the elf prince.")
else:
    print("You are Gimley, the mouthy dwarf.")
