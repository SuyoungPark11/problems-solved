import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        floor, room = h, n // h
    else:
        floor, room = n % h, n // h + 1
    print(str(floor * 100 + room))