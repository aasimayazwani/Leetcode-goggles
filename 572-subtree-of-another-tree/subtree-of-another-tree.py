# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            candidates = []
            for i in range(0,len(stack)):
                node = stack[i]
                if self.check(node) == self.check(subRoot):
                    return True
                if node.left:
                    candidates.append(node.left)
                if node.right:
                    candidates.append(node.right)

            if len(candidates) > 0:
                stack = candidates
            else:
                return False 

    def check(self,root):
        ans = []
        def dfs(root):
            if root == None:
                ans.append("missing")
                return None 
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans