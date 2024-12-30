import sys
input = sys.stdin.readline

def backtrack(nums):
    if len(nums) == M:
        print(*nums)
        return 
    
    for itm in ref:
        if itm in nums:
            continue
        nums.append(itm)
        backtrack(nums)
        nums.pop()
        
N, M = map(int, input().split())
ref = list(map(int, input().split()))
ref.sort()
backtrack([])