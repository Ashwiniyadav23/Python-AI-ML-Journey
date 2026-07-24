# 4. Polymorphism (One Interface, Many Forms)

class Dog:

    def sound(self):
        print("Woof")

class Cat:

    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()