#Object Oriented Programming

#Class - Bluprint to Make objects
#Object - Real Things

class Car:
    color = "red"
    wheel = 4
    seat = 6
    engine = "v9"


bmw = Car()
ferrari = Car()
audi = Car()

print(bmw.seat)
print(bmw.color)
print(audi.color)

#init -> COnstructor. init funchelps to create objects

class Car:
    def __init__(self,Color,Model,Price):
        self.Color = Color 
        self.Model = Model
        self.Price = Price


bmw = Car("Blue","M8","9M")
audi = Car("Red","A1","3M")

print(bmw.Color)
print(audi.Color)

