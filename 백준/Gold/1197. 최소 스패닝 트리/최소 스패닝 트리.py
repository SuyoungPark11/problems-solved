import sys
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int, input().split())

uf_list = [0] * (V+1)
for i in range(V+1):
    uf_list[i] = i

pq = PriorityQueue()
for _ in range(E): 
    s, e, w = map(int, input().split())
    pq.put((w, s, e)) 

def find(a):
    if a == uf_list[a]:
        return a
    else:
        uf_list[a] = find(uf_list[a])
        return uf_list[a]
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        uf_list[b] = a

edge = 0
result = 0
while edge < V-1:
    w, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        edge += 1
        result += w

print(result)