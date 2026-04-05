# hint from solution and chatgpt
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        DIR = [(1,0), (0,1), (-1,0),(0,-1)]
        m = len(grid)
        n = len(grid[0])
        INF = 2147483647
        visited = set()
        queue = []
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r,c))

        distance = 0
        while queue:
            ls = []
            for r, c in queue:
                if r<0 or r>=m or c<0 or c>=n or (r,c) in visited or grid[r][c] == -1:
                    continue
                visited.add((r,c))
                if grid[r][c] == INF:
                    grid[r][c] = distance
                for x, y in DIR:
                    ls.append((r+x, c+y))
            queue = ls
            distance+=1
        