class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        last = 0
        M = 0
        n = len(nums)

        for i in range(1,n):
            if nums[i] > nums[i-1]:
                M = max(M,i-last)
            else:
                last = i
        last = 0
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                M = max(M,i-last)
            else:
                last = i
        
        return M+1