import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())
cnt = 0
s, e = 0, n-1

while s < e:
    temp = a[s] + a[e]
    if temp == x:
        cnt += 1
        s += 1
    elif temp > x:
        e -= 1
    else:
        s += 1

print(cnt)