class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[True]+[False]*n

        for i in range(n):
            if not dp[i]:
                continue
            for j in range(1, nums[i]+1):
                if i+j<n:
                    dp[i+j]=True
        return dp[n-1]