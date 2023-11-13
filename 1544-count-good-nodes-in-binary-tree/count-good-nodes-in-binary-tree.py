# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        current = [[root,str(root.val) + ">"]] 
        counting_good_nodes = 1
        while current :
            status = []
            for i in range(0,len(current)):
                
                node = current[i]
                node, story = node[0], node[1] 
                
                if node.left != None:
                    updated_string = story + str(node.left.val) + ">" 
                    status.append([node.left, updated_string ])
                    current_status = self.check(updated_string)
                    if current_status == True:
                        counting_good_nodes += 1 
                        
                if node.right != None:
                    updated_string = story + str(node.right.val) + ">"
                    status.append([node.right, updated_string  ])
                    current_status = self.check(updated_string)
                    if current_status == True:
                        counting_good_nodes += 1 

                
            current = status
        return counting_good_nodes 

    def check(self,string):
        split_string = [int(item) for item in string.split(">")[0:-1]]
        #print([max(split_string), split_string[-1]])
        return max(split_string)  == split_string[-1]