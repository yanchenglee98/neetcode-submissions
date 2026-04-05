class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        c = Counter(nums) # O(n)

        for key, v in c.items():
            heapq.heappush(heap, (-v, key))
        
        res = []
        while k and heap:
            val = heapq.heappop(heap)
            res.append(val[1])
            k-=1
        return res

