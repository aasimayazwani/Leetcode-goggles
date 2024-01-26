# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        result = self.explore(root)
        result = [item for item in result if len(item) > 0 ]
        return result 

    def explore(self,root):
        current = [root]
        values_store = [[root.val]]
        while current:
            collection = []
            values = []
            for i in range(0,len(current)):
                node = current[i]
                if node.left != None:
                    collection.append(node.left)
                    values.append(node.left.val)
                if node.right != None:
                    collection.append(node.right)
                    values.append(node.right.val)
            values_store.append(values)
            current = collection
        return values_store