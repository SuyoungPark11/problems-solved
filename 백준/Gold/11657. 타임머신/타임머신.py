import sys
input = sys.stdin.readline

N, M = map(int, input().split())

E = []
for _ in range(M):
    u, v, w = map(int, input().split())
    E.append((u, v, w))

def bellman_ford(start, graph):
    D = [float('inf')] * (N+1)
    D[start] = 0

    for _ in range(N-1):
        for s, e, w in graph:
            if D[s] != float('inf') and D[e] > D[s] + w:
                D[e] = D[s] + w

    for s, e, w in graph:
        if D[s] != float('inf') and D[e] > D[s] + w:
            return False
    return D

check = bellman_ford(1, E)

if not check:
    print(-1)
else:
    for i in range(2, N+1):
        if check[i] != float('inf'):
            print(check[i])
        else:
            print(-1)