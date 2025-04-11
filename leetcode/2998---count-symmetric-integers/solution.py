class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        def isSymmetric(num):
            if num >= 10 and num <= 99:
                return num // 10 == num % 10
            if num >= 1000 and num <= 9999:
                left = num // 100
                right = num % 100
                return left // 10 + left % 10 == right // 10 + right % 10
            return False
        return sum(isSymmetric(i) for i in range(low, high + 1))
        
