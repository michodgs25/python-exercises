# In the last exercise I worked out some if-statements and then guess what they are and how they work.
# An if-statement creates what is called a "branch" in the code.
# Like one of those adventure books where you are asked to turn to one page if you make one choice and another if you go in a different direction.
# The if-statement tells the script, "if this boolean expression is 'True' run the code under it.
# Otherwise skip it."

# A colon at the end of a line is how you tell Python you are going to create a new "block of code",
# then indenting four spaces tells Python what lines of code are in the block.
# If the block is not indented, python will return an error.

people = 30
cars = 40
trucks = 15

# asks whether cars value is greater than people - True
if cars > people:
    # Above if-statement is true, string is printed
    print("We should take the cars.")
# elif statement provides an additional option to the above if-statement
# checking if cars value is less than people - False, so print statement is skipped
elif cars < people:
    print("We should not take the cars.")
    # if neither the if or elif statement is correct, else statement runs
else:
    print("We can't decide")

# if statement check whether trucks value is greater than cars = False
if trucks > cars:
    # if statement false, print statement ignored
    print("That's too many trucks.")
# elif statement checks whether truck value is less than cars = True
elif trucks < cars:
    # elif statement True, print statement is run
    print("Maybe we could take the trucks")
    # As elif = true, else statement is not run
else:
    print("We still can't decide.")

# checks if people value is greater than truck = True
if people > trucks:
    # if statement True, print statement is run
    print("Alright let's take the trucks.")
    # if statement = True, else print statement does not run
else:
    print("Fine let's stay home then")
