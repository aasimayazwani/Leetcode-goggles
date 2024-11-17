class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import defaultdict
        level_val = defaultdict(list)
        def dfs(root,depth):
            if root == None:
                return 
            dfs(root.left,depth+1)
            cur = root.val
            level_val[depth].append(cur)
            dfs(root.right,depth+1)
        dfs(root,0)
        res = level_val.items()
        return sorted(res,key=lambda x:x[0],reverse=True)[0][1][0]
