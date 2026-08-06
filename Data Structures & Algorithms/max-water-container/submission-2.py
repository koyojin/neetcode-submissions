class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxf=0
        l,r = 0,len(heights)-1
        while l<r:
            print(l,r)
            v=(r-l)*min(heights[l],heights[r])
            maxf=max(maxf,v)
            print(maxf)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1

        return maxf