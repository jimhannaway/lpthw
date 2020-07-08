# Define x as the variable formatted by using
# some text containing another variable called types_of_people.
types_of_people = 10
x = f"There are {types_of_people} types of people"

# Define y as the variable formatted by using
# some text containing another wo variables
# called binary and do_not.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# Now print two strings containing some text and a variable.
# One string containing variable x and the other variable y.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Set the variable hilarious to false and set the variable
# joke_evaluation to some text plus blank format variable.
# then print the joke_evaluation variable
# and amend the format using hilarious to add False at the end of the string.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

# Show that two string variables are concatenated uing the plus sign
w = "This is the left side of ..."
e = "a string with a right side."

print (w + e)
