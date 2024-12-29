def backtrack(nums, start):
    if len(nums) == M:
        print(*nums)
        return 

    for i in range(start, N+1):
        nums.append(i)
        backtrack(nums, i)
        nums.pop()

N, M = map(int, input().split())
backtrack([], 1)