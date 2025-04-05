class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([(123 - ord(a)) * (i + 1) for i, a in enumerate(s)]) 
