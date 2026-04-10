#Create a set of 5 numbers and print it.
s = {1, 2, 3, 4, 5}
print(s)

#Add element 6 to the set.
M= {7, 4, 5}
M.add(6)
print(M)

#Remove element 2 from the set.
d = {1, 2, 3}
d.remove(2)
print(d)

#Remove element 5 safely (even if not present).
c = {12, 23, 34}
c.discard(5)
print(c)

#Find union of two sets.
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

#Find common elements.
s= {11, 22, 33}
o = {22, 33, 44}
print(s.intersection(o))

#Elements in b but not in p.
b = {1, 2, 3}
p = {2, 3, 4}
print(b.difference(p))

#Check if a is subset of b.
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))

#Remove duplicates.
lst = [1, 2, 2, 3, 4, 4]
unique = set(lst)
print(unique)

#Print all elements.
s = {10, 20, 30}
for i in s:
    print(i)