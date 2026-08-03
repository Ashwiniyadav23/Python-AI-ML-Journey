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



# 1st problem

qualified = (M >= 75) & (A >= 85) & (B == 0)
print(qualified)
count = np.sum(qualified)
print("Qualified Students:", count)


