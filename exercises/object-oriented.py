# OBJECT ORIENTED WORDS AND PHRASES

print("""
Python words and definitions:

* class - Tell Python to make a new type of thing

* object - has two meanings, the most basic type of thing, and any instance of some thing.

* Instance - what you get when you tell Python to create a class.

* def - how you define a function inside a class

* self - Inside the functions in a class, self is a variable for the instance/object being accessed.

* inheritance - The concept that one class can inherit traits from another class.

* composition -  The concept that a class can be composed of other classes as parts.

* attribute - A property classes have that are from composition and are usually variables.

* is-a - A phrase that to say that something inherits from another.

* has-a - A phrase to say that something is composed of other things or has a trait.
""")


class X(Y) # make a class named X that is-a Y

class X(object): def __init__(self, J) # class X has-a __init__ that takes self and J parameters

class X(object): def M(self, J) # class X has-a function named M that takes self and J parameters

foo = X() # set foo to an instance of class X

foo.M(J) # from foo, get the M function, and call it with parameters self, J

foo.K = Q # from foo, get the K attribute, and set it to Q


# In each of the above, where you can see X, Y, M, J, K, Q and foo
# I can treat them as blank spots:

# 1. make a class named ??? that is-a Y
# 2. class ??? has-a __init__ that takes self and ??? as parameters
# 3. class ??? has-a function named ??? that takes self and ??? as parameters
# 4. set ??? to an instance of class
# 5. from ??? get the ??? function& call it with self=??? and parameters ???
# 6. from ??? get the ??? attribute and set it to ???
