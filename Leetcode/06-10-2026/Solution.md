# 921. Minimum Add to Make Parentheses Valid

**LeetCode:** [921. Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=daily-question&envId=2026-10-06)
    

## Solution
    
```python
    class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        curr_status = 0
        ans = 0
        for e in s:
            if e == '(':
                curr_status += 1
            else:
                curr_status -= 1
                if curr_status < 0:
                    ans += 1
                    curr_status += 1
        
        if curr_status > 0:
            ans += curr_status
        
        return ans
    