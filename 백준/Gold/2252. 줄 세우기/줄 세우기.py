import sys
from collections import deque
input = sys.stdin.readline

def topological_sort(vertices, edges):
    in_degree = [0] * (vertices+1)
    graph = [[] for _ in range(vertices+1)]
    
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
    queue = deque([i for i in range(1, vertices+1) if in_degree[i] == 0])
    topological_order = []
    
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(topological_order) != vertices:
        return []
    
    return topological_order

N, M = map(int, input().split())
order = []
for _ in range(M):
    A, B = map(int, input().split())
    order.append((A, B))

result = topological_sort(N, order)
print(' '.join(map(str, result)))