# Check whether a string is palindrome without using [::-1].

text = input("Enter a string: ")
reverse = ""
for ch in text:
    reverse = ch + reverse
if text == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")


# Print Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# Count how many times each character appears in a string.

text = input("Enter a string: ")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# Find the second largest element in a list.

numbers = [10, 45, 23, 89, 67]
numbers.sort()
print("Second Largest Number:", numbers[-2])