#Create two variables a = 10, b = 10 and check if both refer to the same object.
a = 10
b = 10
print(a is b)


#Create two lists with same values and check if they are the same object.
x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)

#Assign one list to another variable and check identity.
a = [5, 6]
b = a
print(a is b)


#Check if two variables are not the same object.
a = [10, 20]
b = [10, 20]

print(a is not b)


#Create two same strings and check if they refer to same object.
a = "hello"
b = "hello"

print(a is b)


#Create a variable with None and check identity.
x = None
y = None

print(x is y)

#Create x = 100, y = 200 and check identity.
x = 100
y = 200

print(x is y)

#Assign list2 = list1 and check identity.
list1 = [1, 2, 3]
list2 = list1

print(list1 is list2)


#Create two variables separately and check identity.
a = 50
b = 60
print(a is b)


#Check both value equality and identity.
a = [1, 2]
b = [1, 2]
print(a == b)
print(a is b)
