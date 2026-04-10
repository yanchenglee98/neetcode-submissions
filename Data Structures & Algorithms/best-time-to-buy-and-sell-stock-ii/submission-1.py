# solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hm = {}
        def dfs(i, bought):
            if i >= len(prices):
                return 0
            if (i, bought) in hm:
                return hm[(i, bought)]
            # skip
            res = dfs(i+1, bought)
            if bought:
                # sell
                res = max(res, prices[i] + dfs(i+1, False))
            else:
                # buy
                res = max(res, -prices[i] + dfs(i+1, True))
            hm[(i, bought)] = res
            return res
        return dfs(0, False)