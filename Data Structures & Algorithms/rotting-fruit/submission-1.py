# hint
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        n = len(grid)
        m = len(grid[0])
        
        queue = []
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2:
                    queue.append((r,c))

        visited = set()

        level = 0
        while queue:
            ls = []
            for r,c in queue:
                for x, y in DIR:
                    nR, nC = r+x, c+y
                    if nR < 0 or nR >=n or nC<0 or nC>=m or grid[nR][nC] != 1:
                        continue
                    grid[nR][nC] = 2
                    ls.append((nR, nC))
            queue = ls
            if queue: level += 1
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    return -1
        return level
        