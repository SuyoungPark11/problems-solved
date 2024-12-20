import sys
input = sys.stdin.readline

def backtracking(x, y, start, numbers):
    if len(numbers) == y:
        print(*numbers)
        return
    
    for i in range(start, n+1):
        numbers.append(i)
        backtracking(n, m, i+1, numbers)
        numbers.pop()
        
n, m = map(int, input().split())
backtracking(n, m, 1, [])