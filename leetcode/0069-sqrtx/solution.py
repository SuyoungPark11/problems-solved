class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        if x <= 1:
            return x
        while low <= high:
            mid =  (low + high) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 < x:
                low = mid + 1
            else:
                high = mid - 1  
        
