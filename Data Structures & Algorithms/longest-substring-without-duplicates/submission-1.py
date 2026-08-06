class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        start=0
        for end in range(len(s)):
            state=s[start:end+1]

            if len(set(state))!=len(state):
                start+=1
                curr=len(state)-1
                res=max(res,curr)
                print('oops!', start, end)
            else:
                curr=len(state)
                res=max(res,curr)
                print(state, res, start, end)

            
        return res