'''
### 🧠 Question 1

Create a global variable `x = 10`.

Create a function that:

* Prints the value of `x`
* Does NOT modify it

Call the function and observe whether it can access the global variable.

---

### 🧠 Question 2

Create a global variable `count = 5`.

Inside a function:

* Try to increase `count` by 1
* Print it

Run the program and observe the error.
Then fix it using the `global` keyword.

---

### 🧠 Question 3

Create a function where:

* A variable `a = 20` is declared inside the function.
* Print it inside the function.

Now try to print `a` outside the function.
What happens?

---

### 🧠 Question 4

Create:

```
x = 100
```

Create a function that:

* Creates a new local variable also named `x = 50`
* Prints `x` inside the function

After calling the function, print `x` outside.

Observe the difference between local and global scope.

---

### 🧠 Question 5

Create a global variable `total = 0`.

Create two different functions:

* One function adds 10 to `total`
* Another function adds 20 to `total`

Make sure the changes affect the same global variable.

Print final value of `total`.'''

s=14
def bd():
    print(s)# as s is declared globally we acess  even acessvit to local
bd()

count=5
def myfun():
    global count#without global keyword we cannot as so here to change keyword inside a function we used globak keyword
    count=count+1#5+1
    print(count)#6
myfun()#function call

def num():
    a=20
    print(a)#20
num()#to call the function
#print(a)here op is a is not defined as we didnot created the variable globally

x = 100
def ex():
    x=50
    print(x)#locally assigned x will be printed 50
ex()
print(x)#globally assinged variable 100

total=0
def fun1():
    global total
    total=total+10
fun1()
def fun2():
    global total
    total=total+20
fun2()
print(total)