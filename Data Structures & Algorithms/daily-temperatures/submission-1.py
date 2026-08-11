#1728
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        r_t=temperatures[::-1]
        for i in range(len(r_t)):
            while stack and r_t[i]>=stack[-1][1]:
                stack.pop()
            if stack and r_t[i]<stack[-1][1]:
                res[len(temperatures)-1-i] = i-stack[-1][0]

            stack.append([i,r_t[i]])
        return res
