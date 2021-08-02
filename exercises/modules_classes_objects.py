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


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


print("""
A class looks more complicated in comparison to modules, due to there be more going on.

Class can be viewed as like a mini-module with myStuff having an apple() function in it.
Also the use of __init__() function and use of self.tangerine for setting the tangerine instance variable.

Classes are used more often instead of modules:
                you can the myStuff class and use it to craft many of them, millions more if you like,
                and each one won't interfere with each other.
                When you import a module there is only one for the entire program.
""")


print("""
Objects are like import
---------------------------

If a class is like a mini-module, then there has to be a concept similar to import but for classes.

That concept is called instantiate, which is just another way of saying create.
When you instantiate/create a class, what you get is an object.

You instantiate(create) a class by calling the class like it's a function:
""")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

print("""
The first line is the instantiate operation, which is similar to calling a function.
However Python, coordinates a sequence of events behind the scenes:

1. Python looks for MyStuff() and sees that it is a class that you've defined.

2. Python crafts an empty object with all functions you've specified in the class using def.

3. Python then looks to see if you made a magic __init__function,
and if you have it calls that function to initialize your newly created object.

4. In the myStuff function __init__ you then get this extra variable, self,
which is that empty object Python made for you, and you can set variables on it,
just like you would with a module, dictionary, or other object.

5. In this case, you set self.tangerine to a song lyric, and then you've initialized this object.

6. Now Python can take this newly minted object and assign it to the thing variable for you to work with.

The above is the basics of how Python does this mini import when you call a class like a function.
This is not using the class but instead is using the class blueprint for building a copy of that thing.

At this point classes and objects diverge from modules at this point:

- Classes are like blueprints or definitions for creating new mini-modules.

- Instantiation is how you make one of these mini-modules and import it at the same time.
  Instatiate just means to create an object from the class.

- The resulting created mini-module is called an object,
  and you then assign it to a variable to work with it.
""")

print("""
Getting things from things
--------------------------------
""")

#dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
