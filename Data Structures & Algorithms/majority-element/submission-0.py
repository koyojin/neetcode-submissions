class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memory=defaultdict(int)
        for n in nums:
            memory[n]+=1
        print(memory)
        
        for k in memory.keys():
            if memory.get(k)> len(nums)/2:
                return k