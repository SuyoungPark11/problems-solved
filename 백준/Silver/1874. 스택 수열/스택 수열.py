import sys

n = int(sys.stdin.readline())  
A = []  
stack = []  
m = 1  
output = []

for _ in range(n):
    A.append(int(sys.stdin.readline()))

valid = True  # 수열을 만들 수 있는지 여부를 나타내는 변수

for i in range(n):
    if A[i] >= m:
        while A[i] >= m:
            stack.append(m)
            output.append('+')
            m += 1
        stack.pop()
        output.append('-')
    else:
        if stack.pop() != A[i]:
            valid = False
            break
        output.append('-')

if valid:
    sys.stdout.write("\n".join(output) + "\n")
else:
    sys.stdout.write("NO\n")
