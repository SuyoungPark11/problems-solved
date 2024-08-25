import sys

n, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

sorted_A = sorted(A)

print(sorted_A[k-1])