import sys

n, m = map(int, sys.stdin.readline().split())
a = [[0] * (n+1)]
for _ in range(n):
    row = [0] + list(map(int, sys.stdin.readline().split()))
    a.append(row)

D = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = a[i][j] + D[i-1][j] + D[i][j-1] - D[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)