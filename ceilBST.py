class Solution:
    def findCeil(self,root, inp):
        
        ceil = -1
        
        while root:
            
            if root.key == inp:
                ceil = root.key
                return ceil
            
            
            elif root.key > inp:
                    ceil = root.key
                    root = root.left
            else:
                    
                root = root.right
            
        
        return ceil
        