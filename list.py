#Create a list of 3 fruits and print it.

fruits = ["apple", "banana", "mango"]
print(fruits)

#Print the first element of a list.
numbers = [10, 20, 30]
print(numbers[0])

#Print the last element of a list.
numbers = [100, 200, 300]
print(numbers[-1])

#Add an element "orange" to a list.

fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)

#Insert "grape" at index 1.
fruits = ["apple", "banana"]
fruits.insert(1, "grape")
print(fruits)

#Remove "banana" from list.
fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)

#Length of List
#Find the length of a list.
numbers = [1, 2,8, 4]
print(len(numbers))

#Loop Through List
#Print all elements in a list.
numbers = [0,9,8, ]
for i in numbers:
    print(i)

#Check Element
#Check if "apple" is in the list.
fruits = ["apple", "banana"]
print("apple" in fruits)


# Update Element
#Change "banana" to "orange".
fruits = ["apple", "banana"]
fruits[1] = "orange"
print(fruits)