#Write a program that converts the string "hello world" into uppercase.
text = "hello world"
result = text.upper()
print(result)

#Write a program that converts "PYTHON PROGRAMMING" to lowercase.

text = "PYTHON PROGRAMMING"
result = text.lower()
print(result)

#Remove spaces from the string "   Python   ".

text = "   Python   "
result = text.strip()
print(result)

#Replace "Java" with "Python" in the string "I love Java".

text = "I love Java"
result = text.replace("Java", "Python")
print(result)

#Count how many times "a" appears in "banana".

text = "banana"
result = text.count("a")
print(result)

#Check if the string "Python is easy" starts with "Python".

text = "Python is easy"
result = text.startswith("Python")
print(result)

#Check if the string "file.pdf" ends with "pdf".

text = "file.pdf"
result = text.endswith("pdf")
print(result)

#Find the index of "world" in "Hello world".

text = "Hello world"
result = text.find("world")
print(result)

#Split the sentence "Python is fun" into words.

text = "Python is fun"
result = text.split()
print(result)

#Join the list ["Python", "is", "fun"] into a single sentence.

words = ["Python", "is", "fun"]
result = " ".join(words)
print(result)