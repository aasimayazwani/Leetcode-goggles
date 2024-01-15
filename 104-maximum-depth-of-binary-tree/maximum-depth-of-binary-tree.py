class Solution:
    def maxDepth(self, root: Optional[TreeNode]):  
        if root == None:
            return 0 
        if root != None:
            counting = 1 

        current = [root]
        while current:
            children = []
            values  = []
            for i in range(0,len(current)):
                if current[i].left != None:
                    children.append(current[i].left)
                if current[i].right != None:
                    children.append(current[i].right)
            current = children
            if len(children) != 0:
                counting +=1 
        return counting 
