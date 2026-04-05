class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        high = 0
        prefix = [0 for _ in range(n)]
        for i, h in enumerate(height):
            high = max(h, high)
            prefix[i] = high
        high = 0
        suffix = [0 for _ in range(n)]
        for i, h in reversed(list(enumerate(height))):
            high = max(h, high)
            suffix[i] = high
        res = 0
        for i, v in enumerate(height):
            res += min(suffix[i], prefix[i]) - v
        return res

        