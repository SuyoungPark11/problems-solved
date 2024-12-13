import sys 
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a and b:
        print(a + b)
    else:
        break