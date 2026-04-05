class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: continue # avoid dupe ans
            l = i+1
            r = len(nums)-1
            while l < r:
                total = a + nums[l] + nums[r]
                if total < 0:
                    l+=1
                elif total > 0:
                    r-=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r: # avoid dupe ans
                        l+=1
        return res
                
        return res