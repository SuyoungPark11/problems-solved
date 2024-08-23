import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
S = [0] * n
for i in range(n):
    if i == 0 :
        S[i] = A[i]
    else:
        S[i] = S[i-1] + A[i]

# 나머지를 저장할 딕셔너리 초기화
remainder_count = defaultdict(int)
count = 0

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        count += 1
    count += remainder_count[remainder]
    remainder_count[remainder] += 1
    
print(count)