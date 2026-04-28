# Write a Python program to create an iterator from a list and print all elements using next().

numbers = [10, 20, 30, 40]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

 #Create an iterator for a string and print each character one by one.

word = "Python"
it = iter(word)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# Use an iterator with a while loop to print tuple elements

data = ("apple", "banana", "mango")

it = iter(data)

while True:
    try:
        print(next(it))
    except StopIteration:
        break


    # Create a custom iterator that prints numbers from 1 to 5.

class Numbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

obj = Numbers()

for i in obj:
    print(i)


# Create an infinite iterator that generates even numbers.

class EvenNumbers:
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        self.num += 2
        return self.num

obj = EvenNumbers()
it = iter(obj)

for i in range(5):
    print(next(it))


# Use reversed() to iterate through a list in reverse order.

numbers = [1, 2, 3, 4, 5]

it = reversed(numbers)

for i in it:
    print(i)


# Create an iterator for dictionary keys and print them.

student = {
    "name": "John",
    "age": 21,
    "course": "Python"
}

it = iter(student)

print(next(it))
print(next(it))
print(next(it))


# Create an iterator for a set and print elements.
colors = {"red", "blue", "green"}

it = iter(colors)

for i in colors:
    print(next(it))

#Create a custom iterator to generate Fibonacci numbers.

class Fibonacci:
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

fib = Fibonacci()
it = iter(fib)

for i in range(7):
    print(next(it))


# Create an iterator from a list comprehension and print values.

squares = [x * x for x in range(1, 6)]

it = iter(squares)

for i in squares:
    print(next(it))
