import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph, start):
    distances = [float('inf')] * (len(graph) + 1)
    distances[start] = 0
    pq = [(0, start)] 
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

a, b = map(int, input().split())

routes = dijkstra(graph, a)
print(routes[b])