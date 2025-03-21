class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num = [i for i in range(1, n+1)]
        num1 = sum([n for n in num if n % m != 0])
        num2 = sum([n for n in num if n % m == 0])
        return num1 - num2

