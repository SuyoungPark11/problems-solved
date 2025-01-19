import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

counts = Counter(numbers)

for t in targets:
    if t in counts:
        print(counts[t], end= ' ')
    else:
        print(0, end= ' ')
    