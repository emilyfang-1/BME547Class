# calculator.py

def add(x, y):
    z = x + y
    symbol = "+"
    return z, symbol

def sub(x, y):
    z = x - y
    symbol = "-"
    return z, symbol

def multiply(x, y):
    z = x * y
    symbol = "*"
    return z, symbol

def divide(x, y):
    z = x / y
    symbol = "/"
    return z, symbol
    
x = input("Enter a letter: ")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num1 = float(num1)
num2 = float(num2)

if x == "a":
    z, sym = add(num1, num2)
    print("{} {} {} = {}".format(num1, sym, num2, z))  
elif x == "s":
    z, sym = sub(num1, num2)
    print("{} {} {} = {}".format(num1, sym, num2, z))
elif x == "m":
    z,sym = multiply(num1, num2)
    print("{} {} {} = {}".format(num1, sym, num2, z))
elif x == "d":
    z, sym = divide(num1, num2)
    print("{} {} {} = {}".format(num1, sym, num2, z))
else:
    print("The {} command is not recognized".format(x))

print("Done")
