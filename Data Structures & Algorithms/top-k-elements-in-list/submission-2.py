class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m=defaultdict(int)
        for n in nums:
            m[n]+=1
        nn=[]
        for i,v in m.items():
            nn.append([i,v])
        
        nn.sort(key=lambda x:-x[1])

        return [x[0] for x in nn][:k]
        