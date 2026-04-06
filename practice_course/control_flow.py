# practice_course/practices.control_flow.py

# control flow statements in python
# Importing necessary types
from typing import List, Callable

# Range
my_range: range = range(1, 10)

# Range in List
my_range_List: List[int] = list(my_range)
print(my_range_List) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]



# If-Else Statement
def check_number(num: int) -> str:
   if bool(num):
      return "Positive"
   else:
      return "Negative"
   
def check_number_with_elif(num: int) -> str:
   if num > 0:
      return "Number is 0"
   elif num > 0:
      return "Positive"
   else:
      return "Negative"





# For Loop
def iterate_numbers(numbers: List[int]) -> None:
   for number in numbers:
      if number % 2 != 0:
         print(f"Odd Number: {number}")
         continue
      elif number == 0:
         print('Zero Encountered')
         break
      print(f"Even Number: {number}")
   print("Iteration Complete")

iterate_numbers([*my_range_List, 0]) # *param is used for distributed values




# While Loop
def countdown(start: int) -> None:
   while start > 0:
      print(f"Countdown: {start}")
      start -= 1
      if start == 0:
         print("Countdown Finished!")
         break
      print("Countdown Not Finished!")




# Infinite Loop
def infinite_Loop() -> None:
   while True:
      print("This is an infinite Loop")
      continue




# Do Nothing
def do_nothing() -> None:
   pass

def prime_numbers_up_to(num: int) -> None:
   for n in range(1, num):
      for i in range(2, n):
         if n % i == 0:
            break
      else:
         print(n, end=" ")

prime_numbers_up_to(100)





# iterators
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list) # Creating an iterator from the list
print(my_iterator.__next__(), next(my_iterator)) # Output: 1 2 - using the __next__ method and next function to get the next item from the iterator. when any of the function is called, it returns the next item while preserving the state of the iterator, so the next time it is called, it will return the next item in the list.

class my_Top_10_iterator:
   def __init__(self) -> None:
      self.num = 1
   
   def __iter__(self):
      return self
   
   def __next__(self):
      if self.num > 10:
         raise StopIteration # This is used to signal that there are no more item to iterate over, and it is used in the __next__ method to stop the iteration when a certain condition is met.
      current_num = self.num
      self.num += 1
      return current_num
   
top_10_values = my_Top_10_iterator()
for value in top_10_values: # Output: 1 2 3 4 5 6 7 8 9 10 - using a for loop to iterate over the custom iterator, which will call the __iter__ method to get the iterator object and then call the __next__ method to get each item until StopIteration is raised.
   print(value)




# generators
def my_generator(n: int):
   for i in range(n):
      yield i # The yield statement is used to produce a value from the generator function and pause its execution, allowing it to be resumed later to produce the next value.

gen = my_generator(5) 
for value in gen: # Output: 0 1 2 3 4
   print(value)




# Exception Handling
# There are three types of erros in python - SyntaxError, RuntimeError, LogicalError
# SyntaxError occurs when there is a mistake in the syntax of the code, such as missing a parenthesis or a colon.
# RuntimeError occurs when there is an error during the execution of the code, such as user inputting a non-integer value when an integer is expected.
# LogicalError occurs when the code runs without any syntax or runtime errors, but it produces an incorrect result due to a mistake in the logic of the code.

# try-except block
def divide_numbers(a: int, b: int) -> float:
   try:
      result = a / b

   except ZeroDivisionError: # This is used to catch the specific error of division by zero and handle it gracefully instead of crashing the program.
      print("Error: Division by zero is not allowed.")
      return 0.0
   
   except TypeError as e: # This is used to catch the specific error of type mismatch and handle it gracefully
      print("Error: inout must be a number.")
      print(f"Details: {e}")
      return 0.0
   
   except Exception as e: # This is used to catch any other exceptions that may occur and handle them gracefully
      print(f"An unexpected error occured: {e}")
      return 0.0
   
   else: # This is used to execute code that should run if no exceptions were raised in the try block.
      print("Division successful.")
      return result
   
   finally: # This is used to execute code that should run regardless of the outcome of the try block
      print("Execution of divide_number function is complete.")
# Types of exceptions include: ValueError, IndexError, KeyError, FileNotFoundError, TypeError, ZeroDivisionError, Exception, etc.

# Throwing an exception
def check_positive(num: int) -> None:
   if num < 0:
      raise ValueError("Input must be a positive number.")
   elif num == 0:
      raise ValueError("Input must be a non-zero positive number.")
   elif num > 100:
      raise Exception("Input must be less than or equal to 100.")
   else:
      print(f"Input is valid: {num}")

# check_positive(-1) # Output Error: ValueError: Input must be a positive number.
check_positive(10) # Output: Input is valid: 10
