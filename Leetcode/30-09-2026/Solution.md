# Maximum Nesting Depth of Two Valid Parentheses Strings

**LeetCode:** [Maximum Nesting Depth of Two Valid Parentheses Strings](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/description/?envType=daily-question&envId=2026-09-30)
    

## Solution
    
```python
    class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # status = 0
        ans = []
        status_a,status_b = 0,0

        for i,e in enumerate(seq):
            if e == '(':
                if i == 0:
                    ans.append(0)
                    status_a += 1
                else:
                    if status_a <= status_b:
                        ans.append(0)
                        status_a += 1 
                    else:
                        ans.append(1)
                        status_b += 1
            else:
                if status_a <= status_b:
                    ans.append(1)
                    status_b -= 1
                else:
                    ans.append(0)
                    status_a -= 1

        return ans
    