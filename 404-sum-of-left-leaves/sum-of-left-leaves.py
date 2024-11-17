class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = []
        
        def dfs(root):
            if root == None:
                return 
            dfs(root.left)
            if root.left != None and root.left.left == None and root.left.right == None:
                ans.append(root.left.val)
            if root.right:
                dfs(root.right)
        
        dfs(root)
        return sum(ans)