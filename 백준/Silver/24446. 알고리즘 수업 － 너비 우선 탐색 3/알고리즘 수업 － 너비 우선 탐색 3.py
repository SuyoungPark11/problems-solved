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
    answers = [-1] * (N+1) 
    depth = 0
    answers[v] = depth
    visited[v] = True
    q = deque()
    q.append([v, depth])
    while q:
        v, d = q.popleft()
        answers[v] = d
        for i in graph[v]:
            if not visited[i]:
                q.append([i, d+1])
                visited[i] = True

    return answers

for i in range(N+1):
    G[i].sort(reverse=True)

answer = bfs(G, R)
for i in range(1, N+1):
    print(answer[i])