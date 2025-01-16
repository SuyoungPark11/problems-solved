import sys
from collections import deque
input = sys.stdin.readline

nodes = int(input())
edges = int(input())
graph = [[] for _ in range(nodes+1)]

for _ in range(edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(g, v):
    visited = [False] * (nodes+1)
    visited[v] = True
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        for i in g[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    return visited

visited = bfs(graph, 1)
print(sum(visited)-1)