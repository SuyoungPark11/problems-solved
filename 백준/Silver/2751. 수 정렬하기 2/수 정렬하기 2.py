import sys

n = int(sys.stdin.readline())
lst = [0] * n

for i in range(n):
    lst[i] = int(sys.stdin.readline())

sorted_lst = sorted(lst)

for i in range(n):
    sys.stdout.write(str(sorted_lst[i]) + '\n')