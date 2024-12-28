def backtrack(numbers):
    if len(numbers) == M:
        print(' '.join(map(str, numbers)))
        return
    
    for i in range(1, N+1):
        numbers.append(i)
        backtrack(numbers)
        numbers.pop()

N, M = map(int, input().split())
backtrack([])