class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs=[]
        res=dict()
        for s in strs:
            sorted_strs.append(str(sorted(s)))
        for i, v in enumerate(sorted_strs):
            if v not in res:
                res[v]=[strs[i]]
            else:
                res[v].append(strs[i])

        return(list(res.values()))