# 1324
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]
        word1_r = list(word1)[::-1]
        word2_r = list(word2)[::-1]
        
        while word1_r or word2_r:
            if word1_r:
                res.append(word1_r.pop())
            if word2_r:
                res.append(word2_r.pop())

        return ''.join(res)