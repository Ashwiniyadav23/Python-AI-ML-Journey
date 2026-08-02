
# Wha is Numpy:   "NumPy is a Python library for fast numerical computing using arrays."

# Why NumPy?

# Suppose you have marks.

80
90
70
60
# You want to add 5 bonus marks.


# Python List:   You need a loop.

marks = [80,90,70,60]

new_marks = []

for i in marks:
    new_marks.append(i+5)

print(new_marks)


# NumPy

import numpy as np
marks = np.array([12,34,5,6])
print(marks+5)




# Matrix Multiplication (connecting to your linear algebra work)



A = np.array([[2, 3], [4, 5]])
B = np.array([[10], [20]])

result = A @ B          # or np.matmul(A, B)
print(result)
# [[ 80]
#  [140]]