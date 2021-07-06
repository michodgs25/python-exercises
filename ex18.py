# def print_two variable, attach two arguments to args 'arg1' + 'arg2'
# print arg1 and arg2 to the console
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
# create function, attach two arguments
# print arguments to the console
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
# Create function, attach one arguments
# print one argument to the console
def print_one(arg1):
    print(f"arg1: {arg1}")
# create function with no arguments
# print string to the console
def print_none():
    print("I got nothing")
# call/run/use each function
# a string is used for each argument
print_two("Michael", "Hodgson")
print_two_again("Michael", "Hodgson")
print_one("First!")
print_none()
