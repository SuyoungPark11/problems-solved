class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]

        carry = 0
        result = ""

        for i in range(max(len(num1), len(num2))):
            digit1 = int(num1[i]) if i < len(num1) else 0
            digit2 = int(num2[i]) if i < len(num2) else 0
            sum_of_digits = digit1 + digit2 + carry
            carry, digit = divmod(sum_of_digits, 10)
            result += str(digit)

        if carry:
            result += str(carry)

        return result[::-1]
            
