class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if i >= len(nums) or total > target:
                return
            for j in range(i, len(nums)):
                n = nums[j]
                if total + n > target:
                    return
                curr+=[n]
                dfs(j, curr, total+n)
                curr.pop()
        dfs(0, [], 0)
        return res