class Solution:
    def mySqrt(self, x: int) -> int:
        if x > 1:
            for i in range(x):
                if i ** 2 < x and (i+1) ** 2 > x:
                    return i
                elif i ** 2 == x:
                    return i
        else:
            return 0

        