import sys

n = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

sorted_P = sorted(P, reverse=False)

S = [0] * n
S[0] = sorted_P[0]

for i in range(1, n):
    S[i] = S[i-1] + sorted_P[i]

sum = 0
for i in range(n):
    sum += S[i]

print(sum)