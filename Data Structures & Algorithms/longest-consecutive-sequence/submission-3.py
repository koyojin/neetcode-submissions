class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst=sorted(list(set(nums)))

        if not nums:
            return 0

        cnt=1
        max=1
        for i in range(len(lst)-1):
            if lst[i]+1==lst[i+1]:
                cnt+=1
                if cnt>max:
                    max=cnt
            else:
                cnt=1
        return max

