class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        s = 0
        e = len(x)-1
        mid = len(x) // 2
        while s <= mid : 
            left, right = x[s], x[e]
            if left != right:
                return False
            else:
                s += 1
                e -= 1
        return True

        