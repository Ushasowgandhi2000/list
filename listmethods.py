x=["apple","mango","kiwi","banana"]
print(x[-4:-1])

x=[565,77,34,99,45]
y={"apple","mango","kiwi","banana"}
x.extend(y)
print(x)

x=[565,77,34,99,45]
z=x*4
print(z)

x=[565,77,34,99,45]
y=["apple","mango","kiwi","banana"]
z=x+y
print(z)

x=[565,77,34,99,45]
del x[2:4]
print(x)

x=[565,77,34,99,45]
x.sort()
print(x)
print(len(x))
