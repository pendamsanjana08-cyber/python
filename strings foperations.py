#Create a string "I like Java" and replace "Java" with "Python".
s="I like Java" 
print(s.replace("Java","python"))

#Create a string "apple apple apple" and replace the word "apple" with "mango".
a="apple apple apple"
print(a.replace("apple","mango"))

#Replace "bad" with "good" in the string:"This is a bad day".
l="This is a bad day"
print(l.replace("bad","good"))

#Split the string "apple,banana,mango" using , as the separator.
s="apple,banana,mango"
print(s.split(","))

#split the sentence "Python is easy to learn" into words.
p="Python is easy to learn"
p1=(p.split(" "))
print(p1)

#Split "2025-03-10" using - and store the result in a list.
date = "2025-03-10"
result = date.split("-")
print(result)

#Create two variables:
#first = "Hello"
#second = "World"
#Join them together using concatenation.
first = "Hello"
second = "World"
print(first+second)

#Join "Python" and "Programming" with a space between them using concatenation.
r="python"
k="programming"
print(r+ " " +k)

#Use format() to print:
#My name is Sanjana.
name = "Sanjana"
print("My name is {}".format(name))

#Create variables name and age and print:
#My name is ____ and I am ____ years old.
name="dimpu"
age=19
print(f"My name is {name} and I am {age} years old.")

#Use format() to print:
#The price of the book is 500.
price=500
print("The price of the book is {}".format(price))

#Create variables name="Sanjana" and city="Hyderabad" and print:
#Sanjana lives in Hyderabad. using f string
name="Sanjana" 
city="Hyderabad" 
print(f"{name} lives in {city}")

#create variables a=10 and b=20 and print:
#The sum of 10 and 20 is 30 using f-string.
a=10 
b=20
print(f"The sum of {a} and {b} is {a+b}")

#Create variables course="Python" and duration="3 months" and print:
#I am learning Python for 3 months.
course="Python" 
duration="3 months"
print(f"I am learning {course} for {duration}")


