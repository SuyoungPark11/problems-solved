import sys
input = sys.stdin.readline

result = []
lst = [int(input()) for _ in range(10)]
for itm in lst:
    remainder = itm % 42
    result.append(remainder)
    
result = set(result)
print(len(result))