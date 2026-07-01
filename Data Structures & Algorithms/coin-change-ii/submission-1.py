
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        hm = {}
        def dfs(i, total):
            if (i, total) in hm: return hm[(i, total)]
            if total == amount:
                return 1
            if i >= len(coins) or total > amount:
                return 0
            # pick 
            pick = dfs(i, total + coins[i])
            # skip
            skip = dfs(i+1, total)
            hm[(i,total)] = pick + skip
            return pick + skip
        return dfs(0, 0)
        