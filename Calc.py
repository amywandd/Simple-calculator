# Amy Njeri Wanderi - sct211-0010/2021
class Calculator:
    def __init__(self):
        pass
    def add(self, x, y):
        return print(f"Sum of {x} and {y} = {x + y}")
    def subtract(self, x, y):
        return print(f"Subtraction of {x} and {y} = {x - y}")
    def multiply(self, x, y):
        return print(f"Multiplication of {x} and {y} = {x * y}")
    def division(self, x, y):
        return print(f"Division of {x} and {y} = {x / y}")
calculator1 = calculator()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("____________Enter operation____________\n Enter(1,2,3 or 4)\n1.Adition\n2.Subtraction\n3.Multiplication\n4.Division.\n**************\n")
if operation == "1":
    calculator1.add(num1, num2)
elif operation == "2":
    calculator1.subtract(num1, num2)
elif operation == "3":
    calculator1.multiply(num1, num2)
else:
    calculator1.divide(num1, num2)
