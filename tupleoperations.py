#Access the 3rd element from the tuple.
t = (10, 20, 30, 40)
print(t[2])

#Print the last element of a tuple.
p = (5, 10, 15)
print(p[-1])

#Print elements from index 1 to 3.
s = (1, 2, 3, 4, 5)
print(s[1:4])

#Join two tuples.
m1 = (1, 2)
m2 = (3, 4)
m3 = m1 + m2
print(m3)

#Repeat a tuple 3 times.
n = (1, 2)
print(n * 3)

#Check if 10 exists in tuple.
v = (5, 10, 15)
print(10 in v)

#Count how many times 2 appears.
f = (1, 2, 2, 3, 2)
print(f.count(2))

#Find index of element 30.
c = (10, 20, 30, 40)
print(c.index(30))

#Convert tuple into list.
b = (1, 2, 3)
l = list(b)
print(l)

#Unpack tuple into variables.

o = (10, 20, 30)
a, b, c = o

print(a)
print(b)
print(c)