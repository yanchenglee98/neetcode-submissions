# help from solution
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pq = []
        trips.sort(key=lambda x: x[1])
        curr = 0
        for num, fro, to in trips:
            while pq and pq[0][0] <= fro:
                t, n = heapq.heappop(pq)
                curr-=n
            curr+=num
            if curr > capacity:
                return False
            heapq.heappush(pq,(to, num))
        return True