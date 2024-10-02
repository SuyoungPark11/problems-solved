import sys
input = sys.stdin.readline

N, K = map(int, input().split())
C = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(0, N+1):
    C[i][1] = i
    C[i][0] = 1
    C[i][i] = 1
    
for i in range(2, N+1):
    for j in range(1, i):
        C[i][j] = C[i-1][j] + C[i-1][j-1]

print(C[N][K])