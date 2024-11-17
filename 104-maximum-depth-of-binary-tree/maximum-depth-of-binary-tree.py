class Solution:
    def maxDepth(self, root: Optional[TreeNode]):  
        ans = [0]

        def dfs(root,depth):
            if root == None:
                return 
            if root.left:
                dfs(root.left,depth+1)
            if root.left == None and root.right == None:
                ans.append(depth+1)
            if root.right:
                dfs(root.right, depth+1)

        dfs(root,0)
        return max(ans)
            