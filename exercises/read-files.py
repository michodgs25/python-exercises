# import argument variable from system
from sys import argv

# attach script and filename to argument variable
script, filename = argv
# print string informing user that we are to erase the file
print(f"We're going to erase {filename}.")
# print suggestion to user
print("If you don't want that, hit CTRL-C (^C).")
# print second suggestion to user
print("If you do want that, hit RETURN.")
# Ask option the user would like to take
input("?")

# if user chooses second option, print opening file
print("Opening the file...")
# target this file and open
target = open(filename, 'w')

# print that the computer is emptying the file
print("Truncating the file.  Goodbye!")
# target file to be emptied
target.truncate()

# print string asking user to input three lines
print("Now I'm going to ask you for three lines.")

# define the three line variables, attach input method to each one
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# inform user that each line will be written into a separate file
print("I'm going to write these to the file.")

# target new file, write first line inputted by the user
target.write(line1)
# after each line there will be a newline
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# print to the console that the file will now be closed
print("And finally, we close it.")
# target the file and close it
target.close()
