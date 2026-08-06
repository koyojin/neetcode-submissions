class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=[]
        for ss in s:
            if ord(ss) in range(48,58) or ord(ss) in range(65,91) or ord(ss) in range(97,123):
                t=ss.lower()
                lst.append(t)

        if lst == lst[::-1]:
            return True
        else:
            return False

        