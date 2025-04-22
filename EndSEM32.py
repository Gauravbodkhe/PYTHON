# 32. Class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object and passing parameters
person1 = Person("John", 30)
person1.display()
