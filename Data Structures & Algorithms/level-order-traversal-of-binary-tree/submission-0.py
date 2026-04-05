# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = [root]
        val = [root.val]
        res = []
        while q:
            res.append(val)
            temp = []
            temp2 = []
            for n in q:
                if n.left: 
                    temp.append(n.left)
                    temp2.append(n.left.val)
                if n.right: 
                    temp.append(n.right)
                    temp2.append(n.right.val)
            q = temp
            val = temp2
        return res

        