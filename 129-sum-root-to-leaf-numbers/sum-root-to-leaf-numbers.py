# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        current  = [[root,str(root.val)]]
        values = []
        answer = []
        while current:
            collections = []
            for i in range(0,len(current)):
                node = current[i][0]
                if node.left:
                    collections.append([node.left,current[i][1] + ">" +str(node.left.val)])
                if node.right:
                    collections.append([node.right,current[i][1] + ">"+str(node.right.val)])
                if (node.left == None) and (node.right == None):
                    answer.append(current[i][1])
            current = collections
            if len(current) > 0:
                values.append(current)
        answer = sum([int(item.replace(">","")) for item in answer])
        return answer
        #return sum([int(item) for item in t1])
                
