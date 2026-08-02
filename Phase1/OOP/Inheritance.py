# 3. Inheritance (Reusing Existing Code)

class Animal:

    def eat(self):
        print("Eating...")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()