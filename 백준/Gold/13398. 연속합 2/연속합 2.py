import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
L = [0] * N
L[0] = A[0]
check = L[0]
for i in range(1, N):
    L[i] = max(A[i], L[i-1] + A[i])
    check = max(check, L[i])
    
R = [0] * N
R[-1] = A[-1]
for i in range(N-2, -1, -1):
    R[i] = max(A[i], R[i+1] + A[i])

result = check 
for i in range(1, N-1):
    temp = L[i-1] + R[i+1]
    result = max(result, temp)
    
print(result)