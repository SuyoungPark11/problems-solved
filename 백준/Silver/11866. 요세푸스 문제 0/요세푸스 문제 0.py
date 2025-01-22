import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
josephus = deque([i for i in range(1, N+1)])
result = []

while josephus:
    for _ in range(K-1):
        josephus.append(josephus.popleft())
    result.append(josephus.popleft())

ans = '<'
for i in range(len(result)):
    if i == len(result)-1:
        ans += str(result[i]) + '>'
    else:
        ans += str(result[i]) + ', '

print(ans)