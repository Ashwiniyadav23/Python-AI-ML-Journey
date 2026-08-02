# 2. Abstraction (Showing Only What's Necessary)

# Code Explanation – Abstraction Example

## Code

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 50:
            print("Passed")
        else:
            print("Failed")

s1 = Student("Ashwini", 95)

s1.result()
