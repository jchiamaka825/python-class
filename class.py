class food:
    x = "Eba"
    y = "Noodle"

print(food.y)
print(food.y)

class play:
    def name(fname, iname):
        print (f"Hello {fname} {iname} hope you are playing")

play.name("john", "kenny")

class Happy:
    def __init__(self, fname, iname):
       self.fname = fname
       self.iname =iname
       print(f"Hello{self,fname} {self.iname}")

       h = Happy("Herny", "Bossy")
       print(h.fname)
       print(h.iname)

class Animal:
    def __init__(self,name,age,leg):
        self.name = name
        self.age = age
        self.leg = leg

    def display(self):
        print(f"The name of this animal is {self.name}")
        print(f"This animal is {self.age}years old")
        print(f"This animal has {self.leg} leg")

A = Animal("cow",102,4)
print(A.name)
print(A.age)
print(A.leg)
A.display()


