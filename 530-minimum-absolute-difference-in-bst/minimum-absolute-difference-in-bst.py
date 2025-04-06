# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = []
        heapq.heapify(ans)
        def dfs(root):
            if root == None:
                return 
            dfs(root.left)
            heapq.heappush(ans,root.val)    
            dfs(root.right)
        dfs(root)
        difference = 100000000
        previous = heapq.heappop(ans)
        while ans:
            current = heapq.heappop(ans)
            difference = min(difference,current-previous)
            previous = current
        return difference 