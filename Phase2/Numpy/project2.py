""" Problem 1
A student qualifies if
Marks ≥ 75
Attendance ≥ 85
No backlog
Count qualified students.

Problem 2
Store qualified students' marks.
Find
Highest
Lowest
Average

Problem 3
Scholarship Rules
Gold: Marks ≥ Highest − 5
Silver: Marks ≥ Average
Bronze: Remaining qualified students
Print all three categories separately.
"""
import numpy as np

# Marks
M = np.array([20, 30, 60, 80, 66, 95])

# Attendance
A = np.array([90, 60, 40, 87, 95, 12])

# Backlog
# 0 = No Backlog
# 1 = Has Backlog
B = np.array([1, 0, 1, 0, 0, 1])

# Problem 1

qualified = (M >= 75) & (A >= 85) & (B == 0)

count = np.sum(qualified)

print("Qualified Students:", count)

# Problem 2

qualified_marks = M[qualified]

print("\nQualified Students Marks:", qualified_marks)

if qualified_marks.size > 0:
    highest = np.max(qualified_marks)
    lowest = np.min(qualified_marks)
    average = np.mean(qualified_marks)

    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Average:", average)

    # Problem 3

    gold = qualified_marks[qualified_marks >= (highest - 5)]
    silver = qualified_marks[
        (qualified_marks >= average) &
        (qualified_marks < (highest - 5))
    ]
    bronze = qualified_marks[qualified_marks < average]

    print("\nGold Scholarship:", gold)
    print("Silver Scholarship:", silver)
    print("Bronze Scholarship:", bronze)

else:
    print("No qualified students.")