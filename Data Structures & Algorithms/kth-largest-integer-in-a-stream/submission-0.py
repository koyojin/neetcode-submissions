class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lst= nums
        self.top = k 
        heapq.heapify(self.lst)
        while len(self.lst)>self.top:
            heapq.heappop(self.lst)

    def add(self, val: int) -> int:
        heapq.heappush(self.lst, val)
        if len(self.lst)>self.top:
            heapq.heappop(self.lst)

        return self.lst[0]
