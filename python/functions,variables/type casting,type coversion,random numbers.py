#Create a program where:
#a = "25"
#Convert it into an integer
#Add 10 to it
#Print the result.a="25"
a="25"
b=int(a)
c=b+10
print(c)

#2 convert a
#convert b
#add both values
#print the sum
a="15"
b="20"
x=int(a)+int(b)
print(x)

#3 Write a program:
#num = 12.75
#Convert it into an integer
#Print the result and its type.
num=12.75
n=int(num)
print(n)
print(type(n))

#4 Write a program where:
#x = 100
#convert it into a string
#print "The value is " + x
x=100
y=str(x)
print("the value is", y)

#5 Write a program:
#a = "15"
#b = 5
#Convert a properly so you can add both numbers and print the result.
a="15"
b=5
c=int(a)+b
print(c)

#6 Write a program where:
#x = "45"
#Convert it to float
#Print the value and its data type.
x="45"
y=float(x)
print(y)
print(type(y))

#7 Write a program using the random module to generate a random number between 1 and 10.
import  random
print(random.randint(1,10))

#8 Write a program that:
#Generates a random number between 1 and 100
#Prints "Random number is:" with the number.
import random
print("random number is:",random.randint(1,100))

#9 Write a program that randomly chooses one value from this list:
#["Python", "Java", "C++", "JavaScript"]
import random
languages = ["Python", "Java", "C++", "JavaScript"]
choice = random.choice(languages)
print("Random language is:", choice)

#10 Random Float
#Write a program to generate a random float number between 0 and 1.
import random
number=random.random()
print(number)