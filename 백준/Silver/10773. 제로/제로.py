import sys
input = sys.stdin.readline

K = int(input())
lst = []
for _ in range(K):
    a = int(input())
    if a != 0:
        lst.append(a)
    else:
        lst.pop()
print(sum(lst))