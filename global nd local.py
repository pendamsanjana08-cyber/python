'''Good 😄 you came back for the tricky ones.
Now we level up your brain a little.

These are **thinking questions** — don’t rush.

---

## 🧠 Tricky Question 1

Predict the output **before running**:

```python
x = 10

def test():
    print(x)
    x = 20

test()
```

Questions:

* Will it print 10?
* Will it print 20?
* Or will it give an error?
* Why?

Think carefully about **local vs global + assignment rule**.

---

## 🧠 Tricky Question 2

Predict the output:

```python
x = 5

def change():
    global x
    x = x + 5
    print("Inside:", x)

change()
print("Outside:", x)
```

Questions:

* What prints inside?
* What prints outside?
* Why are they same or different?

x = 10

def test():
    print(x)
    x = 20# it will consider it as local nd global keyword is not used to change the value so error

test()'''

x = 5

def change():
    global x
    x = x + 5
    print("Inside:", x)#x=5+5=10
change()
print("Outside:", x)#10 because it is lastest updated value of x
