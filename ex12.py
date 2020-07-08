# Prompting People

# C:\Users\Jim> python c:\users\Jim\'.\Documents\Python Scripts\lpthw\'ex12.py
# Can also enter C:\Users\Jim> python c:\users\Jim\Documents\'.\Python Scripts\lpthw\'ex12.py
# The part of the command entered in quotes is to allow Powershell to handle the spaces in the folder name

# Python's input() function allows user input.
# The input() method reads a line from input, converts into a string and returns it.
# The brackets can contain a prompt such as "Please enter your surname:"
# and assigned to the variable as in previous Ex11.
# or rewriting ex11 below to assign by this method  age = input("How old are you? ").

# We reduce the total lines of code by half
# this gets removed print("How old are you?", end=' ') # end=' ' prevents a newline at end of the question.
age = input("How old are you? ")
# this gets removed print("How tall are you in metres?", end=' ')
height = input("How tall are you in metres? ")
# this gets removed print("What weight are you in kg?", end=' ')
weight = input("What weight are you in kg?")

#Print f is Python 3.6 F-strings which improve formatting.
# Strings, held within curly brackets, get passed in by the previous code
print(f"So, you're {age} years old, {height}m tall and weigh in at {weight}kg.")
print("\n")
food = input("What's your favourite food? ")
drink = input("Which drink do you like best? ")
print(f"I like {food} and {drink} too!")
