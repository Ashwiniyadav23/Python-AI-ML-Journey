
# class dog:    #Create a blueprint called Dog.
# def __init__(self, name, breed)


class students:
    def __init__(self, name, marks):
        self.name = name
        self.marks =marks
    def display(self):       # Method to display the student's details
        print(f"Name: {self.name} Marks: {self.marks}")

s1 = students("Ashwini", 95)
s1.display()