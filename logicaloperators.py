# Check if a number is between 10 and 50.

num = 25
if num >= 10 and num <= 50:
    print("In range")
else:
    print("Out of range")


# Check if a number is divisible by both 3 and 5.

num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
else:
    print("Not divisible")


# Check if number is divisible by 3 or 5.

num = 10
if num % 3 == 0 or num % 5 == 0:
    print("Divisible by 3 or 5")
else:
    print("Not divisible")


# Check if a number is NOT even.

num = 7
if not (num % 2 == 0):
    print("Odd number")
else:
    print("Even number")


# Check username and password.

user = "admin"
password = "1234"
if user == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


# Check if person is eligible (age >=18 and citizen).

age = 20
citizen = True
if age >= 18 and citizen:
    print("Eligible")
else:
    print("Not eligible")


# Check if student passed with good marks.

marks = 70
attendance = 80
if marks >= 50 and attendance >= 75:
    print("Pass")
else:
    print("Fail")


# Check if number is between 1–10 or 50–60.

num = 55
if (num >= 1 and num <= 10) or (num >= 50 and num <= 60):
    print("Valid range")
else:
    print("Invalid")

# Check if character is alphabet or digit.

ch = 'A'
if ch.isalpha() or ch.isdigit():
    print("Valid input")
else:
    print("Special character")


# Check if password length >=8 and contains digit.

password = "abc12345"
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Strong password")
else:
    print("Weak password")