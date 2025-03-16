class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt_r = 0
        cnt_l = 0
        ans = 0

        for i in s:
            if i == 'R':
                cnt_r += 1
            else:
                cnt_l += 1

            if cnt_r == cnt_l:
                ans += 1

        return ans 
        
