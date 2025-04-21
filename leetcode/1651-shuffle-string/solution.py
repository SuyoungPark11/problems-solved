class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = ["X"] * len(indices)
        for i, idx in enumerate(indices):
            ans[idx] = s[i]
        return "".join(ans)

        
