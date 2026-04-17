class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0]== 1: return 0
        dp[0][0] = 1 
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                elif r == 0 or c == 0:
                    if obstacleGrid[r][c] != 1:
                        if r > 0:
                            dp[r][c] = dp[r-1][c]
                        elif c > 0:
                            dp[r][c] = dp[r][c-1]
                else:
                    if obstacleGrid[r][c] != 1:
                        dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1] 