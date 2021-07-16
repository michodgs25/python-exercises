# Programs need to do repetitive things very quickly
# I am going to use a for-loop to build and print various lists

# The best way to store the results of a for-loop is via lists
# Here is a list example:

# hairs = ['brown', 'blonde', 'ginger']
# eyes = ['green', 'blue', 'brown']
# weights = [1, 2, 3, 4]

# You start the list with a left square bracket, which opens the list.
# Then you put each item you want in the list, separated by commas.
# Close the list with a right square bracket.
# Python then takes the list& all its contents and assigns it to the variable.


# create three lists, assign each to a variable
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this kind of for-loop goes through a list
for number in the_count:
    print(f"This is count{number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# we can also go through mixed lists
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got{i}")

# I can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# we can print the lists also
for i in elements:
    print(f"Element was: {i}")


# RANGE FUNCTION DEFINITION AND USE
# The function returns a sequence of numbers starting from 0 by default, and increments by 1
# and stops before a specified number.
# SYNTAX:
######## range(start, stop, step)
