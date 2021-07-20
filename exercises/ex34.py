# Accessing Elements of Lists

# Lists are useful, but unless you can get things in them, they aren't all that good.

animals = ['Bear', 'Tiger', 'Penguin', 'Zebra']
Bear = animals[0]
# take a list of animals, and then you get the(1st) one using 0?
# Python lists start at 0

# Everytime "I want the third animal," translate this ordinal number to a cardinal number by subtracting 1.
# The third animal is at index 2 which is the Penguin

# REMEMBER: ordinal == ordered, 1st;
#           cardinal == cards at random, 0
#         0/first   1/second     2/third   3/fourth    4/fifth   5/sixth
animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

# 1. animal at 1 is python3.6

# 2. the third animal is a peacock

# 3. the first animal is a bear

# 4. the animal at 3 is a kangaroo

# 5. the fith animal is a whale

# 6. the animal at 2 is a peacock

# 7. the sixth animal is a platypus

# 8. The animal at 4 is a whale

print(animals)
print(animals[0]) # ordinal: first,  Cardinal: 0
print(animals[1]) # ordinal: second, Cardinal: 1
print(animals[2]) # ordinal: third,  Cardinal: 2
print(animals[3]) # ordinal: fourth, Cardinal: 3
print(animals[4]) # ordinal: fifth,  Cardinal: 4
print(animals[5]) # ordinal: sixth,  Cardinal: 5
