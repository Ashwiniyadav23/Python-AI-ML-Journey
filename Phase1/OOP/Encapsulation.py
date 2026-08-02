# Encapsulation which keeps variable (data) or methods(functions) in a one class.

class Students:
    def __init__(self, name,Marks,roll):
        self.name = name
        self.Marks = Marks
        self.roll = roll
    def display(self):
        print(f"Name: {name} Marks: {Marks} roll-no {roll}")
s1 = (name:"Ashwini", Marks:89, roll:20)
Students.display()