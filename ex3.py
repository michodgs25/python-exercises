# define car quantity
cars = 100
# define car space
space_in_a_car = 4.0
# state how many drivers and passengers
drivers = 30
passengers = 90
# If car not driven there are no drivers
cars_not_driven = cars - drivers
# if car driven there are drivers
cars_driven = drivers
# calculate car capacity by = to cars driven multiplied by space
carpool_capacity = cars_driven * space_in_a_car
# calculate average passenger per car = to passengers divided by cars driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available. ")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
