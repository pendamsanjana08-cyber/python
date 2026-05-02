# Display Student Details Using f-string

name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")


# Calculate and Display Total Bill

item = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print(f"You bought {quantity} {item}(s)")
print(f"Total bill amount is ₹{total}")


# Display Square and Cube of a Number

num = int(input("Enter a number: "))
print(f"Square of {num} is {num ** 2}")
print(f"Cube of {num} is {num ** 3}")


# Format Decimal Values Using f-string

pi = 3.1415926535
print(f"Pi value rounded to 2 decimals: {pi:.2f}")
print(f"Pi value rounded to 4 decimals: {pi:.4f}")


# Create Username Using f-string

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
username = f"{first_name.lower()}.{last_name.lower()}"
print(f"Generated Username: {username}")