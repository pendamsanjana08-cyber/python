# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  # True


# 2. Function to return factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

# 3. Function to count vowels in a string

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # 3


#4. Function to find the maximum element in a list

def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([2, 8, 1, 5]))  # 8


#*5. Function using args to calculate sum

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10
