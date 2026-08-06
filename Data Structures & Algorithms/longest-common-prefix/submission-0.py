class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=''
        strs.sort(key= lambda x: len(x))
        base=strs[0]
        for i in range(len(base)):
            print(base[:i+1])
            if all(base[:i+1] in strs[j] for j in range(1,len(strs))):
                prefix = base[:i+1]
                print(0)

        return prefix