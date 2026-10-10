# 2333. Minimum Sum of Squared Difference

**LeetCode:** [2333. Minimum Sum of Squared Difference](https://leetcode.com/problems/minimum-sum-of-squared-difference/description/?envType=daily-question&envId=2026-10-10)
    

## Solution
    
```python
    class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        
        n = len(nums1)

        temp = []
        base = []
        for i in range(n):
            temp.append(-1*abs(nums1[i]-nums2[i]))
            base.append((nums1[i]-nums2[i]))

        def sumlist(l):
            a = 0
            for e in l:
                a += e**2
            return a
        # print(temp)
        heapq.heapify(temp)
        ans = sumlist(base)
        # print(temp)
        # print(heapq.heappop(temp))
        while (k1 != 0 or k2 != 0):
            # print(temp)
            M = heapq.heappop(temp)
            heapq.heappush(temp, -1*(abs(M)-1))
            if k1:
                k1 -=1
            else:
                if k2:
                    k2 -= 1
            
            for i,e in enumerate(temp):
                if e == M:
                    if k1:
                        k1 -= 1
                        temp[i] = -1*(abs(M)-1)
                        # print(temp)
                        continue
                    if k2:
                        k2-=1
                        temp[i] = -1*(abs(M)-1)
                        # print(temp)
                        continue
            
            
            # # print(temp)
            
            ans = min(ans,sumlist(temp))
            # print(temp)
        
        return ans

        ## greddy approach as hint


        # ## Brute force recursion based
        # def travel(i,k1,k2,S):
        #     # print(i,k1,k2,S,ans[0])
        #     if k1 == 0 and k2 == 0:
        #         S += (sum(temp[i:]))
        #         ans[0] = min(ans[0],S)
        #         # print(f"update -> {i},{k1},{k2},{S},{ans[0]}")
        #         return
            
        #     if k1 > 0:
        #         choices1 = [i for i in range(-k1,k1+1)]
        #     else:
        #         choices1 = [0]
        #     if k2 > 0:
        #         choices2 = [i for i in range(-k2,k2+1)]
        #     else:
        #         choices2 = [0]

        #     for update1 in choices1:
        #         for update2 in choices2:
        #             # flag1,flag2 = 0,0
        #             # if update1:
        #             #     flag1 = 1
        #             # if update2:
        #             #     flag2 = 1
        #             # print(i,k1,update1,k2,update2,S,ans)  
        #             if i < n:
        #                 #stay    
        #                 # if update1 or update2:
        #                 #     travel(i,k1-update1,k2-update2,S+(nums1[i]+update1-(nums2[i]+update2))**2)      
        #             #move
        #                 addn = (nums1[i]+update1-(nums2[i]+update2))**2
        #                 if addn <= temp[i]:
        #                     # temp[i] = addn
        #                     travel(i+1,k1-abs(update1),k2-abs(update2),S+addn)
            
        #     return 

        # travel(0,k1,k2,0)

        # return ans[0]
    