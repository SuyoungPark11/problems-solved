import sys
input = sys.stdin.readline
mii = lambda : map(int, input().split())

N, M, K = mii()

size = 1
while size < N:
    size <<= 1
tree = [0] * (2 * size)
size -= 1

def update(idx, diff):
    idx += size
    while idx:
        tree[idx] += diff
        idx //= 2

for i in range(1, N + 1):
    num = int(input())
    update(i, num)

def query(left, right):
    left += size
    right += size 
    ans = 0
    while left <= right:
        if left % 2 == 1:
            ans += tree[left]
            left += 1
        left //= 2

        if right % 2 == 0:
            ans += tree[right]
            right -= 1
        right //= 2

    return ans

for _ in range(M + K):
    a, b, c = mii()
    if a == 1:
        update(b, c - tree[b + size])
    elif a == 2:
        print(query(b, c))
