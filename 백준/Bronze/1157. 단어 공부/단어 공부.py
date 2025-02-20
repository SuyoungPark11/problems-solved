import sys
from collections import Counter
input = sys.stdin.readline

word = input().rstrip().lower()
word_count = Counter(word)
max_count = max(word_count.values())
max_word = []
for key, value in word_count.items():
    if value == max_count:
        max_word.append(key)
if len(max_word) == 1:
    print(max_word[0].upper())
else:
    print('?')