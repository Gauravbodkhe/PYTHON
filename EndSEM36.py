# 36. Animal and Dog classes
class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        print(f"{self.species} makes a sound")

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def bark(self):
        print(f"{self.breed} says Woof!")

dog1 = Dog("Mammal", "Labrador")
dog1.sound()
dog1.bark()
