class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for n in nums:
            hm[n]+=1
        hm = sorted(hm.items(), key=lambda items: items[1], reverse=True)
        return list(map(lambda x: x[0], hm[:k]))