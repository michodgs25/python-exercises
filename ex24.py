# print string
print("Let's practice everything.")
# print string with escapy characters
print('You\'d need to know \'bout escapes with \\ that do:')
# print string using a newline and tab methods
print('\n newlines and \t tabs.')

# print long form string, applying newline '\n' and tab '\t' to separate the poem
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""
# print line separator, to space out the different strings
print("---------------------")
# print poem
print(poem)
print("---------------------")

# create five variable, attach sum to it
five = 10 - 2 + 3 - 6
# print formatted string, calling five variable
print(f"This should be five: {five}")
# create secret formula function
def secret_formula(started):
    # create jelly_beans variable, equal it to started mulipled by 500
    jelly_beans = started * 500
    # create jars variable, divide jelly_beans count by 1000
    jars = jelly_beans / 1000
    # create crates variable, divide crates by 100
    crates = jars / 100
    # return the value of each variable
    return jelly_beans, jars, crates

# create start_point variable, equal it to 10,000
start_point = 10000
# take the beans, jars, crates variables, equal to secret_formula with start_point in brackets
beans, jars, crates = secret_formula(start_point)

# This is another way to format a string
print("With a starting point of: {}".format(start_point))
# its just like an f"" starting
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
# call start_point variable, equal it to start_point divide by 10
start_point = start_point / 10
# print alternative method
print("We can also do that this way:")
# create new variable 'formula' eqaul it to secret_formula(start_point)
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
