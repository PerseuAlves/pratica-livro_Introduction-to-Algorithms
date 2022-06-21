#!/usr/bin/python3

import math

def parent(i):
    return i / 2

def left(i):
    return 2 * i

def right(i):
    return (2 * i) + 1

def maxHeapify(A, i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] > A[i]:
        maior = l
    else:
        maior = i
    if r < len(A) and A[r] > A[maior]:
        maior = r
    if maior != i:
        aux = A[i]
        A[i] = A[maior]
        A[maior] = aux
        maxHeapify(A, maior)

def buildMaxHeap(A):
    for i in range(math.trunc(len(A)/2), 0, -1):
        maxHeapify(A, i)


'# Test'
A = [-1, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
buildMaxHeap(A)

# Sem tirar o índice 0 que não é alterado na ordenação
print("Original:")
print(A)

print("")

# Tirando o indice 0
bSize = (len(A) - 1)
B = [0] * bSize
for j in range(0, len(A)-1):
    B[j] = A[j+1]
print("Saída esperada:")
print(B)
