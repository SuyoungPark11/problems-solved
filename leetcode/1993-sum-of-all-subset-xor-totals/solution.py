from itertools import combinations

class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)
        for i in range(n+1):
            for comb in combinations(nums, i):
                xor = 0
                for itm in comb:
                    xor ^= itm
                res += xor
        return res
        
