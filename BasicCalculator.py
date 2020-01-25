""" BasicCalculator.py, by Jonathan Burgess, 2020-Jan-14
This is a calculator program. It is a practice project 
and will be updated as I gain more experience in Python. """

# Collect input from user and assign to a variable
num1 = float(input("Enter a number: "))
oper = input("Enter your operator (+, -, *, or /): ")
num2 = float(input("Enter another number: "))

# Use if loop to confirm valid operators
if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print (num1 - num2)
elif oper == "*":
    print (num1 * num2)
elif oper == "/":
    print (num1 / num2)
else:
    print("Error")
    