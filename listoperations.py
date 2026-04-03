#1.Take a list,Add "rose" to the list.

flowers = ["tulips","jasmine","lotus"]
flowers.append("rose")
print(flowers)

#2.Take a list,Insert "grape" at index 1.
fruits = ["apple", "banana"]
fruits.insert(1, "grape")
print(fruits)

#3.Remove "ball" from the list.

toys= ["bat","car","shettle","ball"]
toys.remove("ball")
print(toys)

#4.Remove the last element from the list.

numbers = [10, 20, 30]
numbers.pop()
print(numbers)


#5.Print the length of a list.

numbers = [17,93,81,77]
print(len(numbers))

#6.Sort the list in ascending order.

numbers = [99,55,77,66,44]
numbers.sort()
print(numbers)

#6.Reverse the list

numbers = [41,88,67,44]
numbers.reverse()
print(numbers)

#7.Check if "a" exists in the list.

f = ["a", "b","c","d","e"]
print("a" in f)

#8.Create a copy of a list.

list1 = [14,23,44,66]
list2 = list1.copy()
print(list2)

#9.Remove all elements from a list.

numbers = [12,14,16,18]
numbers.clear()
print(numbers)