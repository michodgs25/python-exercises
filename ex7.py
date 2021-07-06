#  Create formatter variable, pass four curly bracket arguments
formatter = "{} {} {} {}"

# print each line to the console
# the formatter.format informs the program
# to replace the previous arguments passed to the variable 'formatter'
# with new values stated within the format( '' ) method
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one,", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Life is like a",
"box of chocolates",
"you never know what",
"your gonna get...Jennaaaaay"
))
