# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        values = []
        root = [root,str(root.val)]
        def dfs(root):
            if root == None:
                return 
            else:
                current, path = root
                if current.left != None:
                    dfs([current.left,path + ">" +str(current.left.val)])
                if current.left == None and current.right == None:
                    path = path.replace(">","")
                    path = int("".join(path),2)
                    values.append(path)
                if current.right != None:
                    dfs([current.right,path + ">" +str(current.right.val)])
                return values
        ans = dfs(root)
        return sum(ans)