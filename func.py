def name(fname, Iname):
   return f" {fname} {Iname}"

def add(num1,num2):
   return num1 * num2

def divide(num):
   return num/2

def addsub(num1,num2):
   return num1 + num2 -20

print(addsub(10,5))

# Lambda function
d = lambda num : num * 2
print(d(10))

s = lambda fname, iname : f"Hello {fname} {iname}"
print(s("john","moses"))

def multiply(n):
   return lambda x : x * n

f = multiply(10)
print(f(5))

# map function
x = tuple(map(lambda n: n * 5,[4,5,6,7,5]))
print(x)
y = list(map(lambda n,t :n** t,[1,2,3,4,],[5,6,7,8]))
print(y)

#print(2** 6)
#print(3 ** 7)

g = list(map(addsub, [2,4,5,6],[4,6,7,8]))
print(g)

#fliter function

def calsub(num1):
   if (num1 + 5) % 2 == 0:
      return num1 + 5
   else:
      return False
   
rt = list(filter(calsub, [1,2,3,4,5,6,7,8]))
print(rt)

u = tuple(filter(lambda n : n if n % 3 == 0 else False,[2,3,4,9,12,15,18,16]))
print(u)

from functools import reduce
# reduce

lis = reduce(lambda a,b: a if a < b else b, [2,4,5,6,7])
print(lis)

yer = reduce(lambda a,b: a if a> b else b, [2,4,6,7])
print(yer)

ge = reduce(lambda a,b: a+b,[2,4,5,6,7])
print(ge)




#
