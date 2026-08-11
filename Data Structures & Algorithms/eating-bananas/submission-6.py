class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r= 1, max(piles)
        res=float('inf')
        while l<=r:
            mid=(l+r)//2
            c=0
            for p in piles:
                c+=math.ceil(p/mid)
            if c<=h:
                res=min(mid,res)
                r=mid-1
            else:
                l=mid+1
                
        return res

