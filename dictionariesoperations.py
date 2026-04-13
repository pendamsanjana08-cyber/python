#Print all keys and values.

d = {"k": 1, "o": 2, "m": 3}
for key, value in d.items():
    print(key, value)

#Find sum of dictionary values.
f = {"r": 10, "b": 20, "p": 30}
total = 0
for value in f.values():
    total += value

print(total)

#Count how many values are greater than 10.
s = {"w": 5, "u": 15, "x": 25}
count = 0

for v in s.values():
    if v > 10:
        count += 1

print(count)


#Create a copy and modify it.
d1 = {"a": 1, "b": 2}
d2 = d1.copy()

d2["c"] = 3

print("Original:", d1)
print("Copy:", d2)

#Show difference between direct assignment and copy.
d1 = {"a": 1}
d2 = d1          # reference
d3 = d1.copy()   # copy

d2["b"] = 2

print(d1)  # changed
print(d3)  # unchanged


#Print student names and marks.
students = {
    "s1": {"name": "A", "marks": 90},
    "s2": {"name": "B", "marks": 80}
}

for key, val in students.items():
    print(val["name"], val["marks"])


#Print marks of student s1.
students = {
    "s1": {"name": "A", "marks": 90}
}

print(students["s1"]["marks"])


#Add grade to each student.
students = {
    "s1": {"marks": 90},
    "s2": {"marks": 70}
}

for s in students:
    if students[s]["marks"] > 80:
        students[s]["grade"] = "A"
    else:
        students[s]["grade"] = "B"

print(students)


#Find student with max marks.
students = {
    "s1": {"marks": 90},
    "s2": {"marks": 95},
    "s3": {"marks": 85}
}

max_marks = 0
top_student = ""

for s in students:
    if students[s]["marks"] > max_marks:
        max_marks = students[s]["marks"]
        top_student = s

print(top_student, max_marks)


#Show problem with nested dictionary copy.
import copy

d1 = {"a": {"x": 1}}
d2 = d1.copy()        # shallow copy

d2["a"]["x"] = 100

print(d1)   # also changed ❗

# Correct way:
d3 = copy.deepcopy(d1)