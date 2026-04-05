class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.pq = nums
        
    def add(self, val: int) -> int:
        heapq.heappush(self.pq, val)
        while len(self.pq) > self.k:
            heapq.heappop(self.pq)
        print(self.pq)
        return self.pq[0]
