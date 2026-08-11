#1638
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for n in nums1:
            ck=False
            t= nums2.index(n)
            for i in range(t,len(nums2)):
                if nums2[i]> n:
                    res.append(nums2[i])
                    ck=True
                    break
            if ck==False:
                res.append(-1)
        return res
