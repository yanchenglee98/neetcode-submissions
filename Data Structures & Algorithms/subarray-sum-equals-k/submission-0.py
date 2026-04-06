class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        currSum = 0
        res = 0
        for i, n in enumerate(nums):
            currSum+=n
            if (currSum-k) in hm:
                res += hm[currSum-k]
            hm[currSum] = hm.get(currSum, 0) + 1
        return res
        