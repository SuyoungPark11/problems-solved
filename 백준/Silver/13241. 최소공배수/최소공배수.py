import sys
input = sys.stdin.readline

def gcd(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    elif (x >= y) and (y != 0):
        return gcd(y, x % y)
    elif (x < y) and (x != 0):
        return gcd(x, y % x) 

A, B = map(int, input().split())

gcd_val = gcd(A, B)
lcm_val = A * B // gcd_val
print(lcm_val)