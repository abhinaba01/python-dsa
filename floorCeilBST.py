''' class Node:
    def __init__(self, val):
        self.right = None
        self.key = val
        self.left = None '''
        
class Solution:
    def findCeil(self,root, inp):
        
        ceil = -1 , floor = -1
        
        while root:
            
            if root.key == inp:
                ceil= floor = root.key
                return [floor,ceil]
            
            
            elif root.key > inp:
                    ceil = root.key
                    root = root.left
            else:
                floor = root.key
                root = root.right
            
        
        return [floor,ceil]