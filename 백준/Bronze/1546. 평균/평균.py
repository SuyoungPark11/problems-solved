n = int(input())
scores = list(map(int, input().split(' ')))
new_scores = [score / max(scores) * 100 for score in scores]
print(sum(new_scores) / len(new_scores))