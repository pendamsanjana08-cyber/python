#Print each element of a list.

lst = [10, 20, 30, 40]

for i in lst:
    print(i)


#Find the sum of all elements in a list.

lst = [1, 2, 3, 4]
total = 0

for i in lst:
    total += i

print(total)

#Find the largest number in a list.

lst = [10, 5, 20, 8]
max_val = lst[0]

for i in lst:
    if i > max_val:
        max_val = i

print(max_val)

#Count how many even numbers are in a list.

lst = [1, 2, 3, 4, 6]
count = 0

for i in lst:
    if i % 2 == 0:
        count += 1

print(count)

#Create a new list with squares of elements.

lst = [1, 2, 3, 4]
squares = []

for i in lst:
    squares.append(i * i)

print(squares)

#Reverse a list using loop.
lst = [1, 2, 3, 4]
rev = []

for i in lst:
    rev = [i] + rev

print(rev)

#Find common elements between two lists.

a = [1, 2, 3]
b = [2, 3, 4]

common = []

for i in a:
    if i in b:
        common.append(i)

print(common)

#Remove duplicates from list.
lst = [1, 2, 2, 3, 4, 3]
unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print(unique)

#count frequency of each element.

lst = [1, 2, 2, 3, 3, 3]
freq = {}

for i in lst:
    freq[i] = freq.get(i, 0) + 1

print(freq)

#Separate even and odd numbers into two lists.

lst = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)