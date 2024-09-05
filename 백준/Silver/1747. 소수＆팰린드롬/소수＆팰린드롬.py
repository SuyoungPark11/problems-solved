import sys

def check(num):
    string = list(str(num))
    start = 0
    end = len(string)-1 
    while start < end:
        if  string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

input = sys.stdin.readline
n = int(input())
lst = [0] * (10000000 + 1)


for i in range(2, len(lst)):
    lst[i] = i

for i in range(2, int(len(lst)**0.5)+1):
    if lst[i] == 0:
        continue
    for j in range(i+i, len(lst), i):
        lst[j] = 0

ind = n
while True:
    if lst[ind] != 0:
        if check(lst[ind]):
            print(lst[ind])
            break
    ind += 1