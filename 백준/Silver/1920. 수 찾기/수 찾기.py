import sys

input = sys.stdin.readline
n = int(input())
A = map(int, input().split())
m = int(input())
T = list(map(int, input().split()))
sorted_A = sorted(A)

for i in range(m):
    target = T[i]
    start = 0
    end = n-1
    sign = False
    while start <= end: 
        med_ind = (start + end) // 2
        med = sorted_A[med_ind]
        if med > target:
            end = med_ind - 1 
        elif med < target: 
            start = med_ind + 1
        else:
            sign = True
            break
    
    if sign is True:
        print('1')
    else:
        print('0')