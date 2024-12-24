import sys
input = sys.stdin.readline

t = int(input())
f = [0] * 12
f[1], f[2], f[3] = 1, 2, 4
for _ in range(t):
    n = int(input())
    if n <= 3:
        print(f[n])
    else:
        for i in range(4, n+1):
            f[i] = f[i-1] + f[i-2] + f[i-3]
        print(f[n])
    
    