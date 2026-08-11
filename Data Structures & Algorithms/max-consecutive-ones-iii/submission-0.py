class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0
        maxf=0
        for end in range(len(nums)):
            t=nums[start:end+1]
            p= len(t)-t.count(1)
            if p>k:
                start+=1
            else:
                maxf=max(maxf,len(t))
        return maxf