# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def bst(root):
            if root:
                result.append(root.val)
                if root.left:
                    bst(root.left)
                if root.right:
                    bst(root.right)
        bst(root)
        return result
        