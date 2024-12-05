import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, N+1):
    sep = i + sum(map(int, str(i)))
    if sep == N:
        print(i)
        break
    if i == N:
        print(0)