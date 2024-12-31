def backtrack(queen_position):
    if len(queen_position) == N:
        solutions.append(queen_position[:])
        return
    
    for col in range(N):
        if validation(queen_position, len(queen_position), col):
            queen_position.append(col)
            backtrack(queen_position)
            queen_position.pop()
      
    
def validation(queen_position, row, col):
    for r, c in enumerate(queen_position):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


N = int(input())
solutions = []
backtrack([])
print(len(solutions))