class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')' : '(',
            '}' : '{',
            ']' : '[' 
        }
        stack = []
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if stack[-1] != d[i]:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False 