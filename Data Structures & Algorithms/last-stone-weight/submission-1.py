class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = -1*heapq.heappop(stones)
            s2 = -1*heapq.heappop(stones)
            heapq.heappush(stones, -abs(s1-s2))
        return -stones[0]
        