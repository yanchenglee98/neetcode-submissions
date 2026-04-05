import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = math.inf
        p = 0
        for i in prices:
            if i < l:
                l = i
            else:
                p = max(p, i - l)
        return p