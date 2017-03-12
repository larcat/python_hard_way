#Defines number of cars on the road
cars = 100
#Defines how many of my PEOPLES can fit in a car.
space_in_a_car = 4.0
#Number of drivers in the time period.
drivers = 30
#Number of passengers that will be tagging along.
passengers = 90
#Number of cars that won't be being driver, cause no one drives them.
cars_not_driven = cars - drivers
#Number of cars that will be driver. Assumes no inactive drivers.
cars_driven = drivers
#Calcs the excess capacity in cars after drviers accounted for.
carpool_capacity = cars_driven * space_in_a_car
#Calcs average people in a car during the time period.
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.") 

#The error in the example means that he hadn't actually assigned that
#var name to anything, so it errored out. Pretty verbose!

#1
	#In this case, since it is multiplicative, nothing. If division
	#that way lies madness.

# I like the print syntax in python 3 better, but that's probably because
# it is more R-like. That said, said I think it is more intuitive.
	

