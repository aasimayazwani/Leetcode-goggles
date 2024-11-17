# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = [root]
        ans = [root.val]
        while stack:
            candidates = []
            level_total = 0 
            level_length = 0 

            for i in range(0,len(stack)):
                node = stack[i]
                if node.left:
                    candidates.append(node.left)
                    level_total += node.left.val
                    level_length +=1

                if node.right:
                    candidates.append(node.right)
                    level_total += node.right.val
                    level_length +=1 

            stack = candidates
            if level_length > 0:
                ans.append(level_total/level_length)
            if level_length == 0:
                return ans
            
