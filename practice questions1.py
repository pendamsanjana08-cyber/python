# Take marks of 5 subjects and calculate total, average, and grade.

marks = []
for i in range(5):    
    mark = int(input(f"Enter marks for subject {i+1}: "))   
    marks.append(mark)
    total = sum(marks)
    average = total / 5
    if average >= 90:    
     grade = "A"
    elif average >= 75:    
        grade = "B"
    elif average >= 50:    
        grade = "C"
    else:    
        grade = "Fail"
print(f"Total Marks: {total}")
print(f"Average: {average}")
print(f"Grade: {grade}")

# Find common elements present in two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
common = []
for item in list1:
    if item in list2:
        common.append(item)
print("Common elements:", common)