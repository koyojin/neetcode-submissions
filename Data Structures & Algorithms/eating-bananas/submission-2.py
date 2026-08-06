class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        res=[]
        l=1
        r=piles[len(piles)-1]
        while l<=r:
            cnt=0
            mid = (l+r)//2
            for p in piles:
                c= p%mid
                cnt+= p//mid
                if c!=0:
                    cnt+=1

            if cnt<=h:
                r=mid-1
                res.append(mid)
            else:
                l=mid+1


        return min(res)       
