#!/usr/bin/python3

import random

def ordenar_A_P(A, P):
    n = len(A)
    aux = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if P[j] < P[i]:
                aux = P[i]
                P[i] = P[j]
                P[j] = aux
                '#--------'
                aux = A[i]
                A[i] = A[j]
                A[j] = aux
    print(A)
    print(P)

def Permute_By_Sorting(A):
    n = len(A)
    P = [0] * n
    for i in range(0, n):
        P[i] = random.randint(0, n**3)
    ordenar_A_P(A, P)


'# Test'
A = [1,  2,  3,  4]

Permute_By_Sorting(A)
