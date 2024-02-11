# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = []
        def dfs(root):
            if root == None:
                return 
            else:
                dfs(root.left)
                result.append(root.val)
                dfs(root.right)

            return result
        ans = dfs(root)
        
        node  = TreeNode(ans[0])
        answer = node
        for i in range(1,len(ans)):
            node.right = TreeNode(ans[i])
            node = node.right
        return answer 
            
