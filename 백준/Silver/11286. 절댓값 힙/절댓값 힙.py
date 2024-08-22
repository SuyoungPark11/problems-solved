import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
queue = PriorityQueue()
result = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        queue.put((abs(x), x)) # 절대값을 기준으로 정렬하고 같으면 음수 우선 정렬?
    else:
        if queue.empty() == True:
            result.append("0")
        else:
            result.append(str(queue.get()[1])) # [1]은 왜 추가되는지 확인

sys.stdout.write("\n".join(result) + "\n")