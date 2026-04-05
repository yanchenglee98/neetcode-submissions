class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        res = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == -1 or grid[r][c] == 0:
                return 0
            t = 1
            grid[r][c] = -1
            for x,y in direction:
                t += (dfs(r+x, c+y))
            return t
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    size = dfs(r,c)
                    res = max(size, res)
        return res