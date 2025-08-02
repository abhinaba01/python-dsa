class Solution:
    def isCycle(self, V, adj):

        vis = [0 for i in range(V)]

        def dfs(node,parent):

            vis[node] = 1

            for neighbor in adj[node]:
                if vis[neighbor] == 0:
                    if dfs(neighbor,node):
                        return True
                elif neighbor != parent:
                    return True
            
            return False

        return dfs(0,-1)

                    