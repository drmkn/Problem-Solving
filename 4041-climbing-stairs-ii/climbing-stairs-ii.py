class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')]*(n+1)

        def next(i):
            return list(set([min(i+1,n),min(i+2,n),min(i+3,n)]))
        
        dp[0] = 0

        for i in range(n):
            nxts = next(i)

            # m = len(nxts)

            for k in nxts:
                # print(i,dp[i],k,dp[k],dp[i]+costs[k-1]+(k-i)**2)
                dp[k] = min(dp[k],dp[i]+costs[k-1]+(k-i)**2)
        
        # print(dp)
            
        
        return dp[-1]