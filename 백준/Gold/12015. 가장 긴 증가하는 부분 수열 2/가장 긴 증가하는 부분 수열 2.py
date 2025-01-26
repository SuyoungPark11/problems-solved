import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

seq = []
for i in range(len(A)):
    pos = bisect.bisect_left(seq, A[i])
    if pos == len(seq):
        seq.append(A[i])
    else:
        seq[pos] = A[i]

print(len(seq))