# Dictionaries

print("""
A dictionary or `dict` in Python, is a way to store data just like a list.
But instead of using only numbers to get the data, you can use almost anything.
This let's you treat a dict like it's a database for storing and organising data.
""")

print("Dictionary Example:")

# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# Create set of states with cities in them
cities = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jackonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# Print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the states then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}.")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get the abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")


print("""
What Dictionaries can do

A dictionary is another example of a data structure, and like a list,
it is one of the most commonly used data structures in programming.
A dict is used to map or associate things you want to store to keys you need to get.
 """)


# England cities and their football teams

# map city examples

england_cities = {
        'Birmingham': 'BI',
        'Aberdeen': 'AN',
        'leeds': 'LD',
        'Liverpool': 'LP',
        'Manchester': 'MA',
        'London': 'LCY'
}

# Map football teams
football_teams = {
         'BI': 'Aston Villa, Birmingham City',
         'AN': 'Aberdeen',
         'LP': 'Liverpool, Everton, Tramere Rovers',
         'MA': 'Manchester United, Manchester City, Salford',
         'LD': 'Leeds United',
         'LCY': 'Chelsea, Arsenal, Spurs, Crystal Palace, Fulham',
}

# print out some teams
print('-' * 10)
print("LCY city has: ", football_teams['LCY'])
print("MA city has: ", football_teams['MA'])
