# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return None
            if p.val <= node.val <= q.val:
                return node
            if node.val > p.val and node.val > p.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        if q.val < p.val: p, q = q, p
        return dfs(root)