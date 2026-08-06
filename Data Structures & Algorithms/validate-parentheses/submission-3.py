class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        stack.append(s[0])
        for l in s[1:]:
            if len(stack)>0:
                if l==')' and stack[-1]=='(':
                    stack.pop()
                elif l=='}' and stack[-1]=='{':
                    stack.pop()     
                elif l==']' and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(l)
            else:
                stack.append(l)
        if len(stack)==0:
            return True
        else:
            return False