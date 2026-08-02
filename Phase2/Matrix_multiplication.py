A = [
    [2, 3],
    [4, 5]
]

B = [
    [10],
    [20]
]

result = [
    [0],
    [0]
] # for storing result

for i in range(len(A)):          # Rows of A
    for j in range(len(B[0])):   # Columns of B
        for k in range(len(B)):  # Common dimension
            result[i][j] += A[i][k] * B[k][j]

print(result)