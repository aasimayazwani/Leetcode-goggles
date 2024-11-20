class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        cur = [root]
        while cur:
            cand = []
            for i in range(0,len(cur)):
                node = cur[i]
                node.left, node.right = node.right, node.left
                if node.left:
                    cand.append(node.left)
                if node.right:
                    cand.append(node.right)
            cur = cand
        return root 