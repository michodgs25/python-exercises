from sys import exit

#                                 ORIGINAL GAME

#def gold_room():
    #print("This room is full of gold. How much do you take?")

    #choice = input("> ")

    #if "0" in choice or "1" in choice:
    #    how_much = int(choice)
    #else:
    #    dead("Man, learn to type a number.")

    #    if how_much < 50:
#        print("Nice, you're not greedy, You win!")
#            exit(0)
#        else:
#            dead("You greedy bastard!")

#def bear_room():
    #print("There is a bear here.")
    #print("The bear has a bunch of honey.")
    #print("The fat bear is in front of another door.")
    # print("How are you going to move the bear?")
    # print(" 'take honey' or 'taunt bear' ")
    # bear_moved = False

    # while True:
    #    choice = input("> ")

    #    if choice == "take honey":
    #        dead("The bear looks at you and then slaps your face off.")
    #    elif choice == "taunt bear" and not bear_moved:
    #        print("The bear has moved from the door.")
    #        print("You can go through it now.")
    #        bear_moved = True
    #    elif choice == "taunt bear" and bear_moved:
    #        dead("Bear gets pissed off and chews both your legs off.")
    #    elif choice == "open door" and bear_moved:
    #        gold_room()
    #    else:
    #         print("I got no idea what that means.")

#def cthulhu_room():
    #print("Here you see the great evil Cthulhu.")
    #print("He, it, whatever stares at you and drives your mind insane.")
    #print("Do you flee for your life or your head is eaten?")

    #choice = input("> ")

    #if "flee" in choice:
    #    start()
    # elif "head" in choice:
    #    die("Well that was tasty!")
    #else:
    #    cthulhu_room()


# define death, gameover finished
#def dead(why):
#    print(why, "Good job!")
#    exit(0)

# Define start game function
#def start():
    # print three statements, painting the sceneario to the user
    #print("You are in a dark room.")
    #print("There is a door to your right and left.")
    #print("Which one do you take?")

    # User has two choices, 'left' or 'right'
    #choice = input("> ")

    # if left, enter bear room
    #if choice == "left":
    #    bear_room()
    # if right, enter cthulhu room
    #elif choice == "right":
    #    cthulhu_room()
        # choose neither, you die
    #else:
    #    dead("You stumble around the room until you starve.")

# start()



#                    DEVELOPED AND EXTENDED GAME TWO

# define death, gameover finished
def die(why):
    print(why, "Good job!")
    exit(0)
# define game start function, provide user with two options 'right or left door' or 'middle door'
def start():
    print("""
    You are in a dark room.
    There is a door to your right, left and middle.
    Which one do you take?

    Type: right, left or middle
    """)

    # user choice input prompt, either left or right
    choice = input("> ")

    # if-elif-else group, if left: enter bear_room, elif right: enter cthulhu_room, else neither: game ends
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "middle":
        crocodile_room()
    else:
        dead("You stumble around the room until you starve.")
        exit()

# define bear room function, provide two options, take honey or taunt bear
def bear_room():
    print("""
    There is a bear here.
    The bear has a bunch of honey.
    Also, the fat bear is standing in front of another door.
    How are you going to move the bear.

    Type: take honey or taunt bear
    """)
    # create while-loop, infinite loop, loop breaks if user chooses takes honey
    while True:
        # user prompt, take honey or taunt
        choice = input("> ")

        # run if-elif equal too choice statements
        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.")

        # if user choice = taunt bear, user prompted to open next door
        elif choice == "taunt bear":
            print("""
            The bear has moved from the door.
            You can go through it now.

            Type: open door
            """)
            bear_moved = True

        # if chose taunt bear and bear did not move, game ends
        elif choice == "taunt bear" and not bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
        # if user chose to open door and bear has moved, user moves to the gold room
        elif choice == "open door" and bear_moved:
            gold_room()
        # if none of the options take from above, loops restarts from the top
        else:
            print("I have no idea what that means.")

# define the cthulhu_room function
def cthulhu_room():
    print("""
    Here you see the great evil cthulhu.
    He, it, whatever stares at you intensely, and starts to drives you insane.
    Do you flee for your life or try to look away?

    Type: Flee or look away
    """)

    # user prompt, choose between flee or look away
    choice = input("> ")

    # if user flees, game starts from the beginning again
    if "flee" in choice:
        start()
    # user decided to try and look away, game ends
    elif "away" in choice:
        dead("Well that was tasty!")
    # if user chooses neither, they stay in the cthulhu_room
    else:
        cthulhu_room()

# define crocodile room function
def crocodile_room():
    print("""
    This room has the snappy crocodile swimming in a murky lake.
    There is a door at the end of the lake.
    You must get past the crocodile.
    Do you shoot the crocodile with your shotgun,
    or distract it with funky dance moves?

    Type: shotgun or dance
    """)

    # infinite loop, loop breaks when user chooses either shotgun or dance
    while True:
        # user prompt user to choose shotgun or dance
        choice = input("> ")

        # if choice equal to shotgun, gameover
        if choice == "shotgun":
            dead("""
            You frighten the crocodile and,
             he drags you into the icy depths of the lake.
             """)
        elif choice == "dance":
            print("""
            crocodile is so impressed with how you move your hips,
            he allows you too cross the lake
            You can go through the door now.

            Type: open door""")
            crocodile_moved = True

        elif choice == "dance" and not crocodile_moved:
            dead("The crocodile gets pissed off and spins you till your lungs explode.")

        elif choice == "open door" and crocodile_moved:
            palace()
        else:
            crocodile_room()

# define gold room function, user ends up here if chooses successfully
def gold_room():
    print("This room is full of gold. How much do you take?")

    # prompt asks user how much gold they want to take
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much =  int(choice)
    else:
        # if user does not type a number, gameover
        dead("Man, learn to type a number.")
    # if user takes less than 50 gold, they win and the game ends
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    # user takes more than 50 gold, they lose and the game ends
    else:
        dead("You greedy bastard!")

# define palace function, user must fight the king to win his throne
def palace():
    print("""
    You have arrived at the royal palace.
    And must face the king, you have the choice of three weapons.
    A sword, axe or chopsticks.

    Type which one: sword, axe or chopsticks.
    """)

    # prompt ask user which weapon choose to fight the king
    choice = input("> ")

    # if-elif-else group choices, user must pick the right weapon to win
    if choice == "sword":
        dead("""
        The king is a master swordsman, he drives his kings blood blade,
        straight through your beating heart! Good job.
        """)
    elif choice == "axe":
        dead("""
        You put up a great fight against the king,
        howver he uses his snake whip to strangle the life out of you.
        """)
    elif choice == "chopsticks":
        print("""
        You are the reigning choppy chopsticks champ,
         and outwit the old king to take his throne!

         All hail the new king!
         """)
        exit(0)
    # if the user chooses none of the choices, stay in the room
    else:
        palace()

# define dead function, if user picks wrong option, game ends
def dead(why):
    print(why, "Good job!")
    exit(0)

start()
