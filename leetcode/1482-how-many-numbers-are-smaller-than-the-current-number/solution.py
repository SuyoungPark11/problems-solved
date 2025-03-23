class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        dictionary = {}
        for i, v in enumerate(sorted_nums):
            if v not in dictionary:
                dictionary[v] = i
        arr = [] 
        for n in nums:
            arr.append(dictionary[n])
        return arr

