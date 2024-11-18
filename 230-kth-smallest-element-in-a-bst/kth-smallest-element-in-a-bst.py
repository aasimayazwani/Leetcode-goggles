# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(root):
            if root == None:
                return 
            dfs(root.left)
            heapq.heappush(arr,root.val)
            dfs(root.right)
        
        dfs(root)
        while k > 0:
            a = heapq.heappop(arr)
            k-=1 
        return a 