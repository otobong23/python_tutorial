# practice_course/practices.types.py
# types declaration and usage in python

# Importing necessary types
from typing import List, Callable
from array import array
import numpy

# String
my_string: str = "Hello World"

# Integer
my_integer: int = 42

# Float
my_float: float = 3.14

# Boolean
my_boolean: bool = True

# Tuple
my_tuple: tuple[int, str] = (1, "Tuple Example") # Tuples are ordered collections of elements that cannot be modified, can be accessed with indexing
print(my_tuple.count("Tuple Example"), my_tuple.index("Tuple Example")) # How many times "Tuple Example" appears in the tuple and the index of the first occurrence of "Tuple Example" in the tuple

# List
my_numbers: list[int] = [1, 2, 3, 4, 5] # List are ordered collections of elements that can be modified
my_numbers.append(6) # Adding an element to the list
my_numbers.pop() # Removing the last element from the list
print(min(my_numbers), max(my_numbers), sum(my_numbers)) # Output: 1 5 15 - Finding the minimum, maximum, and sum of the numbers in the list
print(len(my_numbers), my_numbers.__len__()) # Output: 5 5 - means of getting the length of the list

# Set
my_set: set[str] = {"apple", "banana", "cherry"} # Sets are unordered collections of unique elements
my_set.add("pawpaw") # Adding an element to the set
my_set.remove("cherry") # Removing an element from the set

# Dictionary (key-value pairs)
def greet() -> None:
   print("Hello World")

my_dictionary: dict[str, str | int | Callable[..., None]] = {
   "firstName": "Miracle",
   "lastName": "Boniface",
   "age": 21,
   "greet": greet,
   "message": lambda m: print(f"Hello {m}") 
}
print(my_dictionary["firstName"], my_dictionary.get("age"), my_dictionary.values(), my_dictionary.keys()) # Output: Miracle 21 dict_values(['Miracle', 'Boniface', 21, <function greet at 0x00000220CA37F880>, <function <lambda> at 0x00000220CA3FD620>]) dict_keys(['firstName', 'lastName', 'age', 'greet', 'message'])

# Function with type annotations
def sum_numbers(numbers: List[int]) -> List[int]:
   total = sum(numbers)
   max_number = max(numbers)
   min_number = min(numbers)
   return [total, max_number, min_number]

def print_text_and_number(text: str, number: int) -> None:
   print(f"{text} {number}")

# Class with type annotations
class Person:
   def __init__(self, first_name: str, last_name: str, age: int):
      self.first_name: str = first_name
      self.last_name: str = last_name
      self.age: int = age

print('converted Text \n with a new line character \t and a tab character')
print(r'This is a raw string, it will not process escape character like \n or \t')


print(type(my_string), type(my_integer), type(my_boolean), type(my_float)) # Output: <class 'str'> <class 'int'> <class 'bool'> <class 'float'>
print(str(my_integer), bool(my_string), complex(my_float, my_integer)) # Output: '42' True (3.14+42j)

# sequence types
print(type(my_tuple), type(my_numbers), type(my_set)) # Output: <class 'tuple'> <class 'list'> <class 'set'>
print(my_tuple[0], my_numbers[1], "banana" in my_set) # Output: 1 2 True
print(tuple(range(5)), list(range(5)), set(range(5))) # Output: (0, 1, 2, 3, 4) [0, 1, 2, 3, 4] {0, 1, 2, 3, 4}

# range
print(type(range)) # Output: <class 'type'>
print(list(range(2, 10, 2))) # Output: [2, 4, 6, 8] - range from 2 to 10 with a step of 2


# Logical operators
print(True and False, True or False, not True) # Output: False True False
print(True != False, True and not False, not (True or False)) # Output: True True False

# Bitwise operators and Binary representation
print(5 & 3, 5 | 3, 5 ^ 3, ~5) # 1 7 6 -6 - Bitwise AND, OR, XOR, and NOT (tilde) operations on the binary representations of the numbers
print(5 << 1, 5 >> 1) # Output: 10 2 - Bitwise left shift and right shift operations on the binary representation of the number
print(bin(5), bin(3), bin(~5)) # Output: 0b101 0b11 -0b110 - Binary representation of numbers, where '0b' prefix indicates a binary number
binary_number: int = 0b1010 # Binary literal for the number 10
print(int(binary_number), int(0b110)) # Output: 10 6 - converting binary to decimal
print(int('101', 2), int('101', 3), int('101', 4,), int('101', 7), int('101', 8), int('101', 16)) # Output:5 10 17 50 65 257 - converting string representations of numbers in different bases to decimal



# Hexadecimal and Octal literals
hexadecimal_number: int = 0x1A # Hexadecimal literal for the number 26
octal_number: int = 0o12 # Octal literal for the number 10
print(int(hexadecimal_number), int(octal_number)) # Output: 26 10 -converting hexadecimal and octal literals to decimal
print(hex(26), oct(10)) # Output: 0x1a 0o12 - converting decimal numbers to hexadecimal and octal literals



# Array
my_number_array: array = array('i', [1, 2, 3, 4, 5]) # Arrays are simiilar to lists but can only contain elements of the same type and are more memory efficient
my_string_array: array = array('u', ['H', 'w']) # Array of Unicode characters
# 'unsigned integer' - i, 'signed integer' - I, 'float' - f, 'double' - d(double precision float), 'unicode character' - u (for text data)
print(my_number_array, my_string_array)

new_arr = array(my_number_array.typecode, (x for x in my_number_array)) # creating a new array using a generator expression to copy elements from an existing array
print(new_arr)



# numpy array
my_numpy_number_array: numpy.ndarray = numpy.array([1, 2, 3, 4, 5], dtype=int) # numpy arrays are similar to Python Array but are more powerful and can handle multi-dimensional data and support a wide range of mathematical operations
print(my_numpy_number_array, my_numpy_number_array.dtype) 



# concatenating arrays
concatenated_array: numpy.ndarray = numpy.concatenate([my_numpy_number_array, numpy.array(my_numbers)]) # Concatenating a numpy array with a list by converting the list to a numpy array first
print(concatenated_array)



# copying arrays
copied_array: numpy.ndarray = my_numpy_number_array.copy() # Creating a copy of a numpy array
print(copied_array, id(copied_array), id(my_numpy_number_array))



# matrix with numpy
my_numpy_matrix: numpy.ndarray = numpy.array([[1, 2, 3], [4, 5, 6]]) # Creating a 2D array (matrix) using numpy
print(my_numpy_matrix, my_numpy_matrix.shape, my_numpy_matrix.flatten(), my_numpy_matrix.reshape(3, 2)) # shape - displays the existing dimension, flatten - makes the matrix one dimension, reshape - reshapes the dimension to specified rows and column

my_matrix_1 = numpy.matrix(my_numpy_matrix)
my_matrix_2 = numpy.matrix("1 2 3 ; 4 5 6 ; 7 8 9")
print(my_matrix_2, my_matrix_2.diagonal(), numpy.diagonal(my_matrix_2))