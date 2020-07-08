# Numbers & Math

print("I will now count chickens:")

# No of hens is 25 plus (30/6=5) which is 30 in total
# Order of math calculates 30/6 first
print("Hens", 25 + 30 / 6)

# No of cocks is 100 minus (remainder of (25*3)/4
# So as 3 is the remainder of 75/4
# Order of match calcuates remainder of 75/4=3 first
# Then the result is 100 - 3.
print("Cocks", float(100 - 25 * 3 % 4)) # using float to ensure type is set for this calc
print(3 % 4)

# Order of math is PEMDAS (left to right order of math operations: Parentheses, Exponents, Multiply, Divide, Add, Subtract)
# Can be thought of as PE(M&D)(A&S)
# Order of math is therefore (4%2=0), (1/4=0.25), then (3+2+1-5+(0)-(0.25)+6)
# Result is 6.75
print("Now I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# Boolean comparison of (3 + 2) being > (5 - 7) gives false
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 -7)

print("Oh, that's why its false")

# Additional Calculation
print("Calculate the number of seconds in half a day:")
print("60 seconds in a minute:", 60, "seconds in a minute")
print("60 minutes in an hour:", 60 * 60,  "seconds in an hour")
print("There are 24 hours in a day so half a day is 12 hours which is:", 60 * 60 *12, "seconds in a half day")

# check spelling on comments and modify the file upload title
# learning review completed
