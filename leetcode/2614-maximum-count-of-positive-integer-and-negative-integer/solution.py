class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negative = [n for n in nums if n < 0]
        positive = [n for n in nums if n > 0]
        return len(negative) if len(negative) > len(positive) else len(positive)
        
