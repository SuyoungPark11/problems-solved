class Solution:
    def climbStairs(self, n: int) -> int:
        D = [0] * (n+1)
        D[1] = 1
        if n >= 3:
            D[2] = 2
            for i in range(3, n+1):
                D[i] = D[i-1] + D[i-2]
        elif n == 2:
            D[2] = 2  
        return D[n] 
        