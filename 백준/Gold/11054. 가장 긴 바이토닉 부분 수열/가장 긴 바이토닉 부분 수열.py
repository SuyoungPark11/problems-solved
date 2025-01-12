import sys
input = sys.stdin.readline
 
N = int(input())
A = list(map(int, input().split()))
A_rev = A[::-1]
inc = [1] * N
dec = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if A_rev[i] > A_rev[j]:
            dec[i] = max(dec[i], dec[j]+1)

dp = [0] * N
for i in range(N):
    dp[i] = inc[i] + dec[N-i-1] - 1

print(max(dp))