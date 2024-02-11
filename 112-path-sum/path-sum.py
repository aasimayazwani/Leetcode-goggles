# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        values = []
        if root == None:
            return False 
        root = [root,str(root.val)]
        def dfs(root):
            if root == None:
                return
            else:
                child, path = root
                if child.left != None:
                    dfs([child.left,path + ">" + str(child.left.val)])

                if child.left == None and child.right == None:
                    path = ("".join(path.replace(">","+")))
                    total = eval(path)
                    values.append(total)

                if child.right != None:
                    dfs([child.right,path + ">" + str(child.right.val)])
                
                return values
        current = dfs(root)
        if targetSum in current:
            return True 
        return False