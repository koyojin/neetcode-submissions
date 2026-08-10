# 1559
class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=''
        for s in strs:
            enc+=str(len(s))+'#'+s
        return enc

    def decode(self, s: str) -> List[str]:
        res=[]
        print(s)
        i=0
        j=0
        while i<len(s):
            if s[i]=='#':
                l=s[j:i]
                print(s[i+1:i+1+int(l)])

                res.append(s[i+1:i+1+int(l)])
                i=j=i+1+int(l)
            else:
                i+=1
            
        return res