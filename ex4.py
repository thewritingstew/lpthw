# number of cars available
cars = 100

# number of seats in each car
space_in_a_car = 4.0

# number of drivers we have available
drivers = 30

# number of passengers we need to transport
passengers = 90

# number of cars that we don't have drivers for
cars_not_driven = cars - drivers

# number of cars that have drivers
cars_driven = drivers

# number of people we can take in the carpool
carpool_capacity = cars_driven * space_in_a_car

# number of people we need to put in each car in 
# order to get all passengers into cars driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "peoople today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."