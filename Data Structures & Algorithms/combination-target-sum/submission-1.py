class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if i >= len(nums) or total > target:
                return
            # add current index 
            curr+=[nums[i]]
            dfs(i,curr, total + nums[i])

            # skip current index
            curr.pop()
            dfs(i+1, curr, total)
        dfs(0, [], 0)
        return res