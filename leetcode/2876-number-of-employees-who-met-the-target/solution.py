class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        cnt = 0
        for h in hours:
            if h >= target:
                cnt += 1
        return cnt
        
