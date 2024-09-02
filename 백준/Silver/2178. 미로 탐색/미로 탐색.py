import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
G = [[0] * m for _ in range(n)]
visit_check = [[False] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(n):
    line = list(input())
    for j in range(m):
        G[i][j] = int(line[j])

def bfs(graph, start, visit):
    queue = deque()
    queue.append(start)
    i = start[0]
    j = start[1]
    visit[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >= 0 and y >= 0 and x < n and y < m :
                if graph[x][y] != 0 and not visit[x][y]:
                    visit[x][y] = True
                    graph[x][y] = graph[now[0]][now[1]] + 1
                    queue.append((x,y))

bfs(G, (0,0), visit_check)
print(G[n-1][m-1])