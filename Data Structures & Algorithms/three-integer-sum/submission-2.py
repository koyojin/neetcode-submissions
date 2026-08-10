#1304
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            cur=nums.copy()
            cur.pop(i)
            l,r = 0, len(cur)-1
            while l<r:
                if nums[i]+cur[l]+cur[r]==0:
                    res.append([nums[i],cur[l],cur[r]])
                    l+=1
                    r-=1
                elif nums[i]+cur[l]+cur[r]<0:
                    l+=1
                else: 
                    r-=1
        unique = {tuple(sorted(t)) for t in res}
        answer = [list(t) for t in unique]

        return answer

        