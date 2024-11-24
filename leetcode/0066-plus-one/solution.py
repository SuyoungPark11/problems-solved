class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        num = 0
        for i in range(length):
            num += digits[i] * (10 ** (length-1-i))
        return [int(i) for i in str(num+1)]


        
