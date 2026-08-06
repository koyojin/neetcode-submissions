class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            c= temperatures.pop()
            print(c)
            cnt=0
            Found=False
            r_stack=stack[::-1]
            print(r_stack)
            for t in r_stack:
                print(t)
                cnt+=1
                if c<t:
                    Found= True
                    break
            if not Found:
                cnt=0

            print(r_stack)
            print('----------')
            stack.append(c)
            res[i]=cnt
        return res[::-1]


