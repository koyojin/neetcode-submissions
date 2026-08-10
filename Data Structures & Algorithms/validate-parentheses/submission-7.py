#1643
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match={"}":"{", ")":'(' ,"]":"["}

        for c in s:
            if c in match:
                if stack and match[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        print(stack)
        return len(stack)==0