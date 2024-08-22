import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()

for i in range(1, n+1):
    stack.append(i)

while len(stack) != 1:
    stack.popleft()
    top = stack.popleft()
    stack.append(top)

print(stack[0])