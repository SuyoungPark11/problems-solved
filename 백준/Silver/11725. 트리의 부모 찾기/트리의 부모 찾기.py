import sys
input = sys.stdin.readline

def dfs(graph, start):
    visited = [False] * (len(graph) + 1)
    answer = [0] * (len(graph) + 1)
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True

            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    answer[neighbor] = node
                    stack.append(neighbor)

    return answer


N = int(input())
nodes = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    nodes[A].append(B)
    nodes[B].append(A)

ans = dfs(nodes, 1)
for i in range(2, N+1):
    print(ans[i])