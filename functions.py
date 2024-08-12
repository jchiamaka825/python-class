def num ():
    return "today is monday!"

print(num())
print(num())
print(num())

def add():
    return 2-5

print(add())

b = "This is python class"
print(len(b))

def addtwoNum(num):
    return num + 10

print(addtwoNum(20))

def username(fname, Iname):
    print(f"your name is {fname} {Iname}")
    print("your name is "+fname+""+Iname)
          
username("john", "doe")

def calculate(num1, num2):
    symbols = input("choose from this symbols "+","-","*","/":")
    if symbols == "+":
        return(num1+num2)
    elif symbols == "-":
        return num1/num2
    elif symbols == "*":
        return num1/num2
    elif symbols == "/":
        return num1/num2
    
    print(calculate(10,5))

    #fristname = input("Enter your frist name")
    #lastname = input("Enter your lastname")

def user(frist, last):
    return f"welcome {frist} {last}"
    
#print(user(fristname, lastnmae))
 
l= [2,5,4,6,7,8,11,12]
def calc (arr):
    d = []
    for i in arr:
        if i % 2==0:
            d.append(i*2)
            print(d)

        else:
            print(i)

def Greet(user="mark"):
    return f"Good evening {user}"

print(Greet("peter"))
print(Greet())

#frist =input("Enter your first name")
#last = input("Enter your last name:")
#middle = input("Enter your middle name:")

def salute(frist,last,middle=""):
    if middle == "":
        print(f"{frist} {last}")
    else:
        print(f"{frist} {middle} {last}")

#salute(frist,last,middle)

# functions with keyword argument
def dog(name,breed): 
    return f"I have a dog named {name} whose breed is {breed}"
print(dog("Willie", "Shiwawa"))#keyword argument
print(dog(breed= "Shiwawa",name="Willie"))#positional Arugument

def thingsTobuy(meat, oil, Rice):
    print(f"i just bought {meat} meat")
    print(f"I just bought {oil} oil")
    print(f"I just bought {Rice} rice")

thingsTobuy("Foreign", "Goat", "Red")# keyword Argument
thingsTobuy(Rice="Foreign", meat="Goat",oil="vergetable")#positional Arugement!!

def play(name, *args): # Mutiple keyword Arugement
      return f"this user is called {name} and has a {args[1]}"

print(play("moses", "car", "house"))

#functions with mutiple positional argument
def sleep(bed, **args):

    args["bed"] = bed
    return f"I sleep on {args} {bed}"

print(sleep("roll", water="water", foam="foam"))

def run(person, *type, **types):
    types["person"] = person
    return f"{person} runs {type[0]} and has {types}"
print(run("sandra", "100 meters", "200 meters", jump="High jump", Relay="senoir Relay"))


              





