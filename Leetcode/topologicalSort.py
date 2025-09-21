class Solution:
    def topoSort(self, V, adj):

        topSort = []
        visit = set()

        def dfs(i,adj,visit,topSort):
            if i in visit:
                return
            visit.add(i) 

            for neighbours in adj[i]:
                dfs(neighbours,adj,visit,topSort)
            topSort.append(i)

        for i in range(V):
            dfs(i,adj,visit,topSort)
        topSort.reverse()
        return topSort
        
        


       
