"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        current = [root]
        depth = 0
        while current:
            children = []
            for i in range(0,len(current)):
                node = current[i]
                children += node.children
            depth +=1    
            current = children
            
        return depth 
            