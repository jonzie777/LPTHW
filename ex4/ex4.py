# Cars variable
cars = 100
# How much space is in a car
space_in_a_car = 4.0
# Drivers for the Cars
drivers = 30
# Passengers for the Cars
passengers = 90
# Cars that are not driven
cars_not_driven = cars - drivers
# Cars being driven
cars_driven = drivers
# Carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# average number of persons per car vs cars driven
average_passengers_per_car = passengers / cars_driven

# printing how many cars are available
print "There are", cars, "cars available."
# printing amount of available drivers
print "There are only", drivers, "drivers available."
# printing how many empty cars there will be for the day
print "There will be", cars_not_driven, "empty cars today."
# printing how many can be transported
print "We can transport", carpool_capacity, "people today."
# printing how many passengers are using the carpool today
print "We have", passengers, "to carpool today."
# printing how many need to be placed in each carpool
print "We need to put about". average_passengers_per_car, "in each car."
