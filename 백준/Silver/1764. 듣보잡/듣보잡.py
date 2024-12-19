import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_set = set([input().rstrip() for _ in range(n)]) 
m_set = set([input().rstrip() for _ in range(m)])
answer = sorted(list(n_set & m_set))
print(len(answer))
for itm in answer:
    print(itm)