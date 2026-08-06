class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            A=[]
            for i,v in enumerate(nums):
                A.append([v,i])
            
            A.sort()

            l,r= 0,len(nums)-1
            while l<r:
                curr=A[l][0]+A[r][0]
                if curr== target:
                    return [min(A[l][1], A[r][1]),
                            max(A[l][1], A[r][1])]
                elif curr>target:
                    r-=1
                else:
                    l+=1