# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [root]
        if root.val%2 == 0:
            return False 
        level = 1  
        while stack:
            inner= []
            level +=1 
            for i in range(0,len(stack)):
                node = stack[i]
                if node.left:
                    inner.append(node.left)
                if node.right:
                    inner.append(node.right)
            
            stack = inner
            value = [item.val for item in stack]
            if level%2 !=0: # odd situation 
                pos= [item for item in value if item%2 ==0]
                if len(pos) == 0:
                    if self.check_odd(value) == False:
                        return False 
                else:
                    return False
                
            if level%2 ==0:
                pos= [item for item in value if item%2 !=0]
                if len(pos) ==0:
                    if self.check_even(value) == False:
                        return False 
                else:
                    return False
        return True         
        
    def check_odd(self,arr):
        for i in range(0,len(arr)-1):
            if arr[i+1]<=arr[i]:
                return False 
            else :
                pass             
        return True 
    
    
    def check_even(self,arr):
        for i in range(0,len(arr)-1):            
            if arr[i+1]>=arr[i]:
                return False 
            else :
                pass 
        return True 