# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root,value):
            if root == None:
                return []
            if root.left:
                dfs(root.left,value +"->"+ str(root.left.val))
            if root.left == None and root.right == None:
                ans.append(value)
            if root.right:
                dfs(root.right,value+"->"+str(root.right.val))
            
        dfs(root,str(root.val))
        return ans