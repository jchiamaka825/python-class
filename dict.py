
d = {2}
print(type(d))

f = {1:20, 2:30}
print(type(f))

a ={1,2,3,4,3,2,3,5,4}
print (a)

c ={"a", "b", "c", "d","a", "c", "b"}
print(c)

c.add("k")
print(c)

print(c.pop())
#c.remove("b")
print(c)

g = {"car","House","Shop", "Church2"}
r = {"man", "woman", "boy", "girl", "car"}

d= g.union(r)
print(d)

print(g.intersection(d))
print(g.symmetric_difference(r))

k = r.update(g)
print(k)

#Dictionaries

y = {"Age": 20, "Address":"mgbuoba", "hubby":"Dancing"}
print(y)
print(y["Age"])
print(y["Address"])

y["mood"] = "Happy"
print(y)

for c in g:
    print(c)

for x in y.keys():
    print(x)

    for k in y.values():
        print(k)

for i,j in y.items():
    print(j,":",i)
#Dict comprehension
u ={i for i in y.values()}
print(u)

I = {i for i in y.keys()}
print(I)
