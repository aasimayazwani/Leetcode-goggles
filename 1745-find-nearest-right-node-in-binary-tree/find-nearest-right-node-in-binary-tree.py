# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        
        stack = [root]
        flag = False
        while stack:
            current = []
            for i in range(0,len(stack)):
                node = stack[i]
                if node.left != None :
                    current.append(node.left)
                    if node.left.val == u.val:
                        flag = True

                if node.right != None:
                    current.append(node.right)
                    if node.right.val == u.val:
                        flag = True
                
            if flag == True:
                results = [item for item in current]
                for i in range(0,len(results)):
                    #print(results[i])
                    if results[i].val == u.val:
                        try:
                            return results[i+1]
                        except:
                            return None 
                return None 
            else:
                stack = current
        return None 