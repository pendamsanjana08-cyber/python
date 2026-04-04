#1.Write a program to remove duplicates from a list without using set().
list = [1, 2, 2, 3, 4, 3, 5]
result = []

for i in list:
    if i not in result:
        result.append(i)

print(result)

#2.Find the second largest number in a list.
d = [10, 20, 4, 45, 99]
d.sort()
print(d[-2])

#3.Count how many times each element appears.

ab= [1, 2, 2, 3, 3, 3]
freq = {}

for i in ab:
    freq[i] = freq.get(i, 0) + 1

print(freq)

#4.Reverse a list manually.
mylist = [1, 2, 3, 4]
rev = []

for i in mylist:
    rev = [i] + rev

print(rev)

#5.3Find common elements in two lists.

m = [1, 2, 3, 4]
n = [3, 4, 5, 6]

common = []

for i in m:
    if i in n:
        common.append(i)

print(common)

#6.Rotate a list to the right by 1 position.

j = [1, 2, 3, 4]
k = [j[-1]] + j[:-1]

print(k)

#7.convert nested list into a single list.

list1 = [[1, 2], [3, 4], [5]]
flat = []

for sub in list1:
    for i in sub:
        flat.append(i)

print(flat)

#8.Find missing number from 1 to n.
o= [1, 2, 4, 5]
n = 5

for i in range(1, n+1):
    if i not in o:
        print(i)

#9.create two lists: one for even and one for odd numbers.
s= [1, 2, 3, 4, 5, 6]

even = []
odd = []

for i in s:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even:", even)
print("Odd:", odd)