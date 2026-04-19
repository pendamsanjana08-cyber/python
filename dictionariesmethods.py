#Add a new key-value pair to dictionary.

d = {"a": 1, "b": 2}
d.update({"c": 3})
print(d)


#Access value of key without error.

d = {"a": 10, "b": 20}
print(d.get("c", "Not Found"))


#Remove key "b" and return its value.

d = {"a": 1, "b": 2}
x = d.pop("b")
print(x)
print(d)


#Remove last inserted key-value pair.

d = {"a": 1, "b": 2, "c": 3}
d.popitem()
print(d)


#Print all keys.

d = {"x": 10, "y": 20}
print(d.keys())


#Print all values.

d = {"x": 10, "y": 20}
print(d.values())


#Print key-value pairs.

d = {"a": 1, "b": 2}
print(d.items())


#Create a copy and modify it.

d1 = {"a": 1}
d2 = d1.copy()
d2["b"] = 2
print(d1)
print(d2)


#Create dictionary with same values.

keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print(d)


#Add key with default value if not present.

d = {"a": 1}
d.setdefault("b", 100)
print(d)
