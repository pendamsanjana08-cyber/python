# A nested if is an if statement inside another if statement.
x = 10
if x > 5:
    if x < 20:
        print("x is between 5 and 20")



# Check if a number is positive and even
num = 8
if num > 0:
    if num % 2 == 0:
        print("Positive and Even")


# Check if a person is eligible to vote and has an ID
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Eligible to vote")


# Find the greatest of two numbers using nested if
a = 10
b = 20

if a > b:
    print("a is greater")
else:
    if b > a:
        print("b is greater")


# Check if a number is divisible by 2 and 3
num = 12

if num % 2 == 0:
    if num % 3 == 0:
        print("Divisible by both 2 and 3")



# Check login credentials
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")



# Check grade and distinction
marks = 85

if marks >= 50:
    if marks >= 75:
        print("Passed with distinction")


# Check if number is in range and odd
num = 15

if num > 10:
    if num % 2 != 0:
        print("Number is greater than 10 and odd")


# Check temperature conditions
temp = 30

if temp > 20:
    if temp < 35:
        print("Weather is pleasant")


# Check password length and special character
password = "abc@123"

if len(password) >= 6:
    if "@" in password:
        print("Strong password")