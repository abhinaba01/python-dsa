class Solution:
    def shortest_distance(self, matrix):

        V = len(matrix)

        dist = [[float("inf")] * V for _ in range(V)]

        
        
        for i in range(V):
            for j in range(V):
                if i == j:
                    dist[i][j] = 0
                if matrix[i][j] != -1:
                    dist[i][j] = matrix[i][j] 
        
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dist[i][j] = min(dist[i][k]+ dist[k][j], dist[i][j])
        
        for i in range(V):
            for j in range(V):
                if dist[i][j] == float("inf"):
                    dist[i][j] = -1

        return dist
        

        


        
        
        



        
    