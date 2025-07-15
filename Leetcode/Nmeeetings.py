class Solution:
    
    def maximumMeetings(self,start,end):
        n = len(start)
        meeting = []
         
        for i in range(n):
            meeting.append([start[i],end[i]])
        
        meeting.sort(key=lambda item: item[1])
        
        present = 0
        cnt = 0
        for i in range(n):
            
            if meeting[i][0] > present:
                present = meeting[i][1]
                cnt += 1
        
        return cnt
        
sol = Solution()
result = sol.maximumMeetings([1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9])
print(sol.maximumMeetings([10, 12, 20],[20, 25, 30]))
print(result)

        
        
        
    
                