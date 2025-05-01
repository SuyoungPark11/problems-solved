class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        def add_func(words):
            res = ''
            for word in words:
                res += word
            return res
            
        ans1 = add_func(word1)
        ans2 = add_func(word2)
        return ans1 == ans2
        
