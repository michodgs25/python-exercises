# Define personal aspects
name = 'Michael Hodgson'
age = 25
height = 73 # inches
weight = 90 # Kilos
hair = 'Brown'
eyes = 'Green'
teeth = 'White'

# Convert weight measure from kilograms to pounds
# First ask the user to enter their weight in Kilos
kilo_grams = float(input('Enter weight in kg to Convert into pounds:'))
# every kilogram there are 2.2 pound multiplied by 2
pounds = kilo_grams * 2.2046
# print kilogram and pound equivalent
print(kilo_grams, ' kilograms =', pounds, ' Pounds')

# Convert feet& inches to cm
# User firstly enters their height
print("Input your height: ")
# enter feet amount i.e '5'
h_ft = int(input("Feet: "))
# enter inches amount i.e '11'
h_inch = int(input("Inches: "))

# height inches plus or equal to height feet
# Multiply by twelve
h_inch += h_ft * 12
# get height in cm equal to rounding height in inches
# Multiply height inches by 2.54 + 1
h_cm = round(h_inch * 2.54, 1)

# print height in cm
print("Your height is : %d cm." % h_cm)


print(f"Let's talk about {name}.")
print(f"He's {height} inches or {h_cm} tall.")
print(f"He's {weight} kilograms or {pounds} pounds.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the monster energy")

total = age + height + weight
equiv_total = age + h_cm + pounds
print(f"If I add my age {age} years old, how tall I am {height} inches,n\
and my weight {weight} kilograms, I get {total}.")
print(f"Or if I changed the height and weight measures:n\
 {age} years old, {h_cm} centimeters, and my weight {pounds} pounds I'd get {equiv_total}.")

print("Of course I am so much more, than the sum of these parts.")
