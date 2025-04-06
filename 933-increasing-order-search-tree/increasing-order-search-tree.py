# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        ans = []
        dfs(root)
        
        answer = temp = TreeNode(-1)
        for i in range(0,len(ans)):
            cur = TreeNode(ans[i])
            temp.right = cur
            temp = temp.right
        return answer.right 

        