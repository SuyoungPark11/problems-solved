import sys
input = sys.stdin.readline

T = int(input())
C = [[0 for _ in range(15)] for _ in range(15)]

for i in range(1, 15):
    C[i][1] = 1
    C[0][i] = i

for i in range(1, 15):
    for j in range(2, 15):
        C[i][j] = C[i][j-1] + C[i-1][j]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(C[k][n])