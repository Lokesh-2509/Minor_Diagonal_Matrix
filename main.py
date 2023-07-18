def sum_minor_diagonal(matrix):
    n = len(matrix)
    diagonal_sum = 0
    for i in range(n):
        j = n - i - 1
        diagonal_sum += matrix[i][j]
    return diagonal_sum
A = [
    [1, -2, -3],
    [-4, 5, -6],
    [-7, -8, 9]
]
result = sum_minor_diagonal(A)
print(result)
