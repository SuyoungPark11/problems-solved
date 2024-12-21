class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        if n >= 2:
            ans[1] = 1
            for i in range(2, n+1):
                ans[i] = ans[i // 2] + i % 2
        elif i == 1:
            ans[1] = 1
        return ans       

        