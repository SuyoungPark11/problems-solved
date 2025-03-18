class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        while x > 0 or y > 0:
            ans += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1
        return ans
