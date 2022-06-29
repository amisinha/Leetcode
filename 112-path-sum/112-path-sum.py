# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def checkSum(node, currSum):
            if not node:
                return False
            currSum += node.val
            if not node.left and not node.right:
                return currSum == targetSum
            return checkSum(node.left,currSum) or checkSum(node.right, currSum)
        return checkSum(root,0)
        
            
        