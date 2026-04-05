# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        stack = [(root, False)]
        depth = defaultdict(int)

        while stack:
            node, visited = stack.pop()
            if visited:
                left = depth[node.left]
                right = depth[node.right]
                if abs(left-right) > 1: return False
                depth[node] = 1+max(left, right)
            else:
                stack.append((node, True))
                if node.right: stack.append((node.right, False))
                if node.left: stack.append((node.left, False))
        return True