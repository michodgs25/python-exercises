# I have learned about lists. When learning about while-loops I appended numbers to the end of a list and printed them out.

# Previously used the 'append' method, when I created the mystuff.append('hello'), I am setting off a chain of events inside Python, to cause something to happen to the mystuff list.

# Here's how it works:

# 1.

# Python sees you mentioned mystuff and looks up that variable.
# It might have to look backward to see if you created it with =,
# if it is a function argument, or even if it's a global variable.
# Either way, it has to find mystuff first.

# 2.

# Once it finds mystuff it reads the . (period) operator,
# and starts to looks at variables that are part of mystuff says it owns.
# Since mystuff is a list, thus it knows that mystuff has a bunch of functions.

# 3.

# It then hits append and compares the name to all the names that mystuff says it owns.
# If append is in there (it is), then Python grabs that to use.

# 4.

# Next Python sees the ( (open parethesis) ) and realises, "oh hey, this should be a function.""
# At this point it calls/runs/executes the function just like normal, but it calls the function with an extra argument.

# 5.

# That extra argument is...mystuff. What happens, at the end of all this, is a function call that looks like append(mystuff, 'hello')

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))




#                          WHAT LISTS CAN DO
# ----------------------------------------------------------------------------
# Let's say you want to create a computer game based on go fish.
# To do this you would need to have some way of taking the concept of a "deck of cards",
# and putting it into your Python program.

# You then have to write Python code that knows how to work this imaginary version of a deck of cards,
# so that a person playing your game thinks that it is real, even if it isn't.
# What you need is a "deck of cards" structure, and programmers call this kind of thing a data structure.

# A data structure is just a formal way to structure some data.
# Even if some data structures can get very complex, all they are is just a way to store facts inside a program.
# So you can access them in different ways. They structure data.

# Lists are one of the most common data structures programmers use.
# A list is an ordered list of things you want to store and access randomly or linearly by an index.

# Deck of cards list example:

# 1. You have a bunch of cards with values

# 2. Those cards are in a stack, list, or list from the top card to the bottom card.

# 3. You can take cards off the top, the bottom or the middle at random.

# 4. If you want to find a specific card, you have to grab the deck and go through it one at a time.

print("An ordered list, the deck of cards is in order, with a first and a last.")
print("of things you want to store, cards can be things I want to store.")
print("And access randomly. Any card from the deck can be accessed at random.")
print("Or accessed linearly, start at the beginning and go through the deck in order.")
print("By an index, access the card by its index position in the deck.")

print("""
That is all a list does.
Every concept in programming usually has some relationship to the real world, at least the usedful ones.
""")


# WHEN TO USE LISTS
# --------------------

print("""
You can use a list whenever you have something that matches the list data structure's useful features:
     1. If you need to maintain order. This is listed order not sorted order, Lists do not sort for you.

     2. If you need to access the contents randomly by a number, remember this uses cardinal numbers: start at 0.

     3. If you need to go through the contents linearly(first to last). Remember that's what for-loops are for.
 """)
