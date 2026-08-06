class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            p=1
            pt=i+1
            for j in range(len(nums)-1):
                if pt>len(nums)-1:
                    p*=nums[pt-len(nums)]
                else:
                    p*=nums[pt]
                pt+=1
            res.append(p)

        return res
