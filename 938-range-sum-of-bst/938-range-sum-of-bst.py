# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.tot = 0
        def dfs(root):
            if root.val >= low and root.val <= high:
                self.tot += root.val
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            return self.tot
        return dfs(root)
                
            
  
        