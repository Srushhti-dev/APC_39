class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo!")


animals = [Dog("Tommy"), Cat("Kitty"), Cow("Gauri")]

for animal in animals:
    animal.eat()
    animal.sound()
