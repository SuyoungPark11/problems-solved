import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
stack = []
NGE = [0] * n

for i in range(n):
    while stack and A[stack[-1]] < A[i] :
        NGE[stack.pop()] = A[i]
    stack.append(i)

while stack:
    NGE[stack.pop()] = -1

print(" ".join(list(map(str, NGE))))