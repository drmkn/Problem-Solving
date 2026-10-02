# Maximum Nesting Depth of the Parentheses

**LeetCode:** [Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/?envType=daily-question&envId=2026-09-28)
    

## Solution
    
```python
    class Solution:
    def maxDepth(self, s: str) -> int:
        M = 0
        c = 0
        for e in s:
            if e == '(':
                c += 1
            elif e == ')':
                c -= 1
            M = max(c,M)
        
        return M
    