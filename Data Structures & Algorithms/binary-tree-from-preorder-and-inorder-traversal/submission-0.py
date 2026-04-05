# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(val=inorder[0])
        i = inorder.index(preorder[0])
        left = self.buildTree(preorder[1:i], inorder[:i]) if i > 0 else None
        right = self.buildTree(preorder[i+1:], inorder[i+1:]) if i < len(preorder) else None
        root = TreeNode(preorder[0])
        root.left = left
        root.right = right
        return root