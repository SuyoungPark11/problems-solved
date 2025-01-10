import sys
input = sys.stdin.readline

n = int(input())
company = {}
for i in range(n):
    name, status = input().split()
    if status == 'enter':
        company[name] = 1
    else:
        company.pop(name)

company = sorted(company.keys(), reverse=True)
for i in company:
    print(i)