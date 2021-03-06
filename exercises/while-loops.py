# WHILE LOOP
# A while-loop will keep executing the code block under it as long the BOOLEAN expression is True
# While-loops simply do a test like a if-statement, but instead of running the code block once,
# the loop jumps back to the top where the while is, and repeat the cycle.
# A while-loop runs until the expression is False.

# However while-loops sometimes do not stop, this is great if you want this,
# otherwise you always want the loop to end eventually.

# WHILE-LOOP RULES

# 1. Ensure to use while-loops sparingly. Usually a for loop is better.
# 2. Review while-statements and make sure that the boolean test will become False at some point.
# 3. When in doubt print out your test variable at the top and bottom of the while-loop to see what's it doing.


# while loop
# i = 0
# numbers = []

# while i < six:
#    print(f"At the top i is {i}")
#    numbers.append(i)

#    i = i + 1
#    print("Numbers now: ", numbers)
#    print(f"At the bottom i is {i}")

# print("The numbers: ")

# for num in numbers:
#    print(num)


# converted while loop in to a function that can called
def loopy(i, x, numbers):
    if (i < x):
        print("At the top i is %d" %i)
        numbers.append(i)

        i += 3
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" %i)
        loopy(i, x, numbers)
    return numbers

numbers = loopy(0, 10, [])
for num in numbers:
    print(num)
