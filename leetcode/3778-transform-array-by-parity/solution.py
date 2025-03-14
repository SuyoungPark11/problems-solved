class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted([0 if n % 2 == 0 else 1 for n in nums])
