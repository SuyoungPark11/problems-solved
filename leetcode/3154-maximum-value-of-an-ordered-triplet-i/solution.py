class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, mx_diff, mx = 0, 0, 0
        for num in nums:
            ans = max(ans, mx_diff * num)
            mx_diff = max(mx_diff, mx - num)
            mx = max(mx, num)
        return ans
