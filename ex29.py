# Create three variables and attach a value to each
people = 20
cats = 30
dogs = 15

# if statement, checks whether there are less people than cats
if people < cats:
    # prints result
    print("Too many cats! The world is doomed!")

# if statement, checks whether there are more cats than people
if people > cats:
    # prints result
    print("Not many Cats! The world is saved!")

# if statement, check if more dogs than people
if people < dogs:
    # print result
    print("The world is drooled on!")

# if statement, check if more people than dogs
if people > dogs:
    # print result
    print("The world is dry!")

# add an increment of 5 to dog value
dogs += 5

# if statement, check whether people are greater than or equal to dogs
if people >= dogs:
    # print result
    print("People are greater than or equal to dogs.")

# if statement, check whether people are less than or equal to dogs
if people <= dogs:
    # print result
    print("People are less than or equal to dogs.")

# if equal statement, checks if people are dogs
if people == dogs:
    # print result
    print("People are dogs")


# 1. What do you think the `if` does to the code below it?
##### It indents the code, checks statement

# 2. Why does the code under the `if` need to be indented four spaces?
##### This allows the computer to read the return/print statement, else it cannot distinguish it from the other statements
