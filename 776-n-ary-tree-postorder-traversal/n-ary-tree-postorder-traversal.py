"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # explore left, right, node 
        result = []
        def dfs(root):
            if root  == None:
                return []
            else:
                childrens = root.children
                for child in childrens:
                    dfs(child)
                result.append(root.val)
            return result
        return dfs(root)