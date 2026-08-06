#1610
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=0
        maxf=0
        res=0
        mem=defaultdict(int)
        for end in range(len(s)):
            mem[s[end]]+=1
            maxf= max(maxf,mem[s[end]])

            d= end-start+1
            if d-maxf<=k:
                res=max(d,res)
            else:
                mem[s[start]]-=1
                start+=1
                
        return res
