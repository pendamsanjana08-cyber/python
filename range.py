#1 Print numbers from 10 to 1 using range
for i in range(10, 0, -1):
    print(i, end=" ")


#2. Print all even numbers between 1 and 50
for i in range(2, 51, 2):
    print(i, end=" ")


#3. Find sum of numbers from 1 to n using range
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_n(5))  


# 4. Print multiplication table of a number
n = 5
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# 5. Count how many numbers are divisible by 3 between 1 and 100
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print(count)


#6. Create a list of squares from 1 to 10 using range
squares = [i**2 for i in range(1, 11)]
print(squares)


#7. Print characters of a string using range and indexing
s = "Python"
for i in range(len(s)):
    print(s[i])


# 8. Reverse a list using range
lst = [1, 2, 3, 4, 5]
for i in range(len(lst) - 1, -1, -1):
    print(lst[i], end=" ")


# 9. Find factorial using range (iterative)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5)) 


#10. Print numbers skipping multiples of 5
for i in range(1, 31):
    if i % 5 == 0:
        continue
    print(i, end=" ")