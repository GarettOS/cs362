def addition(a, b):
   total = a + b
   return total

def subtraction(a, b):
   total = a - b
   return total

def multiplication(a, b):
   total = a * b
   return total

def division(a, b):
   # Logic
   total = a / b
   return total

a = input("Input number: ")
b = input("Input another number: ")
a = float(a)
b = float(b)
additionTotal = addition(a, b)
subtractionTotal = subtraction(a, b)
multiplyTotal = multiplication(a, b)
divisionTotal = division(a, b)

print("The addition of those 2 numbers are: ", additionTotal)
print("The subtraction of those 2 numbers are: ", subtractionTotal)
print("The multiplication of those 2 numbers are: ", multiplyTotal)
print("The division of those 2 numbers are: ", divisionTotal)

