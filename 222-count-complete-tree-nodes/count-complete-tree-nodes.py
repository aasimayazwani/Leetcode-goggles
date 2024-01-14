# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        counting  = 0 

        if root == None:
            return 0
        if root != None:
            counting +=1

        collection = [root]

        while len(collection) > 0 :
            children = []
            for child in collection:
                if child.left != None :
                    counting += 1 
                    children.append(child.left)

                if child.right != None:
                    counting +=1 
                    children.append(child.right)

            collection = children
        return counting 