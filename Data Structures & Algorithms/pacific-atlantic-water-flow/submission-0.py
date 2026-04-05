# hint from solution
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pac, atl = set(), set()
        DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(r, c, visited, prevHeight):
            if r<0 or r>=n or c<0 or c>=m or (r,c) in visited or heights[r][c] < prevHeight:
                return 
            visited.add((r,c))
            for x, y in DIR:
                dfs(r+x,c+y, visited, heights[r][c])
        
        for col in range(m):
            dfs(0, col, pac, 0)
            dfs(n-1, col, atl, 0)
        
        for row in range(n):
            dfs(row, 0, pac, 0)
            dfs(row, m-1, atl, 0)
        
        res = []
        for r in range(n):
            for c in range(m):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res