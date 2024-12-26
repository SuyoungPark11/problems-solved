class Solution:
    def getLucky(self, s: str, k: int) -> int:
        step1 = ''.join(str(ord(a)-96) for a in list(s))
        num = int(step1)
        for _ in range(k):
            num = self.transform(num)
        return num

    def transform(self, num):
        return sum(int(digit) for digit in str(num))      
