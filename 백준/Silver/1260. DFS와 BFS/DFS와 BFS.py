import sys
from collections import deque

input = sys.stdin.readline
n, m, s = map(int, input().split())
Adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    Adj[u].append(v)
    Adj[v].append(u)

for i in range(1, n+1): # 문제 조건에 노드 번호가 작은 것 부터 먼저 방문
    Adj[i].sort()


def dfs(graph, start, visit):
    visit[start] = True
    print(str(start), end=' ')
    for i in graph[start]:
        if not visit[i]:
            dfs(graph, i, visit)

def bfs(graph, start, visit):
    queue = deque()
    queue.append(start)
    visit[start] = True
    while len(queue) != 0:
        node = queue.popleft()
        print(str(node), end=' ')
        for i in graph[node]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True   

visit_check = [False] * (n+1)
dfs(Adj, s, visit_check)
print()
visit_check = [False] * (n+1)
bfs(Adj, s, visit_check)