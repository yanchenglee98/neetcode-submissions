class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2: return min(cost)
        dp = [0 for _ in range(len(cost)+1)]
        #[1,2,3]
        #[1,1,0]
        # dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        print(dp)
        return dp[-1]
        