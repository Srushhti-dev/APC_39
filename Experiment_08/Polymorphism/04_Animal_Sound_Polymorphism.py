class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog: Woof!")


class Cat(Animal):
    def sound(self):
        print("Cat: Meow!")


class Cow(Animal):
    def sound(self):
        print("Cow: Moo!")


class Lion(Animal):
    def sound(self):
        print("Lion: Roar!")


for animal in [Dog(), Cat(), Cow(), Lion()]:
    animal.sound()
