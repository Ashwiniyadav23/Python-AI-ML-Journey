import numpy as np

# 1D array — like a single list

A = np.array([1,2,3,4,5,6])
print(A)  # [1 2 3 4 5 6]


# 2D array — like a table/matrix (rows and columns)

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)




# 2. Vectorized Operations — doing math to a whole array at once

marks = np.array([80, 90, 70, 60])

new_marks = marks + 5
print(new_marks)   # [85 95 75 65]


# 3. Broadcasting — combining arrays of different shapes

marks = np.array([80, 90, 70, 60])
print(marks + 5)   # [85 95 75 65]