A = [i for i in range(1, 31)]
for _ in range(28):
    A.remove(int(input()))
    
print(min(A))
print(max(A))