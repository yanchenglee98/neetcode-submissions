class Solution:
    def numSquares(self, n: int) -> int:
        dp = [1e99 for _ in range(n+1)]
        dp[0] = 0
        for i in range(1,n+1):
            for j in range(math.floor(i ** 0.5)+1):
                dp[i] = min(1+dp[i-(j**2)], dp[i])
        return dp[-1]