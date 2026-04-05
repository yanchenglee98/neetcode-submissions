class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        res = 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == '#' or grid[r][c] == '0':
                return
            grid[r][c] = '#'
            for x,y in direction:
                dfs(r+x, c+y)
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1':
                    dfs(r,c)
                    res+=1
        return res
            
        