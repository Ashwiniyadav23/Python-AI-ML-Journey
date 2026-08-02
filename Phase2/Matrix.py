# Step 1: What is a Matrix?
# A matrix is a just a table of numbers


# calculate rows and columns
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(matrix)
columns = len(matrix[0])


print("Rows:", rows)
print("Columns:", columns)


# Matrix addition 

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# rows = len(matrix)
# columns = len(matrix[0])

# sum = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         sum = sum + matrix[i][j]
# print(sum)


# matrix multiplication
matrix_multiplication =[
    [1,2,3,4],
    [5,6,7,8]
]
sum = 1
for i in range(len(matrix_multiplication)):
    for j in range(len(matrix_multiplication[i])):
        sum = sum * matrix_multiplication[i][j]
print(sum)