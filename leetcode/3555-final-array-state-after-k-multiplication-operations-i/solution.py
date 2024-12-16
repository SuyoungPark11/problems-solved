class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            x = min(nums)
            idx = nums.index(x)
            nums[idx] = x * multiplier
        return nums        
