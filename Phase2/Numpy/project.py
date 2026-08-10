"""
Student Marks Analyzer — a short NumPy practice project.
Covers: array creation, vectorized math, aggregates, boolean filtering, sorting.
"""

import numpy as np

# Marks for 6 students across 4 subjects (rows = students, columns = subjects)
marks = np.array([
    [80, 90, 70, 60],
    [50, 40, 30, 20],
    [95, 88, 92, 91],
    [60, 65, 70, 75],
    [30, 45, 50, 55],
    [100, 95, 90, 85]
])

student_names = np.array(["Ashwini", "Raj", "Aisha", "Meera", "Sam", "Ken"])

print("=== Student Marks Analyzer ===\n")

# 1. Basic shape info
print(f"Number of students: {marks.shape[0]}")
print(f"Number of subjects: {marks.shape[1]}\n")

# 2. Add 5 bonus marks to every score (vectorized — no loop needed)
bonus_marks = marks + 5
print("Marks after +5 bonus (first student):", bonus_marks[0], "\n")

# 3. Average mark per student (row-wise mean)
averages = marks.mean(axis=1)
print("Average marks per student:")
for name, avg in zip(student_names, averages):
    print(f"  {name}: {avg:.2f}")
print()

# 4. Average mark per subject (column-wise mean)
subject_averages = marks.mean(axis=0)
print("Average marks per subject:", subject_averages, "\n")

# 5. Highest and lowest overall scores
print(f"Highest single score: {marks.max()}")
print(f"Lowest single score: {marks.min()}\n")

# 6. Find the top student (highest average)
top_index = np.argmax(averages)
print(f"Top student: {student_names[top_index]} with average {averages[top_index]:.2f}\n")

# 7. Filter — students passing overall (average >= 60)
passing_mask = averages >= 60
passing_students = student_names[passing_mask]
print("Students passing (average >= 60):", passing_students, "\n")

# 8. Sort students by average (descending)
sorted_indices = np.argsort(averages)[::-1]   # [::-1] reverses ascending -> descending
print("Ranking (highest to lowest average):")
for rank, idx in enumerate(sorted_indices, start=1):
    print(f"  {rank}. {student_names[idx]} — {averages[idx]:.2f}")