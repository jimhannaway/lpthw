# Set no of cars to 100
cars = 100
# Set no of seats in a car.
# Use float type as there may be half seats (eg luggage) affecting total capacity
space_in_a_car = 4.0
# Set the number of driver
drivers = 30
#Set the number of passengers
passengers = 90
# Calculate the numbr of cars that can be driven / not driven
cars_not_driven = cars - drivers
cars_driven = drivers
# Calcate the car pool capacity and the average passengers per car
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "people to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Completed the following in Powershell Terminal: Type python enter
i = 6
x = 2
j = 4

print(i)
print(i,j,x)
print(j ** x)
print(j ** x / i)
i == j # False
i == j == x # False
i % j == x # True

# learning review completed
