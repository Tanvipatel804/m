#Oops Concept(Inheritance and Polymorephism)
"""class student:
    def __init__(self,name):
        self.name = name

s1 = student("Tanvi")
print(s1.name)

del s1
print(s1)

class car():
    color = "black"
    @staticmethod
    def start():
        print("Car is started.....")

    @staticmethod
    def stop():
        print("Car is stopped.......")

class toyotacar(car):
    def __init__(self,name):
       self.name = name

car1 = toyotacar("Fortuner")
car2 = toyotacar("spark")

print(car1.name)
print(car1.color)
print(car2.name)
print(car2.color)

class student():
    def __init__(self,name,phy,chem,math):
         self.name = name
         self.phy = phy
         self.chem = chem
         self.math = math
     
    @property
    def percentage(self):
         return self.name + (str(self.phy + self.chem + self.math) / 3) + "%"
   
    
s1 = student("Om",89,87,69)
print(s1.name)
print(s1.phy)
print(s1.chem)
print(s1.math)

s1.phy = 96
print(s1.percentage)"""

class circle():
    def __init__(self,radius):
         self.radius = radius
        
    def area(self):
         return 3.14 * self.radius

    def perimeter(self):
         return 2 * 3.14 * self.radius
         
r1 = circle(2)
print(r1.area())
print(r1.perimeter())