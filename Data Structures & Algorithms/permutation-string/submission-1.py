class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=l+len(s1)
        res=defaultdict(int)
        for s in s1:
            res[s]+=1

        
        while r<=len(s2):
            res_copy=res.copy()
            for t in s2[l:r]:
                if res_copy[t]:
                    res_copy[t]-=1
            print(res_copy)
            if all(v==0 for v in res_copy.values()):
                return True
            
            l+=1
            r+=1
            
        return False