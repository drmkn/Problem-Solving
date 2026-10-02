# Valid Parentheses

**LeetCode:** [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

## Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        
        pair = {'(' : ')' ,'{' :'}','[' :']'}
        stack = []

        for i,e in enumerate(s):
            if e in ['(','{','[']:
                # s1.append(e)
                stack.append(pair[e])
            else:
                if i == 0:
                    return False
   
                if len(stack) and (e == stack[-1]):
                    # print(e)
                    stack.pop()
                else:
                    return False
            
        return (len(stack) == 0)
```