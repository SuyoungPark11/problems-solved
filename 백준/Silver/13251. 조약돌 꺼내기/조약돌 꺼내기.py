import math

def same_color_probability(M, stones, K):
    # 전체 조약돌 수 (N)
    total_stones = sum(stones)
    
    # 전체에서 K개를 뽑는 경우의 수
    total_combinations = math.comb(total_stones, K)
    
    # 같은 색상에서 K개를 뽑는 경우의 수를 합산
    favorable_combinations = 0
    for stone_count in stones:
        if stone_count >= K:
            favorable_combinations += math.comb(stone_count, K)
    
    # 확률 계산: favorable_combinations / total_combinations
    probability = favorable_combinations / total_combinations
    return probability

# 입력 받기
M = int(input())  # 색상의 종류 M
stones = list(map(int, input().split())) 
K = int(input())  


result = same_color_probability(M, stones, K)
print(f"{result:.10f}")