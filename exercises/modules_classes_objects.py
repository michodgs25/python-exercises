# MODULES - CLASSES - OBJECTS

# Call/import mystuff module& run apple function and tangerine variable
import mystuff
mystuff.apple()
print(mystuff.tangerine)

print("""
Python is called an 'object oriented programming language'.

This means there is a construct within python called a class,
which let's you structure your software in a particular way.
Using classes can add consistency to your programs so that they be used in a cleaner way.
""")

print("""
Modules are like dictionaries
------------------------------

We have a very common pattern in python:

1. take a key=value style container
2. get something out of it by the key's name

In the case of the dictionary, the key is a string and the syntax is [key].

In the case of the module, the key is an identifier, and the syntax is .key
""")

print("""
Classes are like modules
------------------------------

You can think about a module as a specialized dictionary that can store python code,
so you can access it with the . operator.
Python also has another construct that serves a similar purpose called a class.

A class is a way to take a grouping of functions& data and place them inside a container,
so you can access them with the . (dot) operator.
""")


class moreStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apples(self):
        print("I AM CLASSY APPLES!")


print("""
A class looks more complicated in comparison to modules, due to there be more going on.
Class can be viewed as like a mini-module with moreStuff having an apple() function in it.
""")
