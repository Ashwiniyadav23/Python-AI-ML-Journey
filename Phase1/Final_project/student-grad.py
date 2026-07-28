# Student Grade Manager
# A small CLI project for practicing Phase 1 Python fundamentals:
# variables, loops, functions, data structures, strings, OOP, and file I/O.



# Step 1: Start with the simplest possible version

Students = []

def add_students(name, grades):
    student = {"name": name, "grades": grades}
    Students.append(student)

add_students("Ashwini", [80])  

print(Students)

# Step 2: Add a function to calculate averages

def calculate_avg(grades):
    return sum(grades) / len(grades)

for student in Students:
    avg = calculate_avg(student["grades"])
    print(f"{student['name']}: Average = {avg:.2f}")




# Step 3: Convert it into a class (this is where OOP pays off)
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if not self.grades:         
            return 0
        return sum(self.grades) / len(self.grades)

    def display(self):
        print(f"{self.name}: Grades={self.grades}, Average={self.average():.2f}")

s1 = Student("Ashwini")
s1.add_grade(85)
s1.add_grade(90)
s1.display()




# Step 4: Build a manager class to hold all students


class GrandeManager:
    def __init__(self):
        self.students = []  # will hold students objects

    def add_student(self,name):
        student = Students(name)
        self.students.append(student)
        return student
    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower(): # case-insensitive match
                return student
        return None # not found
    
    def display_all(self):
        if not self.students:
            print("No students added yet.")
            return
        for student in self.students:
            student.display()

    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average())
        
