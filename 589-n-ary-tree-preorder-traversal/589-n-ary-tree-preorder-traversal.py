"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result =[]
        def PreOrderTraversal(node):
            if node == None:
                return None
            result.append(node.val)
            for next_node in node.children:
                PreOrderTraversal(next_node)
        PreOrderTraversal(root)
        return result
        