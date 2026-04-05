# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        depth = 0
        while stack:
            node, lv = stack.pop()
            if node:
                depth = max(depth, lv)
                stack.append((node.left, lv+1))
                stack.append((node.right, lv+1))
        return depth 
