#What is the difference between append() and extend()? Show with code.

a = [1, 2, 3]
b = [4, 5]
a.append(b)
print("append:", a)   # [1, 2, 3, [4, 5]]
a = [1, 2, 3]
a.extend(b)
print("extend:", a)   # [1, 2, 3, 4, 5]

#Remove the first occurrence of 20 from the list.

list = [10, 20, 30, 20, 40]
list.remove(20)
print(list)   # [10, 30, 20, 40]


#Remove and print the last element using pop().

list1 = [1, 2, 3, 4]

x = list1.pop()
print("Removed:", x)   # 4
print(list1)# [1, 2, 3]


#Insert value 99 at index 2.

st = [10, 20, 30, 40]

st.insert(2, 99)
print(st)   # [10, 20, 99, 30, 40]

#Count how many times 5 appears in the list.

t = [5, 1, 5, 2, 5, 3]
print(t.count(5))   # 3


#Find index of element 30.

l = [10, 20, 30, 40]
print(l.index(30))   # 2

#Sort a list in descending order.
m = [5, 2, 9, 1]
m.sort(reverse=True)
print(m)   # [9, 5, 2, 1]


#Reverse the list using method.
c= [1, 2, 3, 4]

c.reverse()
print(c)   # [4, 3, 2, 1]

#Create a copy of a list and modify the copy.

a = [1, 2, 3]
b = a.copy()

b.append(4)

print("Original:", a)   # [1, 2, 3]
print("Copy:", b)       # [1, 2, 3, 4]

#Remove all elements from a list.
mylist1 = [1, 2, 3]

mylist1.clear()
print(mylist1)   # []