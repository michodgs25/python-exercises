# import argument variable
from sys import argv

# attach script& filename to argv (variable)
script, filename = argv

# Inform txt file to open when called
txt = open(filename)

# print a string, informing user of file
print(f"Here's your file {filename}:")
# read file contents, print to the command line
print(txt.read())
# close file once read
txt.close()

# Inform user to type the filename again
print(f"Type the filename again:")
file_again = input("> ")
# once correct name is inputted, file opens
txt_again = open(file_again)
# read file contents, print to the command line
print(txt_again.read())
# close file after being read
txt_again.close()
