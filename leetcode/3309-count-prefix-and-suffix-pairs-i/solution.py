class Solution(object):
    def isPrefixAndSuffix(self, str1, str2):
        n1, n2 = len(str1), len(str2)
        if n1 > n2:
            return False
        return str2[:n1] == str1 and str2[-n1:] == str1

    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        cnt = 0    
        for i in range(n):
            for j in range(i+1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    cnt += 1
        return cnt
        
        
