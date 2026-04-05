# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0: return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(preorder[0])
        rootIdx = inorder.index(root.val)
        left = self.buildTree(preorder[1:rootIdx], inorder[:rootIdx]) if rootIdx < len(inorder) else None
        right = self.buildTree(preorder[rootIdx+1:], inorder[rootIdx+1:]) if rootIdx + 1 < len(inorder) else None
        root.left = left
        root.right = right
        return root