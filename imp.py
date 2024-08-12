from func import divide

print(divide(10))
print(len(range(10)))

#lambda functions
x = lambda y : y *2
print(x(10))

name = lambda fname, Iname : f"How are you {fname} {Iname}"
print(name("john", "Bright"))

b = list(map(lambda x: x/3, [15,30,45,60]))
print(b)
