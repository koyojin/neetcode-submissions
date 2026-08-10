#1318
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=1
        for fast in range(1, len(nums)):
            if nums[slow-1] != nums[fast]:
                slow+=1
                nums[slow-1] = nums[fast]
        return slow
        