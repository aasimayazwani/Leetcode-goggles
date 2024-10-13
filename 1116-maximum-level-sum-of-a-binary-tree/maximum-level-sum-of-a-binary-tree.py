class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        values = []
        answers = [root.val]
        stack = [root]
        while len(stack) > 0:
            current = []
            for i in range(0,len(stack)):
                node = stack[i]
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)
            stack = current
            if len(current) > 0:
                answers.append(sum([item.val for item in current]))
        result = answers 
        position = -100000
        maximum = -1000000
        for i in range(0,len(result)):
            if maximum < result[i]:
                maximum = result[i]
                position = i + 1
        return position 