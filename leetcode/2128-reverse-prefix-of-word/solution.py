class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        pos = word.find(ch)
        return word[:pos+1][::-1] + word[pos+1:]
        
