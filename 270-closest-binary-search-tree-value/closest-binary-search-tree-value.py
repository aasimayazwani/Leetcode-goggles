# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = []
        

        def dfs(root):
            if root == None:
                return 
            dfs(root.left)
            ans.append((abs(target-root.val),root.val))
            dfs(root.right)
        
        dfs(root)
        heapq.heapify(ans)
        a, b = heapq.heappop(ans)
        return b
        