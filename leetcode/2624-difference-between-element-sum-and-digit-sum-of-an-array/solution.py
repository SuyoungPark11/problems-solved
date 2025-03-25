class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            if num < 10: 
                res += num
            else: 
                for i in str(num):
                    res += int(i)
                    
        return abs(sum(nums) - res)
