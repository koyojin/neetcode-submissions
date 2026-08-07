#1054
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        end=0
        res=float('inf')
        while end<len(nums):
            total=sum(nums[start:end+1])
            if total>=target:
                res =min(res, end+1-start)
            if total>target:
                start+=1
            else:
                end+=1
        return res if res!=float('inf') else 0