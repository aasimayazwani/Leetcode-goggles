# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = []
        def dfs(root):
            if root == None:
                return 

            else:
                dfs(root.left)
                values.append(root.val)
                dfs(root.right)

            return values

        dfs(root)
        ## sorted array called values
        from collections import Counter
        mapping = Counter(values)
        keys = list(mapping.keys())
        for i in range(0,len(keys)):
            difference = k - keys[i]
            if (difference in mapping) and (difference != keys[i]):
                return True
        return False 

