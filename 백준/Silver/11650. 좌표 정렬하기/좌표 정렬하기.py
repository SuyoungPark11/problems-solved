import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append([x, y])
lst.sort()
for itm in lst:
    print(itm[0], itm[1])