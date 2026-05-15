#1. Swap Two Numbers Without Using Third Variable

a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)

#2. Find Largest Element in a List

numbers = [12, 45, 7, 89, 34]
largest = max(numbers)
print("Largest number:", largest)


#3. Count Digits in a Number

num = int(input("Enter a number: "))
count = len(str(num))
print("Number of digits:", count)

#4. Find Sum of Even Numbers from 1 to N

n = int(input("Enter value of n: "))
total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total += i
print("Sum of even numbers:", total)
