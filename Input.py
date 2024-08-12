fname = input("Enter your first name:")
iname = input("Enter your last name:")
print(f"{fname} {iname}")

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number: "))
#print(num1 + num2)

#input && while loop
x= 10
i =5
while i< x:
    print(i)
    i+=1

#N = input("what is your best color")
r =[]
#while r !="quit":
#   N = input("what is your best color")
#   f = f"Your best color is{N}
#   r.append(f)
#   print(r)

userName =""
user = []

while userName != "quit":
    name = input("Enter your name! ")

    if name =="quit":
        break
    else:
        user.append(name)
        print(user)

list1 = ["card", "food", "Dress", "spoon"]
re =[]
while list1 !=[]:
    c = list1.pop()
    re.append(c)
    print(re)

