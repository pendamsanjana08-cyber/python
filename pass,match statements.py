# Write an if statement with no action using pass.

num = 10
if num > 5:
    pass  # placeholder, no action
else:
    print("Small number")


# Skip implementation inside a loop.

for i in range(5):
    pass   # loop runs but does nothing


# Create a function with no body.

def my_function():
    pass


# Print day name using match.

day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid")



# Perform operation using match.

a, b = 10, 5
op = "+"
match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid")


# Handle multiple values in one case.

num = 2
match num:
    case 1 | 2 | 3:
        print("Small number")
    case _:
        print("Large number")


# Explain default case in match.

x = 100

match x:
    case 10:
        print("Ten")
    case _:
        print("Default case")



# Check even or odd using match.

num = 8
match num:
    case x if x % 2 == 0:
        print("Even")
    case _:
        print("Odd")


# Create empty class.

class MyClass:
    pass


# Use pass inside match.

x = 1

match x:
    case 1:
        pass   # no action
    case 2:
        print("Two")
    case _:
        print("Other")