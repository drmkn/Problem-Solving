# Generate Parentheses

**LeetCode:** [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/?envType=daily-question&envId=2026-10-02)
    

## Solution
    
```python
    class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def generate(s,status):
            
            if len(s) == 2*n:
                if status == 0: 
                    ans.append(s)
                return
            
            if status + 1 > 0:
               generate(s+'(',status+1)
            
            if status - 1 >= 0:
               generate(s+')',status-1)    
            
            return

        
        generate("",0)
        return ans
    