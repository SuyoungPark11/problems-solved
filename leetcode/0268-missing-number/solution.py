class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        lst = [i for i in range(n+1)]
        for num in nums:
            if num in lst:
                lst.remove(num)
        return lst.pop()

        
