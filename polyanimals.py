class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Dogesh se Pangaa nahi Mittrrrr"

class Cat(Animal):
    def sound(self):
        return "Laadlee Meowwwww, Ghok Ghok Ghok"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())