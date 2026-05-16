# Convert String to List

text = input("Enter words separated by space: ")
words = text.split()
print(words)

#  Find Minimum Number in a List

numbers = [34, 2, 78, 1, 56]
print("Minimum number:", min(numbers))


#  Check Leap Year

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#  Find ASCII Value of Character

ch = input("Enter a character: ")
print("ASCII value:", ord(ch))