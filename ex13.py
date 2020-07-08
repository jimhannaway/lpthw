# Parameters, Unpacking, Variables

from sys import argv
# read the WYSS sestion for how to run this
script, first, second, third, last = argv

print("THE SCRIPT IS CALLED:", script)
print("Your first variable is called:", first)
print("Your second variable is called:", second)
print("Your third variable is called:", third)
print("Your fourth variable is called:", last)

# now take some user input while the script is running
testq = input("Is this going ok? Just type Y or N: ")
if testq == "Y":
    print("Glad you like it!")
else:
    print("Yes, hard going eh? But keep at it, you'll get there!")

# Skip a line and print the list of all argv variables
print("\n")
print("Argument list: ", argv)
