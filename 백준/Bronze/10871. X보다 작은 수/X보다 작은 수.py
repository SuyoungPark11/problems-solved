import sys
input = sys.stdin.readline

N, X = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
for itm in lst:
    if itm < X:
        ans.append(itm)

for itm in ans:
    print(itm, end = ' ')