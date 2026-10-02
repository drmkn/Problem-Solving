# Check if There Is a Valid Parentheses String Path

**LeetCode:** [Check if There Is a Valid Parentheses String Path](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/description/?envType=daily-question&envId=2026-09-29)
    

## Solution
    
```python
    class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        def add_elt_set(e,s):
            l = list(s)
            temp = []
            for a in l:
                if a >= 0:
                    temp.append(a+e)
            return set(temp)

        ## 2D DP based  approach
        m,n = len(grid),len(grid[0])

        if (m+n-1)%2:
            return False

        if grid[0][0] != '(' or grid[m-1][n-1] != ')':
            return False
        dp = [[set()]*n for _ in range(m)]
        # print(dp)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '(':
                    sign = 1
                else:
                    sign = -1
                if i == 0 and j == 0:
                    if sign == -1:
                        return False
                    dp[i][j].add(sign)
                elif i == 0 and j > 0:
                    dp[i][j] = add_elt_set(sign,dp[i][j-1])
                elif j == 0 and i > 0:
                    dp[i][j] = add_elt_set(sign,dp[i-1][j])   
                else:
                    dp[i][j] = set(list(add_elt_set(sign,dp[i-1][j])) + list(add_elt_set(sign,dp[i][j-1])))
        # print(dp)
        # print(dp[m-1][n-1])           
        ans = list(dp[m-1][n-1])
        return (0 in ans)

        # DFS based recursion
        ## bruteforce
        # m,n = len(grid),len(grid[0])

        # if (m+n-1)%2:
        #     return False
        # # print(m,n)
        # def travel(loc,status):
        #     i,j = loc[0],loc[1]
            
        #     #debug 
        #     # print(loc,status)
        #     #update status
        #     if grid[i][j] == '(':
        #         status += 1
        #     else:
        #         status -= 1

        #     #feasibility check
        #     if status > (m-i + n-j -1) or status < 0:
        #         return False

        #     # print(loc,status)
        #     #stop condition
        #     if (status == 0) and (i == m-1) and (j == n-1):
        #         # print(m,n)
        #         return True
            
        #     #move logic

        #     #right move
        #     if j < n-1 and i < m-1:
        #         if travel((i+1,j),status):
        #             return True
        #         else:
        #             if travel((i,j+1),status):
        #                 return True
        #             return False

        #         # return travel((i,j+1),status) or travel((i+1,j),status) 
        #     elif j == n-1 and i != m-1:
        #         return travel((i+1,j),status)
        #     elif i == m-1 and j != n-1:
        #         return travel((i,j+1),status)
            
        #     return False


        # ans = travel((0,0),0) 

        # return ans
    