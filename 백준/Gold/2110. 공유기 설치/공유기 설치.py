import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

left, right = 1, house[-1] - house[0]

while left <= right:
    mid = (left + right) // 2
    cnt = 1
    curr = house[0]

    for h in house:
        if h >= curr + mid:
            cnt += 1
            curr = h

    if cnt >= C:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(result)