import sys
input = sys.stdin.readline
x, y, w, h = map(int, input().split())
result = []
if x >= (w-x):
    result.append(w-x)
else:
    result.append(x)
if y >= (h-y):
    result.append(h-y)
else:
    result.append(y)
print(min(result))    