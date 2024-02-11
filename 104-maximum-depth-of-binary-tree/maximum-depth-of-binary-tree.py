class Solution:
    def maxDepth(self, root: Optional[TreeNode]):  
        if root == None:
            return 0 
        root = [root,1]
        depth = []
        
        def dfs(root):
            
            [root,path] = root

            if root.left != None:
                dfs([root.left,path+1])
            
            if root.left == None and root.right == None:
                depth.append(path)

            if root.right != None:
                dfs([root.right,path+1])

            return depth

        ans = dfs(root)
        return max(ans)