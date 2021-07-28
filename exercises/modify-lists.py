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
