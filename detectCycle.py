class Solution:
    def isCyclic(self, N, adj):
        
        topSort = []
        visit = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            path.add(node)
            

            for neighbours in adj[node]:
                if not dfs(neighbours):
                    return False
            topSort.append(node)
            visit.add(node)
            path.remove(node)
            return True

        for i in range(N):
            if not dfs(i):
                return False
        topSort.reverse()
        return True
    
if __name__ == "__main__":
# Example 1: Graph with no cycle (DAG)
    N1 = 6
    adj1 = {
        0: [1, 2],
        1: [3],
        2: [3, 4],
        3: [5],
        4: [5],
        5: []
    }

    sol = Solution()
    print("Graph 1 has cycle?", not sol.isCyclic(N1, adj1))  # Expected: False

    # Example 2: Graph with a cycle
    N2 = 4
    adj2 = {
        0: [1],
        1: [2],
        2: [3],
        3: [1]  # back edge creates a cycle
    }

    sol2 = Solution()
    print("Graph 2 has cycle?", not sol2.isCyclic(N2, adj2))  # Expected: True

        
        


       

        