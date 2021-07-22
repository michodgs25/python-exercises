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

# define death, gameover finished
def dead(why):
    print(why, "Good job!")
    exit(0)
# define start of game
def start():
    print("""
    You awake amidst the wreckage of your private plane.
    It's the middle of the night, and the only light for miles around,
    are the burning flames rapidly making their way towards you from the cockpit.
    You must react quickly to get out of the plane.

    Type: cut seatbelt
    """)

    choice = input("> ")

    if choice == "cut seatbelt":
        print("Well done, now exit the plane before it explodes!")
    else:
        dead("You burn alive")
        exit()

start()
