import sys
input = sys.stdin.readline

def backtrack(nums):
    if len(nums) == M:
        print(*nums)
        return

    prev = 0
    for idx, itm in enumerate(ref):
        if prev == itm or visited[idx]:
            continue
        visited[idx] = True
        prev = itm
        nums.append(itm)
        backtrack(nums)
        nums.pop()
        visited[idx] = False

N, M = map(int, input().split())
ref = list(map(int, input().split()))
ref.sort()
visited = [False] * N
backtrack([])