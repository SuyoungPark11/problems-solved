import sys
input = sys.stdin.readline

T = int(input())
answer = []
for _ in range(T):
    a, b = map(int, input().split())
    b %= 4
    if b % 4 == 0:
        b = 4
    s = a ** b
    if s % 10 == 0:
        answer.append(10)
    else:
        answer.append(s % 10)

for a in answer:
    print(a)