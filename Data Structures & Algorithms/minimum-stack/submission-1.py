#1638
class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:

        res=[]
        for i in range(len(self.stack)):
            if i==len(self.stack)-1:
                break
            res.append(self.stack[i])
        self.stack=res
            

    def top(self) -> int:

        return self.stack[-1]
            
        

    def getMin(self) -> int:

        minf=float('inf')
        for s in self.stack:
            minf=min(minf, s)
        return minf
        
