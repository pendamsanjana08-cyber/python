# Find common elements present in two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
common = []
for item in list1:
    if item in list2:
        common.append(item)

print("Common elements:", common)

# Remove duplicate elements from a list without using set().

numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("List after removing duplicates:", unique)