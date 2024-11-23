N, K  = map(int, input().split())
lst = [0]
for i in range(1, (N)+1):
    if N % i == 0:
        lst.append(i)

if len(lst) > K:
    print(lst[K])
else:
    print(0)