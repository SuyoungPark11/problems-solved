import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

def bfs(graph, v):
    visited = [False] * (N+1)
    answers = [0] * (N+1) 
    depth, order = 0, 1
    answers[v] = depth
    visited[v] = True
    q = deque()
    q.append([v, depth])
    while q:
        v, d = q.popleft()
        answers[v] = d
        for i in graph[v]:
            if not visited[i]:
                order += 1
                q.append([i, d+1])
                visited[i] = order

    return answers, visited

for i in range(N+1):
    G[i].sort()

answer, visited = bfs(G, R)
print(sum([answer[i] * visited[i]  for i in range(1, N+1)]))