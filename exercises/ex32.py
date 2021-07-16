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

# LIST DESCRIPTION

# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data.
# The other three are:

# TUPLE: a collection which is ordered and unchangeable. Allows the duplicate members.
# SET: is a collection, which is unordered and unindexed. No duplicate members.
# DICTIONARY: a collection which is ordered and changeable. No duplicate members.

# All with different quality and usage.

# LIST ITEMS: are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index[0], the second item has index[1] etc.

# ORDERED: This means that the items have a defined order and that order will not change.
# If new items are added to the list, the new item will be placed at the end of the list.

# CHANGEABLE: a list can be changed, items can be added or removed after it has been created.

# DUPLICATES: lists are index, therefore lists can have items with same value.
# DUPLICATE EXAMPLE:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# LIST LENGTH: to determine how many items a list has, use the len() function
# LIST LENGTH EXAMPLE:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# LIST ITEMS - DATA TYPES:
# List items can be of any data type
# DATA TYPES EXAMPLE:
list1 = ["apple", "banana", "cherry"] # STRINGS
list2 = [1, 5, 7, 9, 3] # INTEGER
list3 = [True, False, False] # BOOLEANS
# A list with multiple different data types
list1 = ["abc", 34, True, 40, "male"]

# TYPE(): from Python perspective, lists are defined as objects with the data type list:
# <class 'list'>
# DATA TYPE EXAMPLE
mylist = ["apple", "banana", "cherry"] # data type = string
print(type(mylist))

# LIST() CONSTRUCTOR
# You can use the list() constructor when creating a new list
# LIST CONSTRUCTOR EXAMPLE:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

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
elements = [0, 1, 2, 3, 4, 5, 6]

# then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#    print(f"Adding {i} to the list.")
    # append is a function that lists understand
#    elements.append(i)

# we can print the lists also
for i in elements:
    print(f"Element was: {i}")


# RANGE FUNCTION DEFINITION AND USE
# The function returns a sequence of numbers starting from 0 by default, and increments by 1
# and stops before a specified number.
# SYNTAX:
######## range(start, stop, step)

################# PYTHON LIST METHODS

# APPEND(): Add a single element to the end of the list

# CLEAR(): Removes all items from the list

# COPY(): returns a shallow copy of the list

# COUNT(): returns count of the element in the list

# EXTEND(): adds iterable elements to the end of the list

# INDEX(): returns the index of the element in the list

# INSERT(): insert an element into the list

# POP(): removes item from the list

# REVERSE(): reverses the list

# SORT(): sorts elements of a list
