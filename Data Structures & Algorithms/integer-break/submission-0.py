# editorial
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for nums in range(1, n+1):
            # we must break when nums == n
            # if nums < n we dont need to break so dp[nums] max product can be just itself
            dp[nums] = 0 if nums == n else nums
            for i in range(1, nums):
                dp[nums] = max(dp[nums], dp[i] * dp[nums-i])
        return dp[-1]