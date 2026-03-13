#converts the first character to upper case
a="she is sweet!"
b=a.capitalize()
print(b)	

#Converts string into lower case
c="PYTHON IS INSANE"
d=c.casefold()
print(d)

#Returns a centered string
e="sanjana"
f=e.center(40)	
print(f)

#Returns the number of times a specified value occurs in a string
g="she is sweet as well as cute"
h="blue are my fvrt colour,blue is love,sky is blue in the mrng"
i=g.count("as")
j=h.count("blue")
print(i)
print(j)

#Returns true if the string ends with the specified value
k="kind!"
l=k.endswith("!")
print(l)

#Sets the tab size of the string
m="h\tel\tml\tlb\tdp"
n=m.expandtabs(2)
print(n)

#Searches the string for a specified value and returns the position of where it was found
o="hi this is sanj"
p=o.find("sanj")
q=o.find("saj")
print(p)
print(q)#if not found then it will give -1

#Formats specified values in a string
r="{python} programming"
s=r.format(python=c)#connected to varaible from starting program using keyword casefold()
print(s)

#Formats specified values from a dictionary in a string
t={"name":"sanj","rollno":14,"age": 19}
u="iam {name},my rollno is {rollno},and iam {age} years old!"
v=u.format_map(t)	
print(v)

#Searches the string for a specified value and returns the position of where it was found
w="i study my btech in hyd"
x=w.index("i")
y="iam sanjana hello"
z=y.index("sanjana")
print(x)
print(z)

