class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        evens,odds = 1,0
        s = 0
        ans = 0
        M = 10**9 + 7
        for i,e in enumerate(arr):
            s += e
            if s%2:
                ans += evens
                odds += 1
            else:
                evens += 1
                ans += odds

        return ans%M
            
        