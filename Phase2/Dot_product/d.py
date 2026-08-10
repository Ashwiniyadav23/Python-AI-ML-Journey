# Dot Product
# The dot product is calculated by multiplying corresponding elements
# of two vectors and adding the results.

A = [1, 2, 3]
B = [4, 5, 6]

dot = 0

for i in range(len(A)):
    dot += A[i] * B[i]

print("Dot Product =", dot)

# Output:
# Dot Product = 32