class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return sum(abs(i - t.find(a)) for i, a in enumerate(s))
        
