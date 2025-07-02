class Solution:
    
    def insertCorrectPos(self,el,s):
        if len(s) == 0 or s[-1]< el:
            s.append(el)
        else:
            temp = s.pop()
            self.insertCorrectPos(el,s)
            s.append(temp)
   
        
            
    
        
    def Sorted(self, s):
        if len(s) > 0:
           top = s.pop()
           self.Sorted(s)
           self.insertCorrectPos(top,s)
        else:
            return
    
        
sol = Solution()
stack = [32,2,45,17,18,11,3]
sol.Sorted(stack)
print(stack)