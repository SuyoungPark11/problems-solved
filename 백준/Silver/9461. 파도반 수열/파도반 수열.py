import sys
input = sys.stdin.readline

t = int(input())
p = [0] * 101
p[1], p[2], p[3], p[4], p[5] = 1, 1, 1, 2, 2
for _ in range(t):
    n = int(input())
    if n <= 5:
        print(p[n])
    else:
        for i in range(5, n+1):
            p[i] = p[i-3] + p[i-2]
        print(p[n])