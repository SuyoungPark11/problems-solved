class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        D = [[0] * (r+1) for r in range(numRows)]
        for itm in D:
            itm[0] = 1
            itm[-1] = 1
        for i in range(2, numRows):
            for j in range(1, i):
                D[i][j] = D[i-1][j-1] + D[i-1][j]
        return D
        