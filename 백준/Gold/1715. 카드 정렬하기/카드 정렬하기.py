import sys
from queue import PriorityQueue

input = sys.stdin.readline
n = int(input())
deck = PriorityQueue()

for i in range(n):
    deck.put(int(input())) 

result = 0

while deck.qsize() > 1:
    data1 = deck.get()
    data2 = deck.get()
    temp = data1 + data2
    result += temp
    deck.put(temp)

print(result)