class Solution:
    def shortestPath(self, edges, N, M):

        adj = [[] for _ in range(N)]
        dist = [-1] * N

        for start,end in edges:
            adj[start].append(end)
            adj[end].append(start)

        queue = [0]
        dist[0] = 0
        while queue:

            node = queue.pop(0)
            
            for neighbours in adj[node]:
                if dist[neighbours] == -1:
                    dist[neighbours] = dist[node] + 1
                    queue.append(neighbours)
        
        return dist