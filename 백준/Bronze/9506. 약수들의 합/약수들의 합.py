import sys
input = sys.stdin.readline

n = int(input())
while n != -1 :
    ans = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            ans.append(i)
    
    if sum(ans) == n:
        print(n, " = ", " + ".join(str(i) for i in ans), sep="")
    else:
        print(n, "is NOT perfect.")
        
    n = int(input())