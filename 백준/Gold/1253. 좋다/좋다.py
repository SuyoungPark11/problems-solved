import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A = sorted(A)
count = 0
for k in range(n):
    i = 0 
    j = n-1    
    while i < j:
        if A[k] == (A[i] + A[j]):
            if (i != k) and (j != k): # '서로 다른 두 수'니까 추가되어야 하는 조건 
                count += 1
                break
            elif i == k: 
                i += 1
            elif j == k:
                j -= 1
        elif A[k] < (A[i] + A[j]):
            j -= 1
        else:
            i += 1

print(count)