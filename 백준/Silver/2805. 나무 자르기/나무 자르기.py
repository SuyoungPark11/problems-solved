import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 0, max(trees)

while left <= right:
    mid = (left + right) // 2
    take = 0

    for tree in trees:
        if tree > mid:
            take += tree - mid

    if take >= M:
        left = mid + 1
    else:
        right = mid - 1
        
print(right)