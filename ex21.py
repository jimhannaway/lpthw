# Functions Can REturn Something
""" This shows use of return to set variables from the output of functions"""

def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions")

age = add(50, 5)
height = subtract(72, 4)
weight = multiply(95, 2)
iq = divide(230, 2)

print(f"Age: {age}, Height: {height}, weight: {weight}, IQ: {iq}.")

# A puzzle for the extra credit, type it in anyway!
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print("That becomes: ", what, "Can you do it by hand?")
print("Yes. You must work right to left, calculating each function as you go.")
print("Then passing the result into the function immediately to its left. BooM!\n")

what2 = age + (height - (iq/2)*weight)
print("Resulting formula becomes age + (height - (iq/2)*weight)) = ", what2)

print("Let's try to make it a positive result with a different formula.")
what3 = (age / height) * (weight + iq)
print(what3)

what4 = multiply(divide(age,height),add(weight,iq))
print(f"Proving that {what3} does equal {what4}")
