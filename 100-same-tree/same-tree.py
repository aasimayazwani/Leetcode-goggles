# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        v1 = self.bfs(p)
        v2 = self.bfs(q)
        return v1 == v2 

    def bfs(self,root):
        if root == None:
            return [] 
        current = [root]
        final = []
        while current:
            children = []
            values = [root.val]
            for i in range(0,len(current)):
                node = current[i]
                if node.left:
                    children.append(node.left)
                    values.append(node.left.val)
                if node.left == None:
                    values.append("missing")
                if node.right:
                    children.append(node.right)
                    values.append(node.right.val)
                if node.right == None:
                    values.append("missing")
            current = children
            final.append(values)
        return final    
