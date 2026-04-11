class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        majority = len(nums) / 3
        res = []
        for k, v in c.items():
            if v > majority:
                res.append(k)
        return res