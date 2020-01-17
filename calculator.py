# calculator.py

def add(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    print("{} - {} = {}".format(x, y, z))

def multiply(x, y):
    z = x * y
    print("{} * {} = {}".format(x, y, z))

def divide(x, y):
    z = x / y
    
    
x = input("Enter a letter: ")
print("You entered {}".format(x))
if x == "a":
    z = add(47,7)
    print("{} + {} = {}".format(47, 7, z))
elif x == "s":
    sub(47, 7)
elif x == "m":
    multiply(47, 7)
elif x == "d":
    divide(47, 4)
else:
    print("The {} command is not recognized".format(x))
print("Done")
