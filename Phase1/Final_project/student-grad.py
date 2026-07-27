"""
Student Grade Manager
A small CLI project for practicing Phase 1 Python fundamentals:
variables, loops, functions, data structures, strings, OOP, and file I/O.
"""



# Step 1: Start with the simplest possible version

Students = []
def add_students(name,grade):
    student = {"name":name, "grades": grade}
    Students.append(student)
add_students("Ashwini",80)
print(Students)

