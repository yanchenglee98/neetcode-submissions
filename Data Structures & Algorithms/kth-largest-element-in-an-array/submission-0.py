class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, n)
            while len(pq) > k:
                heapq.heappop(pq)
        return pq[0]