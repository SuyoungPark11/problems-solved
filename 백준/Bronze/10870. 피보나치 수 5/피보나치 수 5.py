n = int(input())

def fibonacci(x):
    if x >= 2:
        return fibonacci(x-1) + fibonacci(x-2)
    elif x == 1:
        return 1
    elif x == 0:
        return 0
    
print(fibonacci(n))