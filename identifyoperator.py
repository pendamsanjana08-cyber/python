#is operator
x= ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#isnot operator
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)


#difference between is and ==
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
