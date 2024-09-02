import sys

input = sys.stdin.readline
m, n = map(int, input().split())
lst = [0] * (10000001)

for i in range(2, len(lst)): lst[i] = i

for i in range(2, int(len(lst)**0.5)+1):
    if lst[i] == 0:
        continue
    for j in range(i+i, len(lst), i): 
        lst[j] = 0

count = 0 
for i in range(2, len(lst)):
    if lst[i] != 0:
        temp = lst[i]
        while lst[i] <= n / temp:
            if lst[i] >= m / temp:
                count += 1
            temp = temp * lst[i] 

print(count)