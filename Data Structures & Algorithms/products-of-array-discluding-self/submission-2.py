#1141
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pf=1
        p=[]
        for n in nums:
            pf*=n
            p.append(pf)
        sf=1
        s=[]
        for n in nums[::-1]:
            sf*=n
            s.append(sf)
        s=s[::-1]

        res=[]
        for i in range(len(nums)):
            if i==0:
                res.append(s[i+1])
            elif i==len(nums)-1:
                res.append(p[i-1])
            else:
                res.append(p[i-1]*s[i+1])
        return res