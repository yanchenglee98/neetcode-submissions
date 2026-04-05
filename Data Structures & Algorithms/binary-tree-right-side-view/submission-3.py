# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        q = [root]
        while q:
            res.append(q[-1].val)
            ls = []
            for n in q:
                if n.left: ls.append(n.left)
                if n.right: ls.append(n.right)
            q = ls
        return res

