a = []
b = list()
print(type(a))
print(type(b))

num =[1,2,3,4,5]
print(len(num))
print(num[2])

name = ["John", "Peter", "Andrew", "Phillp"]
print(name[2])

name.append("kelvin")
print(name)

name.insert(1, "Joy")
print(name)

name.insert(0, "Gift")
print(name)

name.remove("Phillp")
print(name)

popped_name =name.pop(4)
print("Hello "+ popped_name)

name2=["George", "Bassey", "Paul"]
name = name + name2
print(name)

List1 = ["BMW", "Toyota", "Audi", "Benz"]
List2 = ["sequia", "Lexus"]
List1.extend(List2)
print(List1)

print(List1[0].lower())
print(List1[0].capitalize())
print("Toyota" in List1)

for i in List1:
    print("i have " + i)
    
print(list(range(1,10+1)))

#List comprehension
b = [x**2 for x in range(1,10+1)]
print(b)

#Tuple
() #Tuple
[] # List

e = tuple()
d =()
print(type(e))
print(type(d))

name[3] = "matthew"
print(name)

loc = ("Uzoaba", "Obiri Kwere", "Rumuosi")
print(loc)

dd =list(loc)
print(dd)
dd[2] = "NTA"
dd.append("Rumosi")
print(dd)     

y =(i.upper() for i in loc)
print(tuple(y))

f1 = (1,2,3,4)
f2 =(5,6,7,8)
f3 = zip(f1,f2)
print(list(f3))
print(tuple(f3))

#new class on list
print(List1[:3])

num = list(range(1,10,+1))
print(num[:3])
print(num[4:])

num2= num[:]
print(num)
#Tuple
tt = list(loc).copy()
print(tt)

num3 =[2,3,4,2,4,3,2,]
num3.sort()
print(num3)

num4 =[1,3,5,2,3,6,3,2,4,5]
num4.reverse()


num5 =[1,3,5,2,3,6,3,2,4,5]
num5.sort(reverse=True)
print(num5)

freq = max(num3, key=num3.count)
print(freq)

x=[3,4,5,6,7,4]
del x[1]
#del1 x
print(x)

print(num4.count(5))

print(num4.index(3))

tup = ("a", "b", "c", "d")
print(tup[2:])
print(len(x))
print(x[3:])

print(sorted(x))





print(tup[:2])




num







      