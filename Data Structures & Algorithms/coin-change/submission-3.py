
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hm = {}        
        def dfs(total):
            if total == 0:
                return 0
            if total in hm: return hm[total]
            res = float('inf')
            for c in coins:
                if c <= total:
                    res = min(res, 1+dfs(total-c))
            hm[total] = res
            return res
        ans = dfs(amount)
        return ans if ans != float('inf') else -1