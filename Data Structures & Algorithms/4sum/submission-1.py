#0114
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-2):
                l,r= j+1, len(nums)-1
                cur_target=target - nums[i] - nums[j]
                while l<r:
                    if nums[l]+nums[r] == cur_target:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                    elif nums[l]+nums[r]<cur_target:
                        l+=1
                    else:
                        r-=1


        return [list(t) for t in set(map(tuple, ans))] 

