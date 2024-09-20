import sys
input = sys.stdin.readline

words = []
for _ in range(5):
    word = input().rstrip()
    words.append(word)

for i in range(15): 
  for j in range(5): 
    if i < len(words[j]):
      print(words[j][i], end="")