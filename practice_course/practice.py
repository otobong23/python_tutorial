

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

# print(factorial_function(5))


# Linear search
def search(param_list: list[int], search_for: int) -> tuple[bool, int | None]: # for ordered or unordered list
   i = 0
   variable_position = -1
   while i < len(param_list):
      if param_list[i] == search_for:
         variable_position = i
         return (True, variable_position + 1)
      i = i + 1
   return (False, None)

# is_it_available, position = search([13, 43, 12, 44, 1, 3], 44)
# print(is_it_available, position)


# Binary Search
def binary_search(param_list: list[int], search_for: int) -> tuple[bool, int | None]: # for order list
   lower_band = 0
   upper_band = len(param_list)
   variable_position = -1

   while lower_band <= upper_band:
      mean_value = (lower_band + upper_band) // 2
      if param_list[mean_value] == search_for:
         variable_position = mean_value
         return (True, variable_position + 1)
      else:
         if param_list[mean_value] < search_for:
            lower_band = mean_value + 1
         else:
            upper_band = mean_value - 1
   return (False, None)

# is_it_available, position = search([1, 3, 12, 13, 43, 44], 44)
# print(is_it_available, position)




# Bubble Sorting
def Sort_list(nums: list[int]) -> None:
   for i in range(len(nums) -1, 0, -1):
      for j in range(i):
         if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp

# unordered_list = [13, 43, 12, 44, 1, 3]
# Sort_list(unordered_list)
# print(unordered_list)

# Selection Sorting
def Selection_sort(nums: list[int]) -> None:
   for i in range(len(nums) -1):
      main_position = i

      for j in range(i, len(nums)):
         if nums[j] < nums[main_position]:
            main_position = j

      temp = nums[i]
      nums[i] = nums[main_position]
      nums[main_position] = temp

# unordered_list = [13, 43, 12, 44, 1, 3]
# Selection_sort(unordered_list)
# print(unordered_list)