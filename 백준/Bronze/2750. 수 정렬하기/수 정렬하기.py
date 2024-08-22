import sys

n = int(sys.stdin.readline())
A = []

for _ in range(n):
    A.append(int(sys.stdin.readline()))

for i in range(n):
    for j in range(n-1-i):
        if A[j] > A[j+1]:
            temp = A[j] # j+1가 아니고, j 
            A[j] = A[j+1]
            A[j+1] = temp
        
for i in range(n):
    print(A[i])