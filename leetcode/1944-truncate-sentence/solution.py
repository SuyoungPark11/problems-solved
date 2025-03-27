class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        words = s.split(" ")
        ans = words[0]
        for i in range(1, k):
            ans += " " + words[i]        
        return ans
