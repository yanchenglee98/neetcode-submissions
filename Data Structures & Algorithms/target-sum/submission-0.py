class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)
        def dfs(i, total):
            nonlocal res 
            if i >= n:
                if total == target:
                    res+=1
                return
            # add
            dfs(i+1, total + nums[i])
            # subtract
            dfs(i+1, total - nums[i])
        dfs(0,0)
        return res