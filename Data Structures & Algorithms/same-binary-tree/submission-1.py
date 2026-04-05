# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = [p], [q]
        while q1 and q2:
            if len(q1) != len(q2): return False
            tq1, tq2= [],[]
            for i in range(len(q1)):
                n1,n2 = q1[i], q2[i]
                if not n1 and not n2: continue
                if not n1 or not n2 or n1.val != n2.val: return False
                tq1.append(n1.left)
                tq1.append(n1.right)
                tq2.append(n2.left)
                tq2.append(n2.right)
            q1, q2 = tq1, tq2
        return True
        