import sys
input = sys.stdin.readline

n = int(input())
G = [] 
for _ in range(n):
    row = list(map(int, input().split()))
    G.append(row)

for k in range(n):
    for s in range(n):
        for e in range(n):
            if (G[s][k] == 1) & (G[k][e] == 1):
                G[s][e] = 1

for i in range(n):
    for j in range(n):
            print(G[i][j], end=' ')
    print()