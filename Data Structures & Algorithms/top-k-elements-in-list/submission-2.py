class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        hm = defaultdict(int)
        for i, n in enumerate(nums):
            hm[n] += 1
        for key , v in hm.items():
            heapq.heappush(pq, (v, key))
            while len(pq) > k:
                heapq.heappop(pq)
        return [key for v, key in pq]