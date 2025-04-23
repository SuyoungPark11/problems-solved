from collections import defaultdict, Counter

class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = [0] * (9 * 4 +1)
        for i in range(1, n+1):
            number = str(i)
            sum_digit = sum([int(j) for j in number])
            cnt[sum_digit] += 1
            
        return cnt.count(max(cnt))
        
