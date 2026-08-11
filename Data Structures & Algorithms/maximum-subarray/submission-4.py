class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cur=0
        cum=[]
        hi=float('-inf')
        lo=0
        for n in nums:
            cur+=n
            cum.append(cur)
        for c in cum:
            hi=max(hi, c-lo)
            if c<lo:
                lo= c
        return hi
        