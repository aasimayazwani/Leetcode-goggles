# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        r = self.explore(root)
        return r 
        
    def explore(self,root):
        current = [root]
        values  = []
        result = [root.val]
        while current:
            collections = []
            values_collector = []
            for i in range(0,len(current)):
                node = current[i]
                if node.left:
                    collections.append(node.left)
                    values_collector.append(node.left.val)
                if node.right:
                    collections.append(node.right)
                    values_collector.append(node.right.val)
            current = collections 
            result.append(sum(values_collector))
        result = result[0:-1]
        position = -100000
        maximum = -1000000
        for i in range(0,len(result)):
            if maximum < result[i]:
                maximum = result[i]
                position = i + 1
        return position 