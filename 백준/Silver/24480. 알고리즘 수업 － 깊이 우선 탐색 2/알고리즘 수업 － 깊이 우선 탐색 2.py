import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

order = 1
def dfs(graph, v, visited):
    global order
    visited[v] = order
    for i in graph[v]:
        if not visited[i]:
            order += 1
            dfs(graph, i, visited)


N, M, R = map(int, input().split())
G = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(N+1):
    G[i].sort(reverse=True)

dfs(G, R, visited)

for i in range(1, N+1):
    print(visited[i]) 