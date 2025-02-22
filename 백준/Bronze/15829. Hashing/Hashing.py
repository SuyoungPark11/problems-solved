L = int(input())
string = input()
mod = 1234567891
hash_val = 0

for i in range(L):
    curr = ord(string[i]) - 96
    hash_val += curr * 31 ** i
    
print(hash_val % mod)