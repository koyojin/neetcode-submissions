class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        fin = defaultdict(int)
        m=0
        for e in nums:
            res[e]+=1
        
        fin=sorted(res.items(),key= lambda x: -x[1])[:k]
        return [x for x,y in fin]

