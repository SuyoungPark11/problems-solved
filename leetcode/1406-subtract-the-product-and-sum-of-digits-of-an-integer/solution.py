class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = reduce(lambda x, y: x * y, [int(i) for i in str(n)])
        s = sum([int(i) for i in str(n)])
        return p - s
