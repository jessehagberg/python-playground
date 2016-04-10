#set variable "cars" = 100
cars = 100
#set variable "space_in_a_car" = 4.0 which is a floating point number
space_in_a_car = 4
#set variable "drivers" = 30
drivers = 30
#set variable "passengers" to 90 which is three times the number of drivers
passengers = 90
#Calculate the number of cars that will not be driven and store in "cars_not_driven".
cars_not_driven = cars - drivers
#Set variable "cars_driven" = to the number of drivers stored in variable "drivers".
cars_driven = drivers
#calculate the overall capacity for carrying passengers for all driven cars and store in variable "carpool_capacity".
carpool_capacity = cars_driven * space_in_a_car
#calculate the average number of passengers per car and store in variable "average_passengers_per_car". 
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."