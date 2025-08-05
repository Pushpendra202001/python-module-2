# Task 1: Perform Basic Mathematical Operations
# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
# o	Addition
# o	Subtraction
# o	Multiplication
# o	Division
# 3.  Displays the results of each operation on the screen.
num1 = input(   "Enter the first number: ")
num2 = input( "Enter the second number: ")
try:
    num1 = int(num1)
    num2 = int(num2)
    print("Addition: ", num1 + num2)
    print("Subtraction: ", num1 - num2)
    print("Multiplication: ", num1 * num2)
    print("Division: ", num1 / num2)
except (ValueError, ZeroDivisionError) as e:
    print(e)
    print("please enter a integer number or second number should be greater than 0")

