import sys
input = sys.stdin.readline

n, m = map(int, input().split())
D = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1): 
    D[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    D[a][b] = 1
    D[b][a] = 1

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if D[s][e] > (D[s][k] + D[k][e]):
                D[s][e] = (D[s][k] + D[k][e])

Min = float('inf')
Answer = -1

for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        temp += D[i][j]
    if Min > temp:
        Min = temp
        Answer = i

print(Answer)