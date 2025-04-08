"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root,depth):
            if root == None:
                return 
            
            ans.append(depth+1)
            children = root.children
            for i in range(0,len(children)):
                dfs(children[i],depth+1)
        ans = []
        dfs(root,0)
        #print(ans)
        if len(ans):
            return max(ans)
        return 0 