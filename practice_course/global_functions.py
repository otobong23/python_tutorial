import math  # Importing the math module to use mathematical functions
import math as m  # Importing the math module with an alias 'm' to use mathematical functions
from math import (
    floor,
    ceil,
)  # Importing specific functions from the math module to use them directly without the module name
from sys import (
    argv,
    getrecursionlimit,
    setrecursionlimit,
)  # Importing the argv function from the sys module to access command-line arguments
from functools import (
    reduce,
)  # Importing the reduce function from the functools module to perform a reduction on a list of items
from practice import *  # Importing specific functions from the practice module to use them in this script. The * imports all functions defined in practice.py
# Regardless of the fact that practice.py is not in the same directory as this script, it is still accessible because it is in the same project and the project is added to the PYTHONPATH environment variable.


print(math.sqrt(16))  # Output: 4.0 - using the sqrt function from the math module
print(math.pi)  # Output: 3.141592653589793
print(
    floor(2.7), ceil(2.7)
)  # Output: 2 3 - using the floor and ceil functions from the math module


# input function
user_input: str = input(
    "Enter a Number: \n"
)  # Taking input from the user and storing it in a variable, \n indicates a new line in the prompt
print(
    f"you entered: {user_input}"
)  # Output: you entered: <user input> - using an f-string to format the input


# eval function
expression: str = input(
    "Enter a mathematical expression: \n"
)  # Taking a mathematical expression as input from the user
eval_result: float = eval(
    expression
)  # Evaluating the expression using the eval function and storing the result in a variable
print(
    f"The result of the expression is: {eval_result}"
)  # Output: The result of the result of the expression is: <evaluted result> - using an f-string to format the evaluted result


# argv function
#  argv: list[str] = ["script_name.py", "argument1", "argument2"] - Example of how argv looks up when a script is runned with command-line arguments
argument_1: str = argv[1]
argument_2: str = argv[2]
print(
    f"Argument 1: {argument_1} - type: {type(argument_1)}, Argument 2: {argument_2} - type: {type(argument_2)}"
)  # Output: Argument and types


# functions, rest parameters, kwargs paramters, destructuring
def print_with_parameters(name: str, age: int):
    print(name, age)


print_with_parameters(age=22, name="Miracle")  # Output: Miracle 22


def print_rest_parameter(a, b, *the_rest):
    print(a, b, the_rest)
    print(
        *the_rest
    )  # Output: each value outputed - * behind a variable is seen as a period seperator


print_rest_parameter(
    1, 2, 3, 4, 5, 6
)  # Output: 1 2 (3, 4, 5, 6) - the listed params with the rest in a tuple


def print_rest_parameter_with_argument(
    name, **the_rest_with_argument
):  # ** - this is called kwargs and it allows for keyword arguments to be passed as a dictionary
    print(name, the_rest_with_argument)


print_rest_parameter_with_argument(
    "miracle", age=22, level="fullstack", year="year 2"
)  # Output: miracle {'age': 22, 'level': 'fullstack', 'year': 'year 2'} - ** - the listed params with the rest in a dictionary


# Destructuring
destructure_dict = {"name": "Miracle", "age": 22}
destructure_list = [1, 2, 3, 4, 5]

print(
    {**destructure_dict, "year": "year 2"}
)  # Output: {'name': 'Miracle', 'age': 22, 'year': 'year 2'}
print([*destructure_list, 6, 7])  # Output: [1, 2, 3, 4, 5, 6, 7]

first, second = destructure_list  # first = 1, second = 2
first_from_list, *rest = destructure_list  # first_from_list = 1, *rest = [2, 3, 4, 5]
first_a, _, last_from_list = (
    destructure_list  # first_a = 1, last_from_list = 5, _ ignores the rest from the list
)


# scope and global
a = 1
b = 5


def do_something():
    global a  # this helps get the global variable and reassigning it rather than creating a new local variale
    a = 2  # assigning 2 to the global a

    globals()["b"] = (
        9  # this is another method of reassigning a global variable while being in touch with the local one
    )
    b = 7

    def second_scopped():
        nonlocal b  # used to get the variable from the parent function scope in the child function scope
        b = 8

    second_scopped()

    print(b)


do_something()
print(a, b)


# RecursionLimit
print(
    "System recursion limit: {}".format(getrecursionlimit())
)  # Output: System recursion limit: 1000
setrecursionlimit(1100)  # Setting a new recursion limit
print(
    "updated recursion limit: {}".format(getrecursionlimit())
)  # Output: updated recursion limit: 1100


# Anonymous function (lambda)
add = lambda x, y: (
    x + y
)  # A lambda function that takes two parameters and returns their sum
print(add(5, 3))  # Output: 8


# list filtering, mapping and reducing
members = [1, 2, 3, 4, 5, 6]
odd_members = list(
    filter(lambda x: x % 2, members)
)  # Using filter with a lambda function to get odd numbers from the members list


def is_even(x):
    return x % 2 == 0


even_members = list(
    filter(is_even, members)
)  # Using filter with a named function to get even numbers from the members list
print(
    "Odd members: {}, Even members: {}".format(odd_members, even_members)
)  # Ouput: Odd members: [1, 3, 5], Even members: [2, 4, 6]

mapped_members = list(
    map(lambda x: x * 2, members)
)  # Using map with a lambda function to double each member in the members list
print(
    "Mapped members: {}".format(mapped_members)
)  # Output: Mapped members: [2, 4, 6, 8, 10, 12]

reduced_members_sum = sum(
    members
)  # Using the built-in sum function to reduce the members list to their total sum
reduced_members_product = reduce(
    lambda x, y: x * y, members
)  # Using reduce with a lambda function to calculate the product of all members in the members list
print(
    "sum of members: {}, product of members: {}".format(
        reduced_members_sum, reduced_members_product
    )
)  # Output: sum of members: 21, product of members: 720


# Decorators
def main_function(n: int):
    print("This is the main function with a value of {}".format(n))


def decorator_function(func):
    def wrapper(n):
        print("This is the wrapper function")
        func(n * 2)  # Modifying the input value before passing it to the main function

    return wrapper


main_function = decorator_function(
    main_function
)  # Decorating the main function with the decorator function
main_function(5)

print("The factorial of 5 is: {}".format(factorial_function(5)))  # Output: 120


# special variables
print(
    __name__
)  # Output: __main__ or <module_name> - this variable holds the name of the current module,
# if the script is run directly, it will be __main__.
# If the script is imported as a module in another script, it will hold the name of the module <module_name>.
# This is often used to check if a script is being run directly or imported as a module.


# Zip - The zip function can be use to create a key value pair object with a set of tuple, list, set
names = ["Miracle", "Favor", "Princess", "Precious"]
companies = ("Dell", "Apple", "Gucci", "MS")

Dictionary_zipped = dict(
    zip(names, companies)
)  # A dictionary made of a zipped list and tuple
Tuple_zipped = tuple(zip(names, companies))  # A Tuple made of a zipped list and tuple
print(
    Dictionary_zipped
)  # Output: {'Miracle': 'Dell', 'Favor': 'Apple', 'Princess': 'Gucci', 'Precious': 'MS'}
print(
    Tuple_zipped
)  # Output: (('Miracle', 'Dell'), ('Favor', 'Apple'), ('Princess', 'Gucci'), ('Precious', 'MS'))
