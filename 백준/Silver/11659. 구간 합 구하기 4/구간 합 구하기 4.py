import sys

suNo,quizNo = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
prifix_sum = [0]
temp = 0
for i in numbers:
    temp = temp + i
    prifix_sum.append(temp) 
for i in range(quizNo):
    s, e = map(int, sys.stdin.readline().split())
    print(prifix_sum[e]-prifix_sum[s-1]) 