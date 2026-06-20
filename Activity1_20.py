def add(a,b):
    return(a+b)

def minus(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)

try:
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a second number: "))
    operation = int(input("Enter an operation(Multiply, Divide, Add, Subtract): "))
except ValueError:
    print("That is not a number or operation")
except ZeroDivisionError:
    print("I cannot divide by zero!")

if operation == "Multiply":
    print(multiply(number1, number2))
elif operation == "Divide":
    print(divide(number1, number2))
elif operation == "Add":
    print(add(number1, number2))
elif operation == "Subtract":
    print(minus(number1, number2))
