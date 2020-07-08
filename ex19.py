# Functions & Variables
# Functions do 3 things, they
    # name pieces of Code the way variables name strings and numbers
    # take arguments the way scripts take argv
    # let you make your own "mini commands" using these first 2 things

""" This shows all different ways to pass values into our
    cheese_and_crackers function. We can pass in straight numbers,
    variables, maths calculations, even math calculations and variables together """

# Define the function 'cheese_and_crackers' to take in two values; cheese_count and boxes_of_crackers
# Then print out the values passed into the function with sme text around them t give context and meaning.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

# Pass two values directly into the cheese_and_crackers function
print("We can just give the funtion numbers directly:")
cheese_and_crackers(20, 30)

# Create two other variables amount_of_cheese and amount_of_crackers,
# assign values to them and an pass them into the cheese_and_crackers function.
print("OR we can use variables from our script.")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Run cheese_and_crackers function with values created from calculations inside the function
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Call (run) cheese_and_crackers with its passed in values created from
# a combination of existing variables with a math calculation
print("And we can combine the two, variable and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

count = 0

def function_ten_ways(numbers, letters):
    print(count)
    print(f"The numbers are {numbers} and the letters are {letters}.")

# 1st around
count = count + 1
function_ten_ways(0, "No letter")
print("No values passed this time! Doesn't work so passed in values directly!")

# 2nd call
count = count + 1
function_ten_ways(1, "A")
print("One value passed this time!")

# 3rd call
count = count + 1
function_ten_ways(1+1, "A"+"B")
print("Added values and strings passed this time!")

# 4th call
count = count + 1
function_ten_ways("1"+"1"+"2", "A"+"B"+"C")
print("Added strings passed as values this time!")

# 5th Call
amount_of_numbers = 10
amount_of_letters = 26
count = count + 1
function_ten_ways(amount_of_numbers, amount_of_letters)
print("Two new varaibles passed this time!")

# 6th Call
count = count + 1
function_ten_ways(amount_of_numbers *2 , amount_of_letters *2)
print("Two variables inclusing arithmetic operations passed this time!")

# 7th Call
count = count + 1
function_six = function_ten_ways
function_six(amount_of_numbers, amount_of_letters)
print("Asssign the function to a variable and call it again! Jeez it works")

# 8th Call
count = count + 1
function_six = function_ten_ways
new_list = (55, "ABCDE")
function_six(*new_list)
print("Asssign the function to a variable with a variable number of arguments as in *args. Yip. Works!")

# 9th call
count = count + 1
def function_seven():
    letters1 = "JHFH"
    numbers1 = 1509
    function_ten_ways(numbers1, letters1)
    print("Create a new function using the original function with new values and call the new function")
function_seven()

# 10th call
count = count + 1
def function_seven():
    letters1 = "XJHFHX"
    return letters1

def function_eight():
    numbers1 = "X" + 1509 + "X"
    return numbers1

function_ten_ways(function_seven, function_eight)
print("Create a new function pasing in two functions.")


# 11th call
count = count + 1
numbers2 = input("Input numbers: ")
letters2 = input("Input letters: ")
function_ten_ways(numbers2, letters2)
print("Call the function using user input as values.")
