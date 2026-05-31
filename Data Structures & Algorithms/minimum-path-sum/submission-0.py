class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0: continue
                num = grid[i][j]
                up, left = float('inf'), float('inf')
                if i > 0:
                    up = grid[i-1][j] + num
                if j > 0:
                    left = grid[i][j-1] + num
                grid[i][j] = min(up, left)
        return grid[-1][-1]