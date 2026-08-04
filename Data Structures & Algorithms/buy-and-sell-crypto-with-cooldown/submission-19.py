from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache
        def dfs(i, hold):
            if i >= len(prices):
                return 0
            if hold:
                # sell
                sell = prices[i] + dfs(i+2, False)
                # dont sell
                dont = dfs(i+1, hold)
                return max(sell, dont)
            else:
                # buy
                buy = -prices[i] + dfs(i+1, True)
                # skip
                skip = dfs(i+1, hold)
                return max(buy, skip)
        return dfs(0, False)
