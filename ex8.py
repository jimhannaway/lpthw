# Define the variable formatter
formatter = "{} {} {} {}"

# Print the variable formatter, each time passing in four different arguments
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
# Print the variable formatter with on-the-fly text string as arguments
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear."
))

# learning review completed
