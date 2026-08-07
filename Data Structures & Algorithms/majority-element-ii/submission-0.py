#1246
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        mem=defaultdict(int)
        for n in nums:
            mem[n]+=1
        print(mem)
        
        for k in mem.keys():
            if mem.get(k) > len(nums)/3:
                res.append(k)
        return res
                