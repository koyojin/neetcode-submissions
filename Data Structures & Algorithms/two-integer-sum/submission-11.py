#1626
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem=[]
        for i,v in enumerate(nums):
            mem.append([i,v])
        mem.sort(key=lambda x: x[1])

        l, r= 0, len(nums)-1
        while l<r:
            if mem[l][1]+mem[r][1]==target:
                res=[mem[l][0],mem[r][0]]
                res.sort()
                return res
            elif mem[l][1]+mem[r][1]<target:
                l+=1
            else:
                r-=1