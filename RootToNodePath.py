class Solution:
    def allRootToLeaf(self, root):

        path = []
        arr = []
        
        def dfs(node):

            if not node:
                return
            arr.append(node.val)
            if not node.left and not node.right:
                path.append(arr[:])
                
            else:
                
                dfs(node.left)
                dfs(node.right)
            
            arr.pop()
        
        dfs(root)
        
        return path