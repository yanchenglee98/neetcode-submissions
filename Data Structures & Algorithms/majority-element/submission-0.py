class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        mx = 0
        val = 0
        for k, v in c.items():
            if v > mx:
                mx = v
                val = k
        return val