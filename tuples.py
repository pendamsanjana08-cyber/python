
#Create a tuple and print the first and last element.

t = (10, 20, 30, 40)
print("First:", t[0])
print("Last:", t[-1])

#Print elements from index 1 to 3.

t = (10, 20, 30, 40, 50)
print(t[1:4])   # (20, 30, 40)

#Count how many times 5 appears

t = (5, 1, 5, 2, 5)
print(t.count(5))   # 3

#Find index of element 30.

t = (10, 20, 30, 40)
print(t.index(30))   # 2

#Unpack tuple into variables.

t = (1, 2, 3)
a, b, c = t
print(a, b, c)


#Convert a list into a tuple.

lst = [1, 2, 3]
t = tuple(lst)
print(t)

#Join two tuples.

t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2

print(t3)   # (1, 2, 3, 4)

#Check if 20 exists in tuple.

t = (10, 20, 30)
if 20 in t:
    print("Found")
else:
    print("Not Found")

#Find number of elements.

t = (1, 2, 3, 4, 5)
print(len(t))   # 5

#Access element 4 from nested tuple.

t = (1, 2, (3, 4, 5))
print(t[2][1])   # 