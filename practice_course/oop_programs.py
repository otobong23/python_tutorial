
# Classes, Objects, Instance Variables, Class Variables, Class Methods, Static Methods, Instance Methods

class School:
   def __init__(self):
      self.school = "Greenwood High"
      self.location = "New York"
   
   def display_school_info(self):
      print(f"Name: {self.school}, Location: {self.location}")



class Person (School):
   def __init__(self, name: str, age: int, level: int) -> None:
      super().__init__()  # calling the constructor of the parent class School to initialize the inherited attributes
      self.name = name     # instance variable
      self.age = age       # instance variable
      self.level = level   # instance variable

   def display_person_info(self):
      print(f"Name: {self.name}, Age: {self.age}, Level: {self.level}")

person1 = Person("John", 25, 3)
person1.display_school_info()
person1.display_person_info()



class Computer:
   def __init__ (self, brand: str, model: str, year: int):  # constructor method
      self.brand = brand   # instance variable
      self.model = model   # instance variable
      self.year = year     # instance variable
      self.owner = Person("Alice", 30, 5)  # instance method
   

   def display_computer_info(self): # instance method that accesses instance variables
      print(f"Computer: {self.year} {self.brand} {self.model}")
   
   ram = 16 # class variable
   storage = 512  # class variable

   @classmethod
   def display_ram(cls):  # class method that accesses class variables - cls is a preserved keyword that takes the class as an argument and is used to access class variables and other class methods within the class methods
      print(f"ram: {cls.ram}GB, storage: {cls.storage}GB")
   
   @staticmethod
   def more_info():
      print("This is a computer class with attributes and methods. this is a static method that does not access instance or class variables.")


my_computer = Computer("Dell", "XPS 15", 2021)
Computer.ram = 32 # Modifying the class variable ram for all instances of Computer
my_computer.display_ram()  # Output: ram: 32GB, storage: 512GB

my_computer.ram = 16 # 
my_computer.display_computer_info() # Output: Computer: 2021 Dell XPS 15
my_computer.display_ram()  # Output: ram: 16GB, storage: 512GB

my_computer.owner.display_person_info() # Output: Name: Alice, Age: 30, Level: 5
my_computer.more_info() # Output: This is a computer class with attributes and methods. this is a static method that does not access instance or class variables.
Computer.more_info() # Output: This is a computer class with attributes and methods. this is a static method that does not access instance or class variables.






# Extending and Inheritance

# a class without initialization method
class Details:
   def more_details(self):
      print("This is a class without an initialization method, it can be used as a parent class for inheritance.")


class Laptop (Details, Computer): # Laptop class inherits from Computer class -  The paranthesis can take multiple parent classes for multiple inheritance
   def __init__(self, brand: str, model: str, year: int, battery_life: int): # constructor method for Laptop class that takes additional parameter battery life after including the parameters of the Computer class, the School class dosen't have any parameters in its constructor
      super().__init__(brand, model, year)     # calling the constructor of the parent class Computer to initialize the inherited attributes, the super() method only initializes the first parent class that has an initialization method.
      self.battery_life = battery_life        # instance variable specific to Laptop class

my_laptop = Laptop("Apple", "MacBook Pro", 2022, 10)
my_laptop.display_computer_info() # Output: Computer: 2022 Apple MacBook Pro
my_laptop.more_details() # Output: This is a class without an initialization method, it can be used as a parent class for inheritance.





# Polymorphism

# 1. Duck Typing Polymorphism
# In duck typing, the type or class of an object is less important than the methods it defines. If an object has the necessary methods, it can be used in place of another object, regardless of its actual type.


# 2. Operator Overloading Polymorphism
value_a = 5
value_b = 10
print('sum of value_a and value_b is:', value_a + value_b, 'is this same as value_a.__add__(value_b) -> ', value_a.__add__(value_b)) # Output: sum of value_a and value_b is: 15 is this same as value_a.__add__(value_b) ->  15
print('it is also the same as int.__add__(value_a, value_b) -> ', int.__add__(value_a, value_b)) # Output: it is also the same as int.__add__(value_a, value_b) ->  15
# other operators that can be overloaded include: -, *, /, //, %, **, <, >, etc. and they have their corresponding special methods like __sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__, __lt__, __gt__ etc.
# the overloaded operators can be used on custom classes, values, and built-in types as well.

class Vector:
   def __init__(self, x: int, y: int):
      self.x = x
      self.y = y

   def __add__(self, other: 'Vector') -> 'Vector': # operator overloading for the + operator
      return Vector(self.x + other.x, self.y + other.y)

   def __str__(self) -> str: # operator overloading for the str() function to return a string representation of the Vector object
      return f"Vector: ({self.x}, {self.y})"

   def display_vector(self) -> None:
      print(f"Vector: ({self.x}, {self.y})")

vector1: Vector = Vector(2, 3)
vector2: Vector = Vector(4, 5)
vector3: Vector = vector1 + vector2 # using the overloaded + operator to add two Vector Objects
vector3.display_vector() # Output: Vector: (6, 8)
print(vector2) # Output: Vector: (4, 5) - this is using the overloaded __str__ method to get a string representation of the Vector object instead of the default memory address representation.


# 3. Method Overloading and Method Overriding Polymorphism

# overloading
def calculate (a: int = 0, b: int = 0, c: int = 0): # method overloading by using default parameters to allow for different numbers of arguments
   return a + b + c
print(calculate(5, 10)) # Output: 15 - this is using the method with two arguments, by default c is 0

# overriding
class Animal:
   def make_sound(self) -> None:
      print("Animal makes a sound")

class Dog(Animal):
   def make_sound(self) -> None:
      print("Dog barks")

my_dog = Dog()
my_dog.make_sound() # output: Dog barks - this is using the overridden method in the Dog class instead of the method in the Animal class.



# Abstract classes and Abstract Methods
from abc import ABC, abstractmethod

class Shape(ABC): # Abstract class that cannot be instantiated and can contain abstract methods that must be implemented by any subclass that inherits from it.
   @abstractmethod
   def area(self) -> float:
      pass

class Circle(Shape):
   def area(self) -> float:
      radius = 5
      return 3.14 * radius ** 2
   

# Synchronous and Asynchronous Programming
import asyncio

class AsyncFunctions:
   async def details(self):
      print('async details')
   
   async def more_details(self):
      await self.details() # awaiting the details method to complete before executing the next line of code
      print('more async details')

   async def run_functions(self):
      # A synchronous way to run the asynchronous function
      await  self.more_details() # running the asynchronous function more_details with await because you can't call asyncio.run() inside another asyncio.run() or an already running event loop, so we use await instead
      # Inside async functions → only use await, Never mix asyncio.run() and await incorrectly

      # An asynchronous way to wait for the asynchronous function to be completed before running the callback function
      async def fetch_details (a: int, b: int) -> int:
         await asyncio.sleep(1)
         return a + b
      
      task = asyncio.create_task(fetch_details(5, 10)) # creating an asynchronous task
      task.add_done_callback(lambda task_response: print(f"Task result: {task_response.result()}")) # adding a callback to the task to print the result when the task is done
      await task  # ✅ ensure it runs

async def task1():
   await asyncio.sleep(1) # SetTimeout for 1 second or delay of 1 second to simulate an asynchronous operation
   return "Task 1"

async def task2():
   await asyncio.sleep(2) # SetTimeout for 2 seconds or delay of 2 seconds to simulate an asynchronous operation
   return "Task 2"

async def main_async():
   results = await asyncio.gather(task1(), task2())
   print(results)

async_functions = AsyncFunctions()
asyncio.run(async_functions.run_functions())
asyncio.run(async_functions.more_details())
asyncio.run(main_async())






# Threading and Multiprocessing
from threading import  *
from time import sleep

class HelloThread(Thread):
   def run(self):
      for i in range(5):
         print('Hello from Thread 1')
         sleep(1)

class HiThread(Thread):
   def run(self):
      for i in range(5):
         print('Hi from Thread 2')
         sleep(1)

hello = HelloThread()
hi = HiThread()

hello.start() # Starting the first thread to run the run method of HelloThread class
sleep(0.2) # Collision Avoidance: Adding a small delay to allow the first thread to start before starting the second thread, this is not necessary but it can help to see the interleaving of the two threads' outputs more clearly.
hi.start() # Starting the second thread to run the run method of HiThread class

print('Displaying this print after hello thread and hi thread first execution, before continuing with their next execution')

hello.join() # Waiting for the first thread to finish before proceeding with the main thread
hi.join() # Waiting for the second thread to finish before proceeding with the main thread

print("Both threads have finished execution")