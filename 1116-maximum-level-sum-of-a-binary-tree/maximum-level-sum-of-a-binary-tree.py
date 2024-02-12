class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        values = []

        def dfs(node, depth):
            if node is None:
                return
            if len(values) < depth:
                values.append([node.val])
            else:
                values[depth-1].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)

        # Calculate the sum for each level and determine the level with the maximum sum
        max_sum = float('-inf')
        max_level = 0
        for i, val in enumerate(values):
            current_sum = sum(val)
            if current_sum > max_sum:
                max_sum = current_sum
                max_level = i + 1  # +1 because levels are 1-indexed

        return max_level
