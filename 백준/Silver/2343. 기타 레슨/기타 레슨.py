import sys

input = sys.stdin.readline
n, m = map(int, input().split())
lessons = list(map(int, input().split()))

start = 0
end = n-1

for itm in lessons:
    if start < itm: start = itm
    end += itm 

while start <= end:
    mid_ind = (start + end) // 2
    sum = 0
    count = 0
    for i in range(n):
        if (sum + lessons[i]) > mid_ind:
            count += 1
            sum = 0
        sum += lessons[i]

    if sum != 0: count +=1
    if count > m: 
        start = mid_ind + 1
    else: 
        end = mid_ind - 1

print(str(start))