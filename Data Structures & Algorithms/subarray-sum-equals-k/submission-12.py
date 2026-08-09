# 1256-
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum=[]
        a=0
        for i in range(len(nums)):
            a+=nums[i]
            cum.append(a) 
        print(cum)
        res=0
        start=0
        for i in range(len(cum)):
            if cum[i]==k:
                print(cum[i])
                res+=1
            
            res+=cum[i+1:].count(cum[i]+k)

    
        return res