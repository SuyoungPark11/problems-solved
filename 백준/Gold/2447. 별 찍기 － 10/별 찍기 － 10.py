import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
N = int(input().rstrip())

def append_star(length):
    if length == 1:
        return ['*']
    
    stars = append_star(length//3)
    result = []

    for star in stars:
        result.append(star*3)

    for star in stars:
        result.append(star + ' '*(length//3) + star)
    
    for star in stars:
        result.append(star*3)
    return result

print('\n'.join(append_star(N)))