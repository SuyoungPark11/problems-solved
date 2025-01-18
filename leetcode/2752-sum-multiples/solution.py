class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum([i for i in range(1, n+1) if (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0)])
        
