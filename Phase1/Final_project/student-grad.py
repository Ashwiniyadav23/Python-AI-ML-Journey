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

