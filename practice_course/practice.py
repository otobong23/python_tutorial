

def prime_numbers_up_to(num: int) -> None:
   for n in range(1, num):
      for i in range(2, n):
         if n % i == 0:
            break
      else:
         print(n, end=" ")

def count_numbers(number_list: list) -> tuple[int, int]:
   even = 0
   odd = 0
   for i in number_list:
      if i % 2 :
         odd+=1
      else:
         even+=1
   return even, odd

even, odd = count_numbers(list(range(1, 101)))
# print("Even numbers count: {}, Odd numbers count: {}".format(even, odd))

def fibonacci_function(n: int) -> list[int]:
   a, b = 0, 1
   fib_sequence = []
   for i in range(n):
      fib_sequence.append(a)
      a, b = b, a + b
   return fib_sequence

def factorial_function(n: int) -> int:
   if n == 0 or n == 1:
      return 1
   else:
      return n * factorial_function(n - 1) # Recursive call to calculate the factorial of n

print(factorial_function(5))