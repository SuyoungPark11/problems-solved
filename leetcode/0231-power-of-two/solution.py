class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1 :
            return False
        return n and not (n & n-1)
            
        
