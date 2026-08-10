# 1501
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        remain= [[i,target-p] for i,p in enumerate(position)]
        remain.sort(key= lambda x: x[1])
        time_lst=[]
        for r in remain:
            time_lst.append(r[1]/speed[r[0]])


        stack=[]
        for j in range(len(time_lst)):

            if j>0 and time_lst[j]<= stack[-1]:
                pass
            else:
                stack.append(time_lst[j])
        return len(stack)
