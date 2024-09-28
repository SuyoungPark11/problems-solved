import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    
N, M = map(int, input().split())
trie = Trie()

for _ in range(N):
    word = input().strip()
    trie.insert(word)

result = 0
for _ in range(M):
    word = input().strip()
    if trie.search(word):
        result += 1

print(result)