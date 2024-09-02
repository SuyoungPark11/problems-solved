import sys
import math

input = sys.stdin.readline
m, n = map(int, input().split())
lst = [0] * (n+1)

for i in range(2, n+1): lst[i] = i

n_sq = int(math.sqrt(n))
for i in range(2, n_sq+1):
    if lst[i] == 0:
        continue
    for j in range(i+i, n+1, i): # i 배수 지우기 
        lst[j] = 0

for i in range(m, n+1):
    if lst[i] != 0:
        print(lst[i])