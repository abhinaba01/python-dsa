class Solution:
    def solve(self, bt):

        bt.sort()
        n = len(bt)

        total_wait,current_wait = 0,0

        for i in range(n-1):
            current_wait += bt[i]
            total_wait += current_wait
        
        avg_wait = total_wait // n
        return avg_wait

        #your code goes here