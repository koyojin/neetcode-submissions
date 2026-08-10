class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=0
        cum=[]
        for n in nums:
            cur+=n
            cum.append(cur)
        print(cum)
        best=cum[0]
        lo=0
        for c in cum:
            best= max(c-lo,best)
            lo=min(c, lo)
        return best
            

