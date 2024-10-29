import sys
input = sys.stdin.readline
lst = [int(input()) for _ in range(9)]
    
max_num = max(lst)
max_idx = lst.index(max_num)
print(max_num)
print(max_idx+1)