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
        queue = [root]
        while queue:
            temp = []
            res.append(queue[-1].val)
            for n in queue:
                if n.left: temp.append(n.left)
                if n.right: temp.append(n.right)
            queue = temp
        return res

        