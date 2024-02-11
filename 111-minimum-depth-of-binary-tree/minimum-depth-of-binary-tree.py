# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0 
        node = [root,1]
        depth = []
        def dfs(node):
            if root == None:
                return 
            current, path = node
            if current.left != None:
                dfs([current.left,path+1])

            if current.left == None and current.right == None:
                depth.append(path)

            if current.right != None:
                dfs([current.right,path+1])
            return depth

        current = dfs(node)
        print(current)
        return min(current)