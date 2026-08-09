# 2334
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h=[]
        for i, v in enumerate(arr):
            h.append([i,v, abs(v-x)])
        
        h.sort(key= lambda x: (x[2],x[0]))
        
        res=[]
        for j in range(k):
            res.append(h[j][1])

        res.sort()
        return res