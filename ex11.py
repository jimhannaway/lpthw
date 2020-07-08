# Asking Questions
# Python's input() function allows user input.
# The input() method reads a line from input, converts into a string and returns it.
# The brackets can contain a prompt such as "Please enter your surname:"
# or be left empty and assigned to the variable as below
# or assigned by this method  age = input("How old are you? ").

print("How old are you?", end=' ') # end=' ' prevents a newline at end of the question.
age = input()
print("How tall are you in metres?", end=' ')
height = input()
print("What weight are you in kg?", end=' ')
weight = input()

#Print f is Python 3.6 F-strings which improve formatting.
# Strings, held within curly brackets, get passed in by the previous code
print(f"So, you're {age} years old, {height}m tall and weigh in at {weight}kg.")

food = input("What's your favourite food? ")
drink = input("Which drink do you like best? ")
print(f"I like {food} and {drink} too!")
