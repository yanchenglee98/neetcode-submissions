class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        dp1 = [0 for _ in range(n-1)]
        dp1[0] = nums[0]
        dp1[1]= max(nums[:2])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        
        dp2 = [0 for _ in range(n-1)]
        dp2[0] = nums[1]
        dp2[1]= max(nums[1:3])
        for i in range(2, n-1):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i+1])
        print(dp1, dp2)
        return max(dp2[-1], dp1[-1])