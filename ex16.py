from sys import argv

script, filename = argv

print(f"We are going to remove a {filename}.")
print("If you don't want that hit CTRL-C (^C)")
print("If you do want that, press RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file.  Goodbye Bitch.")
target.truncate()

print("Now I am asking you for three lines:")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I am going to write these to the file.")

target.write("{0}\n{1}\n{2}\n".format(line1, line2, line3))

print("And we close it")

target.close()
