import sys
input = sys.stdin.readline

n = int(input()) 
m = int(input())
D = [[float('inf')] * (n+1) for _ in range(n+1)]

# 자기 자신에게 가는 거리 = 0
for i in range(1, n+1): 
    D[i][i] = 0

for _ in range(m):
    start, end, weight = map(int, input().split())
    if D[start][end] > weight:
        D[start][end] = weight

# 점화식에 따라 업데이트
for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if D[s][e] > (D[s][k] + D[k][e]):
                D[s][e] = (D[s][k] + D[k][e])

for i in range(1, n+1):
    for j in range(1, n+1):
        if D[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(D[i][j], end=' ')
    print()