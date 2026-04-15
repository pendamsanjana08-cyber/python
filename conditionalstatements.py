# Write a program to check whether a number is positive or negative.

num = -5
if num >= 0:
    print("Positive")
else:
    print("Negative")

#Check if a number is even or odd.

num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Find the larger number.

a = 10
b = 20
if a > b:
    print("a is larger")
else:
    print("b is larger")

#Find the largest among three numbers.

a = 5
b = 15
c = 10
if a > b and a > c:
    print("a is largest")
elif b > c:
    print("b is largest")
else:
    print("c is largest")

# Check divisibility.

num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")

#Assign grade based on marks.

marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#Check whether a year is leap year.

year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# Check if character is vowel or consonant.

ch = 'a'
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#Perform basic operations.

a = 10
b = 5
op = "+"
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")

# Check if person is eligible to vote.

age = 17
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")