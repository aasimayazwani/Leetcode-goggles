# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        current = [root]
        answer = [root.val]
        while current:
            children = []
            max_value = -2947483648
            for i in range(0,len(current)):
                node = current[i]
                if node.left:
                    children.append(node.left)
                    max_value = max(max_value, node.left.val)
                if node.right:
                    children.append(node.right)
                    max_value = max(max_value, node.right.val)
            current = children
            if len(current) == 0:
                return answer
            answer.append(max_value)
