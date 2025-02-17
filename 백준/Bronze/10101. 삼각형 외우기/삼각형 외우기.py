import sys
input = sys.stdin.readline

angles = [int(input()) for _ in range(3)]
temp = sum(angles)

if temp != 180:
    print("Error")
else:
    if angles[0] == 60 and angles[1] == 60 and angles[2] == 60:
        print("Equilateral")
    elif (angles[0] != angles[1]) \
        and (angles[0] != angles[2]) \
        and (angles[1] != angles[2]):
        print("Scalene")
    else:
        print("Isosceles")    