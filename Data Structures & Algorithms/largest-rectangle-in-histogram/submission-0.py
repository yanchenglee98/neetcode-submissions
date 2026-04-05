class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        mx = 0
        for i in range(n):
            for j in range(i, n):
                area = min(heights[i:j+1]) * (j+1-i)
                mx = max(area, mx)
        return mx