class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            n = nums[i]
            goal = target - n
            if goal in hm:
                return [hm[goal], i]
            hm[n] = i
        return [-1,-1]
        