# solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        hm = {}
        def dfs(i):
            if i in hm:
                return hm[i]
            res = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    # include
                    res = max(res, 1+dfs(j))
            hm[i]=res
            return res
        return max(dfs(i) for i in range(len(nums)))