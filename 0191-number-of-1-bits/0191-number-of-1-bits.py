class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 1:
            r = n % 2
            n = n // 2
            if r == 1: count +=1
        return count + 1
        