A, B, C = map(int, input().split())
li = [
    (A+B)%C,
    ((A%C) + (B%C))%C,
    (A*B)%C,
    ((A%C) * (B%C))%C
]
for itm in li:
    print(itm)