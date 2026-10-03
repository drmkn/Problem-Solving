# Longest Valid Parentheses

**LeetCode:** [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/description/?envType=daily-question&envId=2026-10-03)
    

## Solution
    
```python
    class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        
        if n == 0 or n == 1:
            return 0

        ##prefix sum filter
        map = {'(':1,')':-1}
        prefix_sum = [map[s[0]]]
        for i in range(1,n):
            prefix_sum.append(prefix_sum[-1] + map[s[i]])
        if len(set(prefix_sum)) == n and 0 not in prefix_sum:
            return 0


        # at every index check the max achievable VPS
        
        def max_VPS(i):
            if s[i] == ')':
                return 0
            else:
                status = 0
                M = i
                for j in range(i,n):
                    if s[j] == '(':
                        status += 1
                    else:
                        status -= 1
                    if status < 0:
                        break
                    if status == 0:
                        M = max(M,j)
                if M != i:
                    return M-i+1
                return 0     
        ans = 0
        for k in range(n):

            if ans > (n-k):
                break
            ans = max(ans,max_VPS(k))
        # temp = [max_VPS(i) for i in range(n)]
        # if len(temp):
        #     return max(temp)
        return ans
    