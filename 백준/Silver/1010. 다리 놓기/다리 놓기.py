import sys
input = sys.stdin.readline

C = [[0 for _ in range(31)] for _ in range(31)]
for i in range(0, 31):
    C[i][1] = i
    C[i][0] = 1
    C[i][i] = 1

for i in range(2, 31):
    for j in range(1, i):
        C[i][j] = C[i-1][j] + C[i-1][j-1]

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    print(C[M][N])