class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    
    
    
    def merge(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
    
       
        L = [0] * (n1)
        R = [0] * (n2)
    
        
        for i in range(0, n1):
            L[i] = arr[l + i]
    
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
    
        
        i = 0     
        j = 0     
        k = l     
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                self.cnt = self.cnt + n1 - i
                arr[k] = R[j]
                
                j += 1
            k += 1
    
       
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
    
       
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1




    def mergeSort(self,arr, l, r):
        if l < r:
    
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l+(r-l)//2
    
            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, r)
            self.merge(arr, l, m, r)


    def inversionCount(self,arr):
        self.cnt = 0
        n = len(arr)
        self.mergeSort(arr,0,n-1)
        
        return self.cnt
    
if __name__ == '__main__':
    arr = [5,4,2,6,10,9,3,7]
    sol = Solution()
    print(sol.inversionCount(arr))  