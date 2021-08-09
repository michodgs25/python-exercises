# IS-A, HAS-A, OBJECTS, AND CLASSES

# An important concept that you have to understand is the difference between a class and an object.
# The problem is, there is no real difference between a class and an object.
# They are actually the same thing at different points in time.

# A class is not a real thing but a word that we attach to instances of a things with similar attributes.


# Two key phrases:
# is-a for objects& classes that are related to each other via a class relationship.

# has-a when objects& classes that are solely related only because they reference each other.

## Animal is-a object, first instance of Animal
class Animal(object):
    pass

# Dog has-a class, instance of object Animal
class Dog(Animal):

    def __init__(self, name):
        # is-a instance of __init__ param 'name'
        self.name = name

# Cat has-a class, instance of object animal
class Cat(Animal):

    def __init__(self, name):
        # is-a instance of __init__ param 'name'
        self.name = name

# Person is-a object, first instance of person
class Person(object):

    def __init__(self, name):
        # is-a instance of __init__ param 'name'
        self.name = name
