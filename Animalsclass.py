class animals():
    def __init__(self, name):
        self.name =name

    def pet(self):
        print("There are many types of Animals.")
        print("We cannot pet most of them.")


class animaltype(animals):   #Inheritance

    def __init__(self, name, size, color):
        self.color = color
        self.__type = "animal"   #Encapsulation
        self.size = size
        animals.__init__(self, name)

    def printanimals(self):
        print("Animal Name: ", self.name)
        print("Animal Size: ", self.size)
        print("Animal Colour: ", self.color)
        print("Animal Type: ", self.__type)

    def changetype(self, type):
        self.__type = type

class Elephant(animals):

    def pet(self):
        print("We cannot pet an Elephant.")


class Dog(animals):

    def pet(self):
        print("We can pet a dog.")



#Inheritance

print("Inheritance")
b = animaltype("Tiger", "Big", "Black")
b.printanimals()

#Polymorphism

print("Polymorphism")
x = animals("animals")
x.pet()
y = Elephant("Elephant")
y.pet()
z = Dog("dogs")
z.pet()


#Encapsulation
print("Encapsulation")
a = animaltype("Monkey", "small", "brown")

a.__type = "Not an animal"
a.printanimals()
a.changetype("Not animal")
a.printanimals()
