#Add element 50 to a set.
s = {10, 20, 30}
s.add(50)
print(s)

#Add multiple elements to a set.
m = {1, 2}
m.update([3, 4, 5])
print(m)

#Remove element 20 from set.
s1 = {10, 20, 30}
s1.remove(20)
print(s1)

#Remove element without error if not present.
l = {1, 2, 3}
l.discard(5)   # No error
print(l)

#Remove a random element.
o = {10, 20, 30}
a = o.pop()
print("Removed:", o)
print(a)

#Find union of two sets.
s = {1, 2, 3}
n = {3, 4, 5}
print(s.union(n))

#Find common elements.
b = {1, 2, 3}
d = {2, 3, 4}
print(b.intersection(d))

#Find elements in A but not in B.
f = {1, 2, 3}
x = {2, 3, 4}
print(f.difference(x))

#Check if one set is subset of another.
h = {1, 2}
k = {1, 2, 3}
print(h.issubset(k))   # True

#Remove all elements from set.
p= {1, 2, 3}
p.clear()
print(p)   # set()