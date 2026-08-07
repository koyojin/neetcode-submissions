#1012
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        arr= range(max(sorted(weights)),sum(sorted(weights))+1)
        l,r=0,len(arr)
        while l<r:
            mid = (l+r)//2
            cap = arr[mid]
            cnt=1
            repo=0
            d=0

            while d < len(weights):
                repo+= weights[d]
                if repo>cap:
                    cnt+=1
                    repo=weights[d]
                d+=1


            if cnt<=days:
                r=mid
            if cnt>days:
                l=mid+1
        
        return arr[l]
                