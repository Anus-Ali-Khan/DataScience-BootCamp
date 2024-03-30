
# **Calculator**


while True:
  try:
    num1 = int(input("Enter any number:"))
    num2 = int(input("Enter second number:"))
    operation = input("Enter airthmetic operator:")
    if operation.lower() == 'sum' or operation == '+':
      print(num1 + num2)
    elif operation.lower() == 'subtract' or operation == '-':
      print(num1 - num2)
    elif operation.lower() == 'multiply' or operation == '*':
      print (num1 * num2)
    elif operation.lower() == 'divide' or operation == '/' :
      print(num1 / num2)
    elif operation.lower() == 'exit' :
      print("Exit")
      break
  except ValueError:
    print('Invalid Input')
  except Exception as ZeroDivisionError:
    print("Cannot divide by zero")

# Function: calculator()
# Test cases:
# Test Case 1: Test addition operation
# Input: 1, 5, 7
# Expected Output: "Result: 5 + 7 = 12"
# Test Case 2: Test subtraction operation
# Input: 2, 10, 3
# Expected Output: "Result: 10 - 3 = 7"
# Test Case 3: Test multiplication operation
# Input: 3, 6, 8
# Expected Output: "Result: 6 * 8 = 48"
# Test Case 4: Test division operation
# Input: 4, 20, 4
# Expected Output: "Result: 20 / 4 = 5.0"
# Test Case 5: Test division by zero
# Input: 4, 10, 0
# Expected Output: "Cannot divide by zero"
# Test Case 6: Test invalid input (non-integer choice)
# Input: "abc"
# Expected Output: "Invalid Input"
# Test Case 7: Test invalid input (non-integer numbers)
# Input: 1, "abc", 5
# Expected Output: "Invalid Input"
# Test Case 8: Test exit operation
# Input: 5
# Expected Output: Program exits