import sys
input = sys.stdin.readline

def backtrack(nums, idx):
    if len(nums) == M:
        print(*nums)
        return

    for i in range(idx, len(ref)):
        nums.append(ref[i])
        backtrack(nums, i)
        nums.pop()


N, M = map(int, input().split())
ref = set(list(map(int, input().split())))
ref = sorted(ref)

backtrack([], 0)