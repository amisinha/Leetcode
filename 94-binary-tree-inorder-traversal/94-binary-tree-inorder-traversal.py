# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def bstI(root):
            if root:
                bstI(root.left)
                if root:
                    result.append(root.val)
                if root.right:
                    bstI(root.right)
        bstI(root)
        return result
        