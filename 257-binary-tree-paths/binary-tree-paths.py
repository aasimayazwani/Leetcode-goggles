# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_path = []

        def dfs(root,path,value):

            if root == None:
                return 
            else:
                path = path + str(value)

                if (root.left == None) and (root.right == None):
                    all_path.append(path)
                else:
                    if root.left != None:
                        dfs(root.left,path +"->", root.left.val)
                    if root.right != None:
                        dfs(root.right,path +"->", root.right.val)

        dfs(root,"",root.val)
        return all_path
            
            