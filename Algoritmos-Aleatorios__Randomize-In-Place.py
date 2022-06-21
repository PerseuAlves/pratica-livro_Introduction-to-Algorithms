#!/usr/bin/python3

import random

def Randomize_In_Place(A):
    n = len(A)
    for i in range(0, n):
        tempRandomNum = random.randint(0, (((n - i) + i) - 1))
        aux = A[i]
        A[i] = A[tempRandomNum]
        A[tempRandomNum] = aux


'# Test'

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Randomize_In_Place(A)
print(A)
