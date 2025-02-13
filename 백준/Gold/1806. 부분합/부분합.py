import sys
input = sys.stdin.readline

N, S = map(int, input().split())
a = list(map(int, input().split()))
s, e = 0, 0
temp = a[0]
ans = 100001

while True:
    if temp < S:
        e += 1
        if e == N: break
        temp += a[e]
    else:
        temp -= a[s]
        ans = min(ans, e - s + 1)
        s += 1

print(ans if ans != 100001 else 0)