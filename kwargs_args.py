# The single star operator - *
# *args for packing - Finding a home for lost arguments
print("*args for packing - Finding a home for lost arguments.")
print("Create an array with 3 elements and then store each element in a different variable:")
a, b, c = [1, 2, 3]
print(f"a: {a}\nb: {b}\nc: {c}") #Simply printing them on separate lines for those not used to f-strings


print("What if you have only 3 variables and 6 elements to store?")
print("You can do this: a, b, c = array[0], array[1], array[2:]")
array = [1, 2, 3, 4, 5, 6]
a, b, c = array[0], array[1], array[2:]
print(f"a: {a}\nb: {b}\nc: {c}")
print("OR you can do this: a, b, *c = [1, 2, 3, 4, 5, 6]")
a, b, *c = [1, 2, 3, 4, 5, 6]
print(f"a: {a}\nb: {b}\nc: {c}")
print("\nThe * stands for a function that recognises objects left in limbo and puts them together in a list.")


print("Instead of *c, we could also have written *args, *random_name, *args_is_a_convention.")
print("because the actual word after the * is the name of the list name holding all the elements not already put inside a variable.")
print("For example: a, b, *args = [1, 2, 3, 4, 5, 6]")
a, b, *args = [1, 2, 3, 4, 5, 6]
print(args)

print("For example: a, b, *random_name = [1, 2, 3, 4, 5, 6]")
a, b, *random_name = [1, 2, 3, 4, 5, 6]
print(random_name)

print("We could just as easily save the first and last elements in a and c respectively and use * to store whatever is left.")
print("As follows: a, *args_is_a_convention, c = [1, 2, 3, 4, 5, 6]:")
a, *args_is_a_convention, c = [1, 2, 3, 4, 5, 6]
print(args_is_a_convention)

# *args for packing - Adding flexibility to your functions' argument intake
def basic_function(a, b, c):
    print(f"\n  a: {a}\nb: {b}\nc: {c}")

basic_function('The name', 2, False)

print("Basically, the function definition is acting in the same way as the variable declaration.")
print("If we want the function work in this case: a, b, c = ['The name', 2, False, 1, 'Last Name']")
print("We make c able to take in all the values that a and b fail to take for themselves.")
print("The function is modified slightly: def basic_function(a, b, *c):")
print("Then calling basic_function with values of ('The name', 2, False, 12, 5) gives c the last 3 values:")

def basic_function(a, b, *c):
    print(f"a: {a}\nb: {b}\nc: {c}\n")

basic_function('The name', 2, False, 12, 5)


print("c is a tuple. Eg. *name will simply take all the extra arguments and store them in a tuple called name.\n")
print("Creating and running the function, def basic_function(a, b, *args) gives: ")
def basic_function(a, b, *args):
    args_type = type(args)
    first_element = args[0]
    summed_args = sum(args)

    print(f"Type of args: {args_type}")
    print(f"First element of args list: {first_element}")
    print(f"Summed elements of args: {summed_args}\n")

basic_function('The name', False, 2, 5, 5)

print("args here was very much a tuple, we asked for its type (tuple...) and can get elements by index, sum it, etc.")
print("The function def example_of_sum(*args): with values (1, 9, 4, 6) creates an arg with all the values, in a tuple, which can be summed.")
print("There were no variables available other than *args (no a or b) and the resulting tuple args contained all the values provided.")

def example_of_sum(*args):
    print(sum(args),"\n")

example_of_sum(1, 9, 4, 6)

print("The other thing to note is that *args must be the last argument.")
print("def basic_function(a, *args, c):  ... creates an error.")
print("So def basic_function(a, *args, c): is WRONG, and def basic_function(a, c, *args): is RIGHT.\n")

# *args for unpacking - Setting list elements free
print("*args for unpacking - Setting list elements free.")
print("If you use * in a tuple or list (whether created with * or not), all the elements stored inside the tuple will be unpacked.")
print("Print (my_tuple) = (1, 2, 3)")
my_tuple = (1, 2, 3)
print(my_tuple)
print("Now print (*my_tuple) = (1, 2, 3)")
print(*my_tuple, "\n")

print("Other examples, print *my_list [1, 2, 3]")
my_list = [1, 2, 3]
print(*my_list)

print("print *my_set {1, 2, 3}")
my_set = {1, 2, 3}
print(*my_set)

print("print *my_dict {'first':1, 'second':2, 'third':3}")
my_dict = {'first':1, 'second':2, 'third':3}
print(*my_dict)
print("Useful for passing list elements as independent, into a function that expects independent values instead of a tuple or a list.\n")

print("Imagine for example that we don't have much control over the function definition (maybe its part of another library")
print("and you don't want to dig through the source code) and you happen to have your data stored in a tuple already:")
print("def function_from_library(a, b, c):")
print('    print(f"a: {a}b: {b}c: {c}")')

print('my_tuple = ("First Name", "Last Name", "email")')
print("you can now feed your tuple easily with:")

print("function_from_library(*my_tuple)")
print("a: First Name")
print("b: Last Name")
print("c: email\n")

# **kwargs for packing - Finding a home for lost keyword arguments
print("**kwargs for packing - Finding a home for lost keyword arguments.")
print("On the other hand, **kwargs packs key-value pairs into a dictionary.")
print("Function:  def using_kwargs(a, b, **c): and passing in: (a=4, b=[1, 2, 3], so_new=True, even_newer=100, freshest_of_all=[20, 5, 1])")

def using_kwargs(a, b, **c):
    print(f"a: {a}\nb: {b}\nc: {c}")

using_kwargs(a=4, b=[1, 2, 3], so_new=True, even_newer=100, freshest_of_all=[20, 5, 1])

print("""
We see here that all of the new named inputs that were not previously defined are now stored into a dictionary where the key
represents the name of the parameter , e.g. so_new and the value of that dictionary entry is the value passed in the function,
e.g. True. If this isn't great already, think that you can also use them together:
""")
print("Now using both args and kwargs, def using_both(a, *b, **c):")
def using_both(a, *b, **c):
    print(f"a: {a}\nargs: {b}\nkwargs: {c}")

using_both(4, 5, 6, "I'm an arg", [1, 2, 3], test="success", so="simple", where="I'm in a dictionary")
a: 4
args: (5, 6, "I'm an arg", [1, 2, 3])
kwargs: {'test': 'success', 'so': 'simple', 'where': "I'm in a dictionary"}

print(""" If it wasn't clear yet, I suggest you take an extra second to look at that previous example.
The idea is that a took the first input (the number 4), the b took the rest of the unnamed inputs
(the 5 all the way to the list [1, 2, 3]) because of the * and the c took all of the named inputs
because of the ** and the fact that the only really defined input we had was the a.
""")

print("The order of your parameters when defining the function matters. Always put your *args and **kwargs at the end.")

# def my_function(a, b, c, d, ...,  *args, **kwargs)
# Think of this when you use the function as well. If you tried to do something like this you would get an error
# (try it anyway to see):

# ERROR
## def my_function(a, b, c, d, *args, **kwargs):
##    pass #Since we can't leave this blank, we put pass to say "don't do anything"

## my_function(5, 4, 3, 2, 'extra arg', a='this is A', extra='extra kwarg')
# One might expect that since we are explicitly telling the function to put 'This is A' into the variable a,
# it would be able to take care of the "extra" arguments (5, 4, 3, 2 and 'extra arg') by putting them into args.
# However, the spot inside of a is taken by the 5 before you even reach your explicit use of a='This is A'.
# Be mindful of this type of situations.

print("*kwargs for unpacking - Setting dictionaries free")

def interesting_function(x, y):
    print(f'What an interesting result: {x + y}')

my_dict_data = {"x":2, "y":8}

interesting_function(**my_dict_data)
