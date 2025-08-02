class Solution:
    # Function to return connected components of the graph
    
    
    def dfs(self,node,adj,vis,component):
        
        vis[node] = True
        
        component.append(node)
        
        for neighbor in adj[node]:
            if not vis[neighbor]:
                self.dfs(neighbor,adj,vis,component)
            
        
        
        
    def getComponents(self, V, edges):

        
        # build the adjacency graph 
        adj = [[0 for i in range(V)] for _ in range(V)]
        
        for edge in edges:
            u , v = edge[0] , edge[1]
            
            adj[u].append(v)
            adj[v].append(u)
            
            
        vis = [False] * V
        res = []
        
    
        for i in range(V):
            if not vis[i]:
                component = []
                
                self.dfs(i,adj,vis,component)
                
                res.append(component)
                
        return res
                
                
        