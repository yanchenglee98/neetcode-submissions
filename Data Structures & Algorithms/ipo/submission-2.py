# solution
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCapital = []
        maxProfit = []
        n = len(profits)
        for i in range(n):
            heapq.heappush(minCapital, (capital[i], i))
        
        while k:
            while minCapital and minCapital[0][0] <= w:
                c, i = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, (-profits[i], i))
            if not maxProfit: return w
            p, i = heapq.heappop(maxProfit)
            w-=p
            k-=1
        return w