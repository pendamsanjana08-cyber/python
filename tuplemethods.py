#Count how many times 10 appears in a tuple.

m = (10, 20, 10, 30, 10)
print(m.count(10))   # 3

#Find index of element 30.

l= (10, 20, 30, 40)
print(l.index(30))   # 2

#What happens if element appears multiple times?

b = (1, 2, 3, 2, 4)
print(b.index(2))   # 1 (first occurrence only)

#What happens if element is not present?

p= (1, 2, 3)
if 5 in p:
    print(p.index(5))
else:
    print("Not found")

#Check if element appears more than once.

f = (1, 2, 2, 3)

if f.count(2) > 1:
    print("Repeated")
v = (1, 2, 2, 3, 3, 3)
for i in v:
    print(i, ":", v.count(i))

#Find all positions of element 2.
b= (1, 2, 3, 2, 4)
positions = []
for i in range(len(b)):
    if b[i] == 2:
        positions.append(i)
print(positions)

#Find element with highest frequency.

c= (1, 2, 2, 3, 3, 3)
max_count = 0
max_elem = None
for i in c:
    if c.count(i) > max_count:
        max_count = c.count(i)
        max_elem = i
print(max_elem)

#Check if tuple has no duplicates.

f= (1, 2, 3, 4)
unique = True
for i in f:
    if f.count(i) > 1:
        unique = False
print(unique)

#Find index of element and print elements after it.

d = (10, 20, 30, 40, 50)
i = d.index(30)
print(d[i+1:])   # (40, 50)