# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        def dfs(node, lv):
            nonlocal depth 
            if not node:
                depth = max(depth, lv)
                return
            dfs(node.left, lv+1)
            dfs(node.right, lv+1)
        dfs(root, 0)
        return depth