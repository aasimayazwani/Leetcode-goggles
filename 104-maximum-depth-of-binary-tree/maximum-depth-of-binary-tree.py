class Solution:
    def maxDepth(self, root: Optional[TreeNode]):  
        result = []
        def backtrack(root,depth):
            if root == None:
                return 
            backtrack(root.left,depth+1)
            result.append([root.val,depth])
            backtrack(root.right,depth+1)


        if root != None:
            backtrack(root,1)
            return max([item[1] for item in result])
        return 0 