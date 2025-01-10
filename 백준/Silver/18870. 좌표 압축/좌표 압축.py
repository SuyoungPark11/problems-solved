import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().rstrip().split()))
sorted_X = sorted(list(set(X)))
cnt = {sorted_X[i]: i for i in range(len(sorted_X))}
print(*[cnt[x] for x in X])