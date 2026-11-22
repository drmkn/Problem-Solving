class Solution:
    def minCost(self, nums: list[int]) -> int:
        n = len(nums)

        keys = Counter(nums[1:n-1])

        cost = {}

        ## prefix
        last = 0
        for i in range(1,n-1):
            # if i == 1:
            #     if (i,nums[i]) not in cost:
            #         cost[(i,nums[i])] = [0,0]
            #     cost[(i,nums[i])][0] = (nums[i])
            #     continue
            if nums[i] != nums[i-1]:
                last = i
            if (i,nums[i]) not in cost:
                cost[(i,nums[i])] = [0,0]
            cost[(i,nums[i])][0] = (last)*(nums[i])

        ##suffix
        last = n-1
        for i in range(n-2,0,-1):
            # if i == n-2:
            #     if (i,nums[i]) not in cost:
            #         cost[(n-1-i,nums[i])] = [0,0]
            #     cost[(i,nums[i])][1] = (nums[i])
            #     continue
            if nums[i] != nums[i+1]:
                last = i
            if (i,nums[i]) not in cost:
                cost[(i,nums[i])] = [0,0]
            cost[(i,nums[i])][1] = (n-1-last)*(nums[i])

        # print(cost)

        ans = float('inf')

        for k,v in cost.items():
            ans = min(ans,sum(v))

        return ans 

        

        

        
            
            