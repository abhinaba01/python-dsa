class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        # code here
        ans = []
        n = len(maze)
        visited = []
        
        def dfs(i,j,path):
            if i == n-1 and j == n-1:
                ans.append(path)
                return
            
            visited.append([i,j])
            if i+1<n: 
                if maze[i+1][j] != 0 and  [i+1,j] not in visited:
                    path = path + "D"
                    
                    
                    dfs(i+1,j,path)
                  
                    path = path[:-1]
            if j-1>=0:
                if maze[i][j-1] != 0 and  [i,j-1] not in visited:
                    path = path + "L"
                   
                    dfs(i,j-1,path)
                   
                    path = path[:-1]
            if j+1 < n:
                if maze[i][j+1] != 0 and  [i, j+1] not in visited:
                    path = path + "R"
                    
                    dfs(i,j+1,path)
                    
                    path = path[:-1]
            if i-1 >=0:
                if maze[i-1][j] != 0 and  [i-1, j] not in visited:
                    path = path + "U"
                    
                    dfs(i-1,j,path)
                    
                    path = path[:-1]
                    
            visited.pop()
                    
        dfs(0,0,"")
        return ans
        
            