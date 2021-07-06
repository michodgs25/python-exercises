# variables in your function are not connected to the variables in your script

# call cheese_and_crackers function, with two arguments inside
# print formatted string with each argument wrapped in curly braces
# print two other strings to the console
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
# print string to the console, informing the user they can input numbers into function directly
# call cheese_and_crackers function, attach numbers 20 and 30 inside the parenthesis
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
# print string, explaining user can call the arguments from above and attach
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# call cheese_and_crackers function with two variables defined above inside the the function parenthesis
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print string to the console
# call cheese_and_crackers function, with sum inside
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# explain to the user, that we can combine the variables and the maths
# call cheese_and_crackers function, with the variables and sum inside
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



def monster_cans_and_crates(monster_count, crates_of_monster):
    print(f"You have {monster_count} cans of monster.")
    print(f"What!??! We only have {crates_of_monster} crates of monster!")
    print("Christ thats not enough, our top customer won't be happy!!")
    print("Call the president, he has to know about this.")
    print("Call him now god dammit!!\n")
    print("Mr President we need to replenish our stores for Michael Hodgson!!")

monster_count = 500
crates_of_monster = 50
monster_cans_and_crates(500, 50 + 5000)
# monster_cans_and_crates(monster_count, crates_of_monster)
