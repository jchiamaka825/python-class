name = "my name is Louis"
print(name[0])
for i in name:
    print(i)

    tup1 = ("shoe", "Hand bag", "Shirts", "Cards")
    for item in tup1:
        print (item)
        print (item.upper())
        print (item[0].upper())
ar =[2,4,5,6,7,8,9,10,11,43,23,52,]
c = []
for num in ar:
    y = num*2
    c.append(y)
    #print(c)

num1 = [x*2 for x in ar]
print (num1)

list1 = []
for d in tup1:
    b = d.upper()
    list1.append(b)
    #print(list1)

#condition with for loop
for num in range(1,11):
    if num %2 ==0:
        print(num*2)
    else:
        print(num)

for c in range(2,20, 2):
    print(c*2)
names = ["Amara", "Steve", "ben", "carl", "Rowland"]
for n in names:
    if len(n)<=3:
        print(n.lower())
    elif len(n)<=5:
        print(n.title())
    else:
        print(n.upper())




