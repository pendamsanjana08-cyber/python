#Create a dictionary with name, age, and course.
student = {"name": "John", "age": 20, "course": "CS"}
print(student)


#Print the value of "name".
student = {"name": "John", "age": 20}
print(student["name"])


#Safely access "age".
student = {"name": "John", "age": 20}
print(student.get("age"))


#Add "email" to dictionary.
student = {"name": "John"}
student["email"] = "john@gmail.com"
print(student)

#Change age to 25.
student = {"name": "John", "age": 20}
student["age"] = 25
print(student)

#Remove "age".
student = {"name": "John", "age": 20}
student.pop("age")
print(student)


# Print all keys and values.
student = {"name": "John", "age": 20}

for key, value in student.items():
    print(key, value)


# Check if "name" exists.
student = {"name": "John", "age": 20}
if "name" in student:
    print("Exists")


#Combine two dictionaries.
a = {"x": 1, "y": 2}
b = {"z": 3}
a.update(b)
print(a)

#Count frequency of numbers in a list.
lst = [1, 2, 2, 3, 3, 3]
freq = {}
for num in lst:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)