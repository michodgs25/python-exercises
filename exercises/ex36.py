from sys import exit

# DESIGNING AND DEBUGGING

#                   RULES FOR IF-STATEMENTS

# 1. Every if-statement must have an else

# 2. If this else should never run because it doesn't make sense,
#    use a die function in the else that prints out an error message and dies.

# 3. Never nest if-statements more than two deep, and always try to do them one deep.

# 4. Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences.
#    Put blank sentences before and after.

# 5. Your boolean tests should be simple.
#    If they are complex, move their calculations to earlier in your function
#    and use a good name for the variable.

#                      RULES FOR LOOPS

# 1. Use a while-loop only to loop forever, and that means probably never.
#    This only applies to Python; other languages are different.

# 2. Use a for-loop for all other kinds of looping,
#    especially if there is a fixed or limited number of things to loop over.

#                     TIPS FOR DEBUGGING

# 1. Do not use a "debugger".

# 2. The best way to debug a program is to use print,
#    to print out the values of variables at points in the program to see where they go wrong.

# 3. Make sure parts of your program work as you work on them.
#    Do not write massive files of code before you try to run them.
#    Code a little, run a little, fix a little


# Game premise:
# You have crashed landed on a remote island and, and need to figure out an escape plan before your few food supplies run out.
# However you will need to move quick, as by nightfall the islands blood thirsty demons will reveal themselves,
# and they know your location already.
# Game Objectives:
#                 Survive the night
#                 Escape the island by tomorrow mid-afternoon


# START GAME

# First define death, gameover
def dead(why):
    print(why, "Gameover")
    exit(0)


# define start of game
def start():
    print("""
          You awake amidst the wreckage of your private plane.
          It's the middle of the night, and the only light for miles around,
          are the burning flames rapidly making their way towards you from the cockpit.
          You must react quickly to get out of the plane.
          *type: a - to cut seatbelt
          """)

    choice = input("> ")

    if choice == "a":
        print("Well done, now exit the plane before it explodes!")
        retrieve_extinguisher()
    else:
        dead("You burn alive. Ouch.")


# user must put out the fire, the plane is the only hope of having shelter
# a fire extinguisher is located at the rear of the plane
# There are three ways presented: escape hatch, underpassage or cockpit

# define put_fire_out function, user needs to pick right choice to enter next sceneario
def retrieve_extinguisher():
    print("""
          You stand outside and realise you must put out the fire to save the remainder of the plane,
          this plane could be your only chance of calling for help.
          There is a fire extinguisher at the rear of the plane,
          how will you get there without dying?

          Choose wisely, otherwise the fire will engulf the plane and yourself

          *type: a, b or c

          a. cockpit
          b. escape hatch
          c. underpassage
          """)

    # user prompt, must choose between three choices to retrieve the fire extinguisher
    choice = input("> ")

    # if user chooses cockpit, gameover
    if choice == "a":
        dead("You burn alive! The fire is coming from the cockpit!")
    # chooses either option, user succeeds
    elif choice == "b":
        print("Well done you made it inside, just in time.")
        put_fire_out()
    elif choice == "c":
        print("Well done you made it inside, just in time.")
        put_fire_out()
        # user must choose out of the three options
    else:
        # if user does not pick one of the available options, otherwise remain stay in the scene
        print("Please hurry, your survival counts on it!")
        retrieve_extinguisher()


# Next scene, user needs to put out the fire
def put_fire_out():
    print("""
          You have found the extinguisher,
          you need to put the fire out quickly.

          The fire has engulfed the main seating area,
          the extinguisher has a limited supply however, so choose wisely.

          Which section will you extinguish first, which will put the fire OUT the fastest?

          *type: a, b or c

          a. passenger section
          b. cockpit entrance
          c. giveup
    """)

    # prompt user to pice an option
    choice = input("> ")

    # if elif and else group
    if choice == "a":
        dead("The fire is too strong, and melts your eye balls.")
    elif choice == "b":
        print("Fire extinguished!! Well done!")
        survive_night()
    else:
        # if user choice is 3, or a none of the options, code below runs
        choice != "a" or "b"
        dead("Good luck in the next life.")


# define survive night function, user must choose how he will survive
def survive_night():
    print("""
       You have extinguished the fire well done, however during the commotion,
       this has drawn the attention of the island demons.

       Now that you've extinguished the fire, there is no light whatsoever.
       A demon crashes into the side of cockpit, you have seconds to make a decision.

       *type: a, b or c

       a. Fight the demon with your fire extinguisher
       b. Seal off the cockpit and hide in the pilot supplies cupboard.
       c. You discover a gun in the glove compartment and shoot the demon.
       """)

    # input prompt, user must choose between options: a, b, c
    choice = input("> ")

    if choice == "a":
        dead("""
        You attempt to swing at the soul slayer but it morphs,
        and attacks. The demon grimey black pit of a face feasts on your soul.
        """)
    # game diverges into two different scenarios, morning_break or island_cave
    elif choice == "b":
        print("""
        You decide to wait out the night, with the gun loaded,
        and pressed against the cupboard door.
        You have survived...for now.
        """)
        morning_break()
    elif choice == "c":
        print("""
        You startle the demon who has never experienced a gun before,
        however you do not kill it and the bullet is spat out.
        You make a run for it out into the darkness...
        """)
        island_cave()
    # User must choose an available option, to progress
    else:
        choice != "a" or "b" or "c"
        print(""""
        HURRY! Choose!
        a, b or c

        Or Ctrl-c to quit
        """)
        survive_night()

#  user must navigate out of the cave
def island_cave():
    print("""
         Phew that was close, you were very lucky.

         Thankfully it was a full moon and this protected you from the demon,
         legends call....
         the soul slayer.
         In your blind desperation you found a cave and hid under a huge rock.
         However this is the soul slayers den, and it is not happy.
         You still have the gun but you only have two bullets left.

         What is your next move?

         *type: a, b, c or d

         a. Hideout under the rock until day comes

         b. Throw the gun in the opposite direction and run

         c. Attempt to gun down the soul slayer with remaining two bullets

         d. Cover yourself in dirt and sneak out
         """)
# To break the infinite loop, user must choose b or d option
    while True:
        # user prompt, user must choose to progress
        choice = input("> ")
        # user choices, a or c equal gameover, other choices = game continues
        if choice == "a":
            dead("Soul slayer eats you alive and burns your soul.")
        elif choice == "c":
            dead("""
            Slayer does not flinch as both bullets pass through.

            It's bone filthy hands grab you by the neck,
            and rips your spinal cord out and decapitates you.
            """)
        elif choice == "b" or "d":
            print("""
            You have escaped, and hide in a nearby mud lagoon.
            Which by sheer chance, shields you from the slayers smell sensor.
            """)
            # True value met, loop ends
            escaped = True
            # function called, next phase of game coming up
            search_plane()
        else:
            # if requirements not met, gameover
            dead("You are doomed.")

# a simple scenario for the user, option a to progress
def search_plane():
    print(""""
    Congratulations you have survived the night.
    Thankfully the demons do not appear during daytime, so you are safe.

    You need to search the remnants of the plane for any equipment and supplies.

    *type: a - search plane
         """)

         choice = input("> ")

         if choice == a:
             print("""
             The plane is a complete wreckage, however you find some burnt ham sandwiches& crumpled cafe lattes.
             More importantly during the search of the cockpit, the pilot radio is emitting a small crackle.
             Maybe someone is trying to get in contact, however you cannot get it beyond a crackle.

             You notice that when you bring it above your head, the crackle gets louder, perhaps if you construct an aerial,
             and find a higher point; you will be able to make contact.
             """)
             higher_point()
        else:
            dead("You collapse.")

def higher_point():
    print("""
    With tools you construct an aerial.
    You see a cliff top, towards the far middle right of the island.
    This is the best chance of gaining signal to be recused.

    You must determined your route, as there are three ways to reach the cliff.

    *type a, b, or c

    a. the beach, straight towards the cliff
    b. the forest to the left of the cliff
    c. a rocky hill to the right of the cliff

    remember you have limited supplies
    """)

    choic

start()
