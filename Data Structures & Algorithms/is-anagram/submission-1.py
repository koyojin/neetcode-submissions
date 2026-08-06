class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst_s={}
        lst_t={}
        for e in s:
            if e not in lst_s:
                lst_s[e]=1
            else:
                lst_s[e]+=1
        for f in t:
            if f not in lst_t:
                lst_t[f]=1
            else:
                lst_t[f]+=1

        if lst_s == lst_t:
            return True
        
        else:
            return False