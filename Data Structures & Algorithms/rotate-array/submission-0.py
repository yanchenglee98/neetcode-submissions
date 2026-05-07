class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = k
        copy = nums.copy()
        for l in range(len(nums)):
            nums[r % len(nums)] = copy[l]
            r+=1
         