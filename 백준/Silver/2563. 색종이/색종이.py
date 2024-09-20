import sys
input = sys.stdin.readline

n = int(input())
white = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            if white[j][i] == 0:
                white[j][i] = 1
            else:
                pass

sum_array = 0
for i in range(100):
    sum_array += sum(white[i])
print(sum_array)