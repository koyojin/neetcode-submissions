class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        cc= self.stack.copy()
        cnt =1
        for i in range(len(cc)):
            if cc:
                if price>=cc[-1]:
                    cc.pop()
                    cnt+=1
                else:
                    break

        self.stack.append(price)

        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)