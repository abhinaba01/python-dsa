class Solution:
    def findPreSuc(self, root, key):
        
        successor , predecessor = None , None
        fRoot = root
        
        while root:
            if root.data > key:
                successor = root
                root = root.left
            else:
                
                root = root.right
                
        while fRoot:
            if fRoot.data < key:
                predecessor = fRoot
                fRoot = fRoot.right
            else:
                
                fRoot = fRoot.left
        
        return predecessor , successor
        