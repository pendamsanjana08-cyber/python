# Write a program to check whether a number is an Armstrong number or not.

num = int(input("Enter a number: "))
power = len(str(num))
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10
if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# Print all prime numbers between two numbers.

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


# Count uppercase and lowercase characters in a string.

text = input("Enter a string: ")
upper = 0
lower = 0
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)