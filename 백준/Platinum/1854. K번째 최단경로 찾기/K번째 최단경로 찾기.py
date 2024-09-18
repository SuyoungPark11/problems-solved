import sys
import heapq
input = sys.stdin.readline

def function(graph, start):
    distances = [[float('inf')] * k for _ in range(n + 1)]
    distances[start][0] = 0
    pq = [(0, start)] 
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor][k-1]:
                distances[neighbor][k-1] = distance
                distances[neighbor].sort()
                heapq.heappush(pq, [distance, neighbor])
    
    return distances

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

routes = function(graph, 1)

for idx in range(1, n+1):
    if routes[idx][k-1] == float('inf'):
        print(-1)
    else:
        print(routes[idx][k-1])