# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        values = self.get(root)
        #print(values)
        return max([max(item) - min(item) for item in values])
            
    def get(self,root):
        values = []
        def dfs(root,path):
            if root == None:
                return 

            else:
                path = path+[root.val]
                dfs(root.left,path)
                if root.left == None and root.right == None:
                    values.append(path)
                dfs(root.right,path)
        dfs(root,[])
        return values