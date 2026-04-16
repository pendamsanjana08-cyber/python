# Assign grades based on marks.

marks = 72
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

# Check if number is positive, negative, or zero.

num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



# Find the largest number.

a, b, c = 10, 25, 15
if a > b and a > c:
    print("a is largest")
elif b > c:
    print("b is largest")
else:
    print("c is largest")


# Identify character type.

ch = '5'

if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

# Perform operation based on user choice.

a, b = 10, 5
choice = 2

if choice == 1:
    print(a + b)
elif choice == 2:
    print(a - b)
elif choice == 3:
    print(a * b)
elif choice == 4:
    print(a / b)
else:
    print("Invalid choice")



# Classify age group.

age = 45
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior")


# Check divisible by 2, 3, or both.

num = 6
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both")
elif num % 2 == 0:
    print("Divisible by 2")
elif num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible")

# Display weather condition.

temp = 30
if temp < 15:
    print("Cold")
elif temp < 25:
    print("Warm")
else:
    print("Hot")


# Print day based on number.

day = 3
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Invalid")

#Calculate bill based on units.

units = 150

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Bill:", bill)

