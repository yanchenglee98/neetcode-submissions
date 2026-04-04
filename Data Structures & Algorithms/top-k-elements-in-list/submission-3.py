class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        arr = [[] for _ in range(n+1)]
        count = Counter(nums)
        for key, val in count.items():
            arr[val].append(key)
        
        res = []
        i = n
        while len(res) < k:
            res.extend(arr[i])
            i-=1
        return res