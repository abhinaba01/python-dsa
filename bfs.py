class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        
        n = len(adj)
        
        vis = [0 for i in range(n)]
        queue = [0]
        vis[0] = 1
        
        path = []
        
        while queue:
            
          
            node = queue.pop(0)
            path.append(node)
            
            
                
            for neighbor in adj[node]:
                if vis[neighbor] == 0:
                    queue.append(neighbor)
                    vis[neighbor] = 1
        return path
            
            
            
       
        
                
                    
            
            