# solution
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumStones = sum(stones)
        target = (sumStones+1)//2
        n = len(stones)
        hm = {}
        def dfs(i, total):
            if (i, total) in hm:
                return hm[(i, total)]
            if total >= target or i == n:
                return abs(total - (sumStones - total))
            res = min(dfs(i+1, total + stones[i]), dfs(i+1, total))
            hm[(i, total)] = res
            return res
        return dfs(0,0)