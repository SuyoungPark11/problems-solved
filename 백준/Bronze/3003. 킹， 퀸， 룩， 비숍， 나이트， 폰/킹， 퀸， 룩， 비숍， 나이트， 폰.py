import sys
input = sys.stdin.readline

chs = [1, 1, 2, 2, 2, 8]
hav = list(map(int, input().split()))

for i in range(len(chs)):
    print(chs[i] - hav[i], end=' ')