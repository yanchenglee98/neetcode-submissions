# chatgpt
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        s = set()
        n = len(nums)
        nums.sort()
        def dfs(i):
            if i == n:
                res.append(path[:])
            if i >= n:
                return
            for j in range(n):
                if j > 0 and nums[j] == nums[j-1] and j-1 not in s: continue
                if j in s: continue
                # include
                path.append(nums[j])
                s.add(j)
                dfs(i+1)
                # backtrack
                path.pop()
                s.remove(j)
        dfs(0)
        return res