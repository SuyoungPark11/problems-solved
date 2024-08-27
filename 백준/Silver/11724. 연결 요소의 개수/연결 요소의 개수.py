import sys

sys.setrecursionlimit(10**6) # BOJ에서는 재귀가 1000회 제한이라서 필요
input = sys.stdin.readline
n, m = map(int, input().split())

def dfs(graph, start, visit):
    visit[start] = True
    for i in graph[start]:
        if not visit[i]:
            dfs(graph, i, visit)

# 인접 리스트 그래프 표현
Adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    Adj[u].append(v)
    Adj[v].append(u)
# 방문 초기화 
visit_check = [False] * (n+1)

count = 0
for i in range(1, n+1):
    if not visit_check[i]:
        dfs(Adj, i, visit_check)
        count += 1

print(count)