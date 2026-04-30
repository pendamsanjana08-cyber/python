# Find Largest Among Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest = a
if b > largest:   
     largest = b
if c > largest:    
     largest = c
print("Largest number is:", largest)



# Check Whether a Number is Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num > 0:    
    print("Positive Number")
elif num < 0:    
    print("Negative Number")
else:    
    print("Zero")
