"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root):
            if root == None:
                return 
            ans.append(root.val)
            children = root.children
            for child in children:
                dfs(child)
        ans = []
        dfs(root)
        return ans 
        