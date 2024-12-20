import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    init = input().rstrip()
    if 'push' in init:
        _, i = init.split()
        stack.append(int(i))
    elif init == 'pop':
        print(-1) if len(stack) == 0 else print(stack.pop())
    elif init == 'size':
        print(len(stack))
    elif init == 'empty':
        print(1) if len(stack) == 0 else print(0)
    elif init == 'top':
        print(-1) if len(stack) == 0 else print(stack[-1])
    