def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!\n")

age = subtract(30, 5)
height = add(78, 4)
weight = divide(90, 2)
iq = multiply(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ {iq}.\n")

# A puzzle for extra credit and showing off
print("Here is the puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 3))))

print("That becomes: ", what, "Can you do it by hand?\n")

# inverse formula, left iq to the end as had integer arg
inverse = multiply(weight, subtract(height, add(age, divide(iq, 2))))
print("A somewhat:", inverse, "an inverse formula. No I cannot do it by hand.\n")

# random formula
how = multiply(age, multiply(height, subtract(weight, add(iq, 2))))
print("This is: ", how, "how a random formula goes.\n" )

# My own function returning baked beans preference
def baked_beans(h, c):
    print(f"COOKING {h}, {c}")
    return baked_beans

h = "hot"
c = "cold"

print(f"I love having baked beans doesn't matter if {h} or {c}.")
