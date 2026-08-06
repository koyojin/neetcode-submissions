class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp= 0
        rp= len(heights)-1
        mx=0
        while lp<rp:
            v= min(heights[lp],heights[rp])*(rp-lp)
            if v>mx:
                mx=v
            if heights[lp]<heights[rp]:
                lp+=1
            else:
                rp-=1
        return mx