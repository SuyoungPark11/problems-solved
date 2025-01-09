import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
result = []

for i in range(N - 7):
    for j in range(M -7):
        cnt1 = 0
        cnt2 = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'W':
                        cnt1 += 1
                    if board[x][y] != 'B':
                        cnt2 += 1
                else:
                    if board[x][y] != 'B':
                        cnt1 += 1
                    if board[x][y] != 'W':
                        cnt2 += 1
        result.append(cnt1)
        result.append(cnt2)

print(min(result))