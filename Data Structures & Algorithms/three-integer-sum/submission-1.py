class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        for i in range(len(nums)):
            l,r= i+1,len(nums)-1
            while l<r:
                curr= nums[l]+nums[r]+nums[i]
                if curr==0:
                    k=[nums[i],nums[l],nums[r]]
                    res.add(tuple(k))
                if curr>0:
                    r-=1
                else:
                    l+=1
        return list(res)