class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        queue = [root]
        while queue:
            candidates = []
            for i in range(0,len(queue)):
                node = queue[i]
                node.left, node.right = node.right, node.left
                
                if node.left:
                    candidates.append(node.left)
                if node.right:
                    candidates.append(node.right)
            if len(queue) > 0:
                queue = candidates

        return root
                