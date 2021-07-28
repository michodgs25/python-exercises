from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
print(f"Also {user_name}, do you like grapes?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What is your age {user_name}?")
age = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me and grapes.
You are {age} years old. Ooof getting on.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
