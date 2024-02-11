"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        
        def dfs(root):
            if root == None:
                return []
            else:
                result.append(root.val)
                children = list(root.children)
                for child in children:
                    dfs(child)
            return result
        return dfs(root)