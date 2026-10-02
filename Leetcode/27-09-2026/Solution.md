# Reverse Substrings Between Each Pair of Parentheses

**LeetCode:** [Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/?envType=daily-question&envId=2026-09-27)
    

## Solution
    
```python
    class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        if s.find('(') == -1:
            return s
        # l_track,r_track = [],[]
        # (((()))())
        # for i,e in enumerate(s):
        #     if e == '(':
        #         l_track.append(i)
        #     elif e == ')':
        #         r_track.append(i)

        # #inner most mathched parethesis
        # bruteforce 
        def finder_match(s):
            l_track,r_track = None,None
            for i,e in enumerate(s):
                if e == '(':
                    l_track = i
                elif e == ')':
                    r_track = i
                    break
            ans = s[:l_track]
            ans += s[l_track+1:r_track][::-1]
            ans += s[r_track+1:] 
            return ans

        temp = s
        while True:
            temp = finder_match(temp)

            if temp.find('(') == -1:
                break
        
        return temp
    