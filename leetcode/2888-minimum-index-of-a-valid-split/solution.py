from collections import Counter

class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count1 = Counter()
        count2 = Counter(nums)

        for i, num in enumerate(nums):
            count1[num] = count1[num] + 1
            count2[num] = count2[num] - 1
            if count1[num] * 2 > i + 1 and count2[num] * 2 > len(nums) - i - 1:
                return i
        return -1
        
