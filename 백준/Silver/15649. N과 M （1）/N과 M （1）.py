import sys
input = sys.stdin.readline

def backtrack(numbers):
    if len(numbers) == M:
        print(' '.join(map(str, numbers)))
        return
    
    for i in range(1, N+1):
        if visited[i] == False:
            visited[i] = True
            numbers.append(i)
            backtrack(numbers)
            numbers.pop()
            visited[i] = False
        
N, M = map(int, input().split())
visited = [False] * (N+1)
backtrack([])