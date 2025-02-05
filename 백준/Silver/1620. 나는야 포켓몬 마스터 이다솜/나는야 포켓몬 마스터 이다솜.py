import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon_int = dict()
pokemon_str = dict()
for i in range(N):
    pokemon = input().rstrip()
    pokemon_int[i] = pokemon
    pokemon_str[pokemon] = i

for _ in range(M):
    item = input().rstrip()
    if item.isdigit():
        print(pokemon_int[int(item)-1])
    else:
        print(pokemon_str[item]+1)