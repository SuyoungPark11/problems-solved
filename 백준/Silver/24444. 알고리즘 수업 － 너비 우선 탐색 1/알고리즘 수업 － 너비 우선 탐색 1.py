import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
G = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

order = 1

def bfs(graph, v):

    global visited, order

    visited[v] = order
    q = deque([v])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                order += 1
                visited[i] = order
                q.append(i)

for i in range(N+1):
    G[i].sort()

bfs(G, R)

for i in range(1, N+1):
    print(visited[i])