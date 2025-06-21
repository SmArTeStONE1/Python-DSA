class Car:
    def __init__(self, Color, Model, Price):
        self.Color = Color
        self.Model = Model
        self.Price = Price
bmw = Car("Blue", "M8", "9M")
audi = Car("Red", "A1", "3M")
print(bmw.Color)
print(audi.Color)

class smartphone:
    def __init__(self, Storage, Model, Price):
        self.Storage = Storage
        self.Model = Model
        self.Price = Price
samsung = smartphone("128GB", "S21", "1M")
iphone = smartphone("256GB", "iPhone 13", "1.2M")
print(samsung.Storage)
print(iphone.Storage)
class Laptop:
    def __init__(self,Price,Brand,Model,Storage)
        self.Price= Price
        self.Brand = Brand
        self.Model = Model
        self.Storage = Storage
dell = Laptop("1.5M", "Dell", "XPS 13", "512GB")
hp = Laptop("1.2M", "HP", "Spectre x360", "1TB")
MacBook = Laptop("2M", "Apple", "MacBook Pro", "1TB")
asus = Laptop("1.8M", "Asus", "ZenBook 14", "512GB")
Lenovo = Laptop("1.4M", "Lenovo", "ThinkPad X1", "1TB")
print(dell.Brand)
print(hp.Brand)
print(MacBook.Brand)
print(asus.Brand)
print(Lenovo.Brand)
print(dell.Storage)
print(hp.Storage)
print(MacBook.Storage)
print(asus.Storage)
print(Lenovo.Storage)
class Animal:
    def __init__(self, Species, Age, Habitat):
        self.Species = Species
        self.Age = Age
        self.Habitat = Habitat
lion = Animal("Lion", 5, "Savannah")
tiger = Animal("Tiger", 4, "Rainforest")
elephant = Animal("Elephant", 10, "Grassland")
print(lion.Species)
print(tiger.Age)
print(elephant.Habitat)