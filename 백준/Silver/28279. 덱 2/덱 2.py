import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
D = deque()
for _ in range(N):
    prompt = input().split()  # 입력 문자열 분리

    command = int(prompt[0])

    if command == 1:
        D.appendleft(int(prompt[1]))
    elif command == 2:
        D.append(int(prompt[1]))
    elif command == 3:
        if D: print(D.popleft())
        else: print(-1)
    elif command == 4:
        if D: print(D.pop())
        else: print(-1)
    elif command == 5:
        print(len(D))
    elif command == 6:
        if D: print(0)
        else: print(1)
    elif command == 7:
        if D: print(D[0])
        else: print(-1)
    elif command == 8:
        if D: print(D[-1])
        else: print(-1)