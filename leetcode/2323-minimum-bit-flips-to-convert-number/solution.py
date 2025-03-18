class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        ans = 0
        while start > 0 or goal > 0:
            ans += (start & 1) ^ (goal & 1)
            start >>= 1
            goal >>= 1
        return ans
        
