#!/usr/bin/python3

def Square_Matrix_multiply(A, B):
    n = len(A)
    C = [[0] * n, [0] * n, [0] * n]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = 0
            for k in range(0, n):
                C[i][j] = (C[i][j] + (A[i][k] * B[k][j]))
    return C


'# Test'
A = [[3, -1, 0], [2, 5, 1], [-7, 1, 3]]
B = [[6, -1, 0], [0, 1, -2], [3, -8, 1]]

C = Square_Matrix_multiply(A, B)

print(C)
