import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
waiting = deque(map(int, input().split()))
temp = []
order = 1

while waiting or temp:
    if waiting and waiting[0] == order:
        waiting.popleft()
        order += 1
    elif temp and temp[-1] == order:
        temp.pop()
        order += 1
    elif waiting:
        temp.append(waiting.popleft())
    else:
        break
        
if order == n+1:
    print("Nice")
else:
    print("Sad")