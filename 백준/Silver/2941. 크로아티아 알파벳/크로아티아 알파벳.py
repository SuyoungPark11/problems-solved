import sys
input = sys.stdin.readline

croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().strip()
for i in croatian:
    word = word.replace(i, ' ')

print(len(word))