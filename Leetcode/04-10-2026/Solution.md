# 678. Valid Parenthesis String

**LeetCode:** [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/description/?envType=daily-question&envId=2026-10-04)
    

## Solution
    
```python
    class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        mapper = {'(':1,')':-1}
        s1,s2 = [],[]

        for i,e in enumerate(s):
            if e == '(':
                s1.append(i)
            elif e == '*':
                s2.append(i)
            else:
                if len(s1) == 0 and len(s2) == 0:
                    return False
                if len(s1):
                    s1.pop()
                    # print(s1)
                    continue
                if len(s2):
                    s2.pop()
                    # print(s2)
                    continue
            # print(s1,s2)
        if len(s1) and len(s2) == 0:
            return False
        while len(s1):
            if len(s2) == 0:
                return False
            temp = s1.pop()
            if temp <= s2[-1]:
                s2.pop()
            else:
                return False


        return (len(s1) == 0)       



        #recursion based approach
        # temp = 0
        # if '*' not in s:
        #     for i,e in enumerate(s):
        #         temp += mapper[e]
        #         if temp < 0:
        #             return False
        #     if temp == 0:    
        #         return True
        #     return False

        # def travel(i,status):
        #     # print(i,status)
        #     if i == 0 and s[i] == ')':
        #         return False
        #     if status > (n-i):
        #         return False
            
        #     for j in range(i,n):
        #         if s[j] != '*':
        #             if status >= 0:
        #                 status += mapper[s[j]]
        #             else:
        #                 return False
        #         else:
        #             # print(j,status)
        #             # return travel(min(j+1,n-1),status) or travel(min(j+1,n-1),status+1) or travel(min(j+1,n-1),status-1)
        #             if travel(min(j+1,n-1),status):
        #                 return True
        #             if travel(min(j+1,n-1),status+1):
        #                 return True
        #             if travel(min(j+1,n-1),status-1):
        #                 return True
        #     if j == n-1 and status == 0:
        #         return True

        #     return False
        
        # return travel(0,0)
    