# 856. Score of Parentheses

**LeetCode:** [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/description/?envType=daily-question&envId=2026-10-05)
    

## Solution
    
```python
    class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth_sum = {1:0}
        status = 0

        for i,e in enumerate(s):
            # print(status,depth_sum)
            if e == '(':
                status += 1

                if status not in depth_sum:
                    depth_sum[status] = 0
            else:
                if s[i-1] == ')':
                   depth_sum[status] += 2*depth_sum[status+1]
                   depth_sum[status+1] = 0
                else:    
                    depth_sum[status] += 1
                status -= 1
            # print(e,status,depth_sum)
        return depth_sum[1]
    