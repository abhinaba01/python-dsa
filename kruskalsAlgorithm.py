

import heapq

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False  # already connected
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True



class Solution:
    def spanningTree(self, V, adj):
        minHeap = []
        for i in range(V):
            for neighbor,weight in adj[i]:
                if i < neighbor:
                    heapq.heappush(minHeap,[weight,neighbor,i])
        
        unionFind = UnionFind(V)

        mst = []
        total_weight = 0
        while len(mst) < V - 1:
            w1,n1,n2 = heapq.heappop(minHeap)
            if not unionFind.union(n1,n2):  
            # they belong to the same comnnected component
                continue
            mst.append([n1,n2])
            total_weight += w1
        
        return mst,total_weight


if __name__ == "__main__":
    
    V = 4
    adj = {
    0: [(1, 1), (3, 4)],
    1: [(0, 1), (2, 2)],
    2: [(1, 2), (3, 3)],
    3: [(0, 4), (2, 3)]
}

    adj_list = [[] for _ in range(V)]
    for u in adj:
        adj_list[u] = adj[u]

    sol = Solution()
    mst, total_weight = sol.spanningTree(V, adj_list)

    print("Edges in MST:", mst)
    print("Total weight of MST:", total_weight)
