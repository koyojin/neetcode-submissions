#1133
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack=[]
        intervals.sort()
        for i in intervals:
            if stack and stack[-1][1]>=i[0]:
                t=stack.pop()
                stack.append([min(t[0],i[0]),max(t[1],i[1])])
            else:
                stack.append(i)
        return stack