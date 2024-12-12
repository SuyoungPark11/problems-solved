import sys
input = sys.stdin.readline

a, b = -1, -1

while True:
    try:
        a,b = map(int,input().split())
    except:
        break
    print(a+b)
    