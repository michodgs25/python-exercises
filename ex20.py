from sys import argv

script, input_file = argv

# create print all function with an argument of 'f'
def print_all(f):
# print file content to the console
    print(f.read())

# create rewind function with an argument of 'f' for file
def rewind(f):
# move to the start of the file using seek(0)
    f.seek(0)

# create print_a_line function with arguments of 'line_count' and 'f' for file
def print_a_line(line_count, f):

# print file line amount and using readline method to print each line of the file
    print(line_count, f.readline())

# set current file variable, return open function with an argument of input file
current_file = open(input_file)

# print string to the console
print("First let's print the whole file:\n")

# call print_all function with current_file variable as an argument
print_all(current_file)

# print string to the console
print("Now let's rewind, kind of like a tape.")

# call rewind function with argument of current_file
rewind(current_file)

# print string to the console
print("Let's print three lines:")

# call current_line and equal it to one line
current_line = 1
# call print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)

# call current_line and equal it to current_line plus one
current_line = current_line + 1
# call print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)

# call current_line and equal it to current_line plus one
current_line = current_line + 1
# call current_line and equal it to one line
print_a_line(current_line, current_file)
