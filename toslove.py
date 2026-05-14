# Count Words in a Sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))


#  Sort List in Ascending Order

numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers)

# Print Pattern

rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# Find Factorial Using Function

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = int(input("Enter a number: "))
print("Factorial:", factorial(num))