import sys

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

input = sys.stdin.readline
a, b = map(int, input().split())
result = gcd(a, b)
print('1' * result)