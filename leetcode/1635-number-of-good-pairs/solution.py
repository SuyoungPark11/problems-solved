class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            ref = nums[i]
            for j in range(i+1, n):
                if ref == nums[j]:
                    count += 1
        return count
        
