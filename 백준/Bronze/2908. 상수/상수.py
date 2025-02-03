a, b = input().split()
ra, rb = a[::-1], b[::-1]
ans = max(int(ra), int(rb))
print(ans)