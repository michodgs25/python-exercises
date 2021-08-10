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

        ## person has-a pet of some kind
        self.pet = None

# Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        # Super has-a init
        super(Employee, self).__init__(name)
        # self is-a salary
        self.salary = salary

# Fish is-a object, first instance of Fish
class Fish(object):
    pass

# Salmon has-a relationship with Fish
class Salmon(Fish):
    pass

# Halibut has-a relationship with Fish
class Halibut(Fish):
    pass


# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# from mary get pet attribute, set it to 'satan'
mary.pet = satan

# Set Frank to Employee, which takes two params "Frank" and 120000
frank = Employee("Frank", 120000)

# from frank get pet attribute and set it to rover
frank.pet = rover

# set flipper to class Fish()
flipper = Fish()

# set crouse to class Salmon()
crouse = Salmon()

# set harry to class Halibut()
harry = Halibut()

print("""
In python3, you do not need to add the (object) after the name of the class,
but the Python community believes in 'explicit is better than implicit'.
""")
