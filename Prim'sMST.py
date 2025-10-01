import heapq

# Your Solution class
class Solution:
    def spanningTree(self, V, adj):
        res = 0
        visit = set()
        minHeap = [[0, 0]]  # Start from node 0

        while len(visit) < V:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue

            res += w1
            visit.add(n1)

            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, [w2, n2])

        return res

V = 3 
adj = [[[1, 5], [2, 15]], [[0, 5], [2, 10]], [[0, 15], [1, 10]]]

# Create object and call the method
sol = Solution()
mst_weight = sol.spanningTree(V, adj)
print("Weight of Minimum Spanning Tree:", mst_weight)
