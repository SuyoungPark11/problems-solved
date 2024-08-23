import sys

n = list(input()) # 이거만 바꿈
A = list(map(int, n))

for i in range(len(A)):
    max_index = i
    for j in range(i+1, len(A)):
        if (A[max_index] < A[j]):
            max_index = j
    if (A[i] < A[max_index]):
        temp = A[i]
        A[i] = A[max_index]
        A[max_index] = temp 

A = list(map(str, A))
print("".join(A))