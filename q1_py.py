
"""Q1.py
# **Functions**


1.   Even-Odd number
"""
# Test cases:
# Test Case 1: Test with an even number
# Expected Output: "156 is even"
# Test Case 2: Test with an odd number
# Expected Output: "7 is odd"
# Test Case 3: Test with zero
# Expected Output: "0 is even"
# Test Case 4: Test with a negative odd number
# Expected Output: "-9 is odd"
# Test Case 5: Test with a negative even number
# Expected Output: "-22 is even"

def even_odd_number(x):
  if x % 2 == 0:
    return(f'{x} is an even number.')
  else:
    return(f'{x} is an odd number.')

result = even_odd_number(2)
print(result)
result = even_odd_number(5)
print(result)

"""

2. Min & Max number in a List

"""

# Function: max_num()
# Test cases:
# Test Case 1: Test with positive numbers
# Expected Output: 500
# Test Case 2: Test with negative numbers
# Expected Output: -4
# Test Case 3: Test with a mixture of positive and negative numbers
# Expected Output: 200
# Test Case 4: Test with a list containing only one element
# Expected Output: 100
# Test Case 5: Test with an empty list
# Expected Output: None

def max_number(List):
  temp_max = List[0]
  for i in  range(len(List)-1):
    if temp_max < List[i]:
      temp_max=List[i]
  return temp_max


# Function: min_num()
# Test cases:
# Test Case 1: Test with positive numbers
# Expected Output: 0
# Test Case 2: Test with negative numbers
# Expected Output: -4
# Test Case 3: Test with a mixture of positive and negative numbers
# Expected Output: -4
# Test Case 4: Test with a list containing only one element
# Expected Output: 100
# Test Case 5: Test with an empty list
# Expected Output: None

def min_number(List):
  temp_min = List[0]
  for i in  range(len(List)-1):
    if temp_min > List[i]:
      temp_min=List[i]
  return temp_min

List = [19, 33, 100, 50, 105, 23]
result = min_number(List)
print(result)

"""3. Table of any number
"""
# No specific test cases provided. The function takes user input.

def table(x):
  for i in range(1,11):
    print (x * i)

table(9)


"""4. Factorial of a number"""
# def test_factorial_positive_integers():
 # assert factorial(5) == 120, "Test failed: factorial(5) should be 120"
# assert factorial(1) == 1, "Test failed: factorial(1) should be 1"


def factorial(num):
  if num < 0:
    print("Factorial of negative number  doesn't exist")
  elif num == 0 :
   return 1
  else:
    factorial = 1
    for i in range(num,1,-1):
      factorial *= i
    return factorial

factorial(1)

# Recursive logic
def fac(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n*fac(n-1)

fac(6)



"""5. Sum of a List"""
# def test_sum_multiple_integers():
# assert sum([1, 2, 3, 4, 5]) == 15, "The sum of the list [1, 2, 3, 4, 5] should be 15."


def sum(List):
  sum = 0
  for i in List:
    sum += i
  return sum

t = [100,200,300,400]
sum(t)

"""6.  Generating acsending and decending numbers sequence using loop"""

starting = int(input("Enter Starting no. "))
ending =int(input("Enter Ending no."))

def ascending_seq():
  for i in range(starting, ending, 1):
    print (i)

ascending_seq()

def descending_seq():
  for i in range(starting,ending, -1):
    print(i)

descending_seq()

"""7.  Calculating area of a circle"""

import math
def area_of_circle(radius):
  return (math.pi * pow(radius,2))

area_of_circle(5)

"""8. Convert Celsius to Fahrenheit and vice versa"""

def celsius(f):
  return ((f-32)*5)/9

def farenhite(c):
  return ((9*c)/5)+32

result = farenhite(12)
print(result)

"""9. Sum of the first n positive integers"""

def sum_of_integers(n):
  return (n*(n+1))/2

result = sum_of_integers(6)
print(result)

"""10. Linear Search"""

# Test cases:
# Test Case 1: Test with a number present in the list
# Expected Output: 7
# Test Case 2: Test with a number not present in the list
# Expected Output: -1
# Test Case 3: Test with the first element of the list
# Expected Output: 0
# Test Case 4: Test with the last element of the list
# Expected Output: 7
# Test Case 5: Test with an empty list
# Expected Output: -1

def linear_search(list,k):
  for i in range(len(list)):
    if list[i] == k:
      return i
List = [1,2,3,4,5]
result = linear_search(List,5)
print(result)