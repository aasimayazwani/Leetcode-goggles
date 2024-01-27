class Solution:
    def maxDepth(self, root: Optional[TreeNode]):  
        if root == None:
            return 0 
        if root != None:
            return self.explore(root)


    def explore(self,root):
        counting = 0
        current = [root]
        while current:
            collections = []
            for i in range(0,len(current)):
                node = current[i]
                if node.left:
                    collections.append(node.left)
                if node.right:
                    collections.append(node.right)
            current = collections
            counting +=1 
        return counting