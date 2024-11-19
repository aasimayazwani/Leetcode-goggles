# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        result = []
        def dfs(root):
            if root == None:
                return 
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)

        dfs(root)
        left, right = 0, len(result)-1
        while left < right:
            total = result[left] + result[right]
            if total == k:
                return True 
            elif total < k:
                left +=1 
            elif total > k:
                right -=1 
        return False
