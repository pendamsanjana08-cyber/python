# write a Python program to take the user's name as input and print a welcome message.
name = input("Enter your name: ")
print("Welcome,", name)

# Write a program to take two numbers from the user and print their sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

# Write a program to find the area of a rectangle using user input.

length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle =", area)


# Write a Python program to check whether a number entered by the user is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:    
    print("Even number")
else:   
     print("Odd number")


# Write a program to take the user's age and check if they are eligible to vote.

age = int(input("Enter your age: "))
if age >= 18:   
    print("Eligible to vote")
else:    
    print("Not eligible to vote")


# Write a Python program to swap two numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping:")
print("a =", a)
print("b =", b)
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)


# Write a Python program to take a number from the user and print its multiplication table.

num = int(input("Enter a number: "))
for i in range(1, 11):   
    print(num, "x", i, "=", num * i)


# Write a program to take marks from the user and display the grade.

marks = int(input("Enter marks: "))
if marks >= 90:    
    print("Grade A")
elif marks >= 75:    
    print("Grade B")
elif marks >= 50:    
    print("Grade C")
else:    
    print("Fail")


# Write a Python program to calculate the average of three numbers entered by the user.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
average = (a + b + c) / 3
print("Average =", average)