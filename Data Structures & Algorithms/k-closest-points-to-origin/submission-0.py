class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        def dist(x1, y1, x2, y2):
            return ((x1-x2)**2 + (y1-y2)**2) ** (0.5)
        for x, y in points:
            heapq.heappush(pq, (-dist(x,y,0,0), (x,y)))
            while len(pq) > k:
                heapq.heappop(pq)
        return [p for _, p in pq]
        
        