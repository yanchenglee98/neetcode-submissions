class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = []
        res = []
        s = set()
        def dfs(i):
            if i == n:
                res.append(subset[:])
                return 
            if i > n:
                return 
            for j in range(n):
                if nums[j] in s: continue
                subset.append(nums[j])
                s.add(nums[j])
                dfs(i+1)
                subset.pop()
                s.remove(nums[j])
        dfs(0)
        return res
                
        