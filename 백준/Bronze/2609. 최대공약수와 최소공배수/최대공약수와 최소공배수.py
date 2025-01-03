def gcd(a, b):
    while b>0:
        a, b = b, a % b
    return a   

x, y = map(int, input().split())
g = gcd(x, y)
print(g)
print(x * y // g)