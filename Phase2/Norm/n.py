# 2. Norm (Vector Length): How long vector Norm tells whats the length of a vector.


import math

A = [3,4]

norm = math.sqrt(A[0]**2 + A[1]**2)

print(norm)



import numpy as np

A = np.array([3, 4])
norm = np.linalg.norm(A)

print(norm)   # 5.0