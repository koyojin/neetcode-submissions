#1030
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem=defaultdict(int)
        res=0
        start=0
        for end in range(len(s)):
            c = s[end]
            mem[c]+=1
            while mem[c]>=2:
                mem[s[start]]-=1
                start+=1
            res = max(res,end+1-start)
        return res
            