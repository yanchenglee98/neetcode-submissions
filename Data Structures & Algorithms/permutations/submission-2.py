# hint
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        s = set()
        n = len(nums)
        def dfs(i):
            if i == n:
                res.append(subset[:])
                return 
            if i > n:
                return 
            for j in range(n):
                if nums[j] in s: continue
                s.add(nums[j])
                subset.append(nums[j])
                dfs(i+1)
                subset.pop()
                s.remove(nums[j])
        dfs(0)
        return res