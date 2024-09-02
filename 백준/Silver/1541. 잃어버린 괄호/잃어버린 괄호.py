import sys

input = sys.stdin.readline
a = input().split('-')
b = [itm.split('+') for itm in a]
result = 0
for i in range(len(b)):
    if i != 0 :
        result -= sum(list(map(int, b[i])))
    else:
        result += sum(list(map(int, b[i])))

print(result)