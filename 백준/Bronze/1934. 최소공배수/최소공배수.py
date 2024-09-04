import sys

def gcd(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    elif (x >= y) and (y != 0):
        return gcd(y, x % y)
    elif (x < y) and (x != 0):
        return gcd(x, y % x) 

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = (a * b) / gcd(a,b)
    print(str(int(result)))