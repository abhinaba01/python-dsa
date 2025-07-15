#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        
        n = len(arr)
        
        arr.sort()
        dep.sort()
        
        i,j,platform,max_platform = 0,0,0,0
       
        while i < n and j < n:
            if arr[i] <= dep[j]:
                i += 1
                platform += 1
                max_platform = max(platform,max_platform)
            else:
                j += 1
                platform -= 1
            
                
        return max_platform
            