# Write a program to reverse a list without using built-in reverse function.

arr = [1, 2, 3, 4, 5]

reversed_arr = []
for i in range(len(arr)-1, -1, -1):
    reversed_arr.append(arr[i])

print(reversed_arr)


# Find the largest and smallest number in a list.

arr = [10, 20, 4, 45, 99]

max_val = arr[0]
min_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max:", max_val)
print("Min:", min_val)

# Calculate sum of all elements.

arr = [1, 2, 3, 4, 5]

total = 0
for num in arr:
    total += num

print("Sum:", total)


# Remove duplicate elements from list.

arr = [1, 2, 2, 3, 4, 4, 5]

unique = []
for num in arr:
    if num not in unique:
        unique.append(num)

print(unique)


# Count how many times each element appears

arr = [1, 2, 2, 3, 3, 3]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

# Find second largest number in list.

arr = [10, 20, 4, 45, 99]

largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest:", second)


# Rotate list to the right by one position.

arr = [1, 2, 3, 4, 5]

last = arr[-1]
for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1]

arr[0] = last

print(arr)


# Check whether list is sorted in ascending order.


arr = [1, 2, 3, 4, 5]

is_sorted = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break

print(is_sorted)


# Merge two lists into one.

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

merged = arr1 + arr2
print(merged)


# Find common elements between two lists.

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
common = []
for num in arr1:
    if num in arr2 and num not in common:
        common.append(num)
print(common)