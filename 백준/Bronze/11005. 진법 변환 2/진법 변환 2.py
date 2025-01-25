N, B = map(int, input().split())
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''
while N : 
    answer += number[N % B]
    N //= B

print(answer[::-1])