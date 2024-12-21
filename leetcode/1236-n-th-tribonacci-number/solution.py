class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0 :
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else: 
            t = [0] * (n+1)
            t[1], t[2] = 1, 1
            for i in range(3, n+1): 
                t[i] = t[i-3] + t[i-2] + t[i-1]

            return t[n]
        
