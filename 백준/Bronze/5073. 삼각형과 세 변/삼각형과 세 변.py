import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
while a != 0 and b != 0 and c != 0:
    valid = max([a, b, c]) < (sum([a, b, c]) - max([a, b, c]))
    if valid:
        if a == b and b == c:
            print("Equilateral")
        elif a != b and a != c and b != c:
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Invalid") 
        
    a, b, c = map(int, input().split())
