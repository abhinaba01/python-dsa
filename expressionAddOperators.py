from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

       

        n = len(num)
        ans = []
       
        def dfs(index,path):
            
            if index == n - 1:
                
                result = eval(path)
                if result == target:
                    ans.append(path)

                return

            path += ("*" + num[index+1])

            dfs(index+1,path)

            path = path[:-2]
            path += ("+" + num[index+1])

            dfs(index+1,path)

            path = path[:-2]
            path += ("-" + num[index+1])

            dfs(index+1,path)

       
        dfs(0,f"{num[0]}")
        return ans

        
sol = Solution()

print(sol.addOperators("123",6))

print(sol.addOperators("00",0))


