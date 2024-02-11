# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        root = [root,str(root.val)]
        answer = []
        def dfs(root):
            if root == None:
                return 
            else:
                current_node, path = root
                if current_node.left != None:
                    dfs([current_node.left,path+"->"+str(current_node.left.val)])
                if current_node.left == None and current_node.right== None:                
                    answer.append(path)
                if current_node.right != None:
                    dfs([current_node.right,path+"->"+str(current_node.right.val)])
            return answer 

        return dfs(root)