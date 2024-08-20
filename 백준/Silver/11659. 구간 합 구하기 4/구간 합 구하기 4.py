import sys

input = sys.stdin.readline
suNo,quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prifix_sum = [0]
temp = 0
for i in numbers:
    temp = temp + i
    prifix_sum.append(temp) 
for i in range(quizNo):
    s, e = map(int, input().split())
    print(prifix_sum[e]-prifix_sum[s-1]) 