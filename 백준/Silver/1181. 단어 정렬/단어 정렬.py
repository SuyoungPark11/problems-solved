import sys
input = sys.stdin.readline

N = int(input())
words = set(input().rstrip() for _ in range(N))
lst = list(words)
lst.sort()
lst.sort(key=len)

for itm in lst:
    print(itm)