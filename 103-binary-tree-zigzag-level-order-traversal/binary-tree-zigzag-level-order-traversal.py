# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        stack = [root]
        answer = [[root.val]]
        depth = 1
        while stack:
            depth += 1 
            inner_stack = []
            for i in range(0,len(stack)):
                node = stack[i]
                if node.left:
                    inner_stack.append(node.left)
                if node.right:
                    inner_stack.append(node.right)
                    
            #print(depth)
            stack = inner_stack
            if depth%2== 0:
                answer.append([item.val for item in stack][::-1])
            if depth%2 != 0:
                answer.append([item.val for item in stack])
                
        return [item for item in answer if item != []]