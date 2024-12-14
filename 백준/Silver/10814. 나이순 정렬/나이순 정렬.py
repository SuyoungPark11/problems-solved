import sys
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    age, name = input().split()
    lst.append([int(age), name])
    
lst = sorted(lst, key=lambda x : x[0])
for i in range(n):
    print(lst[i][0], lst[i][1])