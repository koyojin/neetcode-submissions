# 1515
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            heapq.heapify_max(stones)

            heap=[]
            for stone in stones:
                heapq.heappush(heap, stone)
                if len(heap)>2:
                    heapq.heappop(heap)
            print(stones)
            x= heap[0]
            y= heap[1]
            if x==y:
                heapq.heappop(stones)
                heapq.heapify_max(stones)
                heapq.heappop(stones)
                print(stones)
            else:
                heapq.heappop(stones)
                heapq.heapify_max(stones)
                heapq.heappop(stones)
                heapq.heappush(stones, y-x)
                print(stones)

        if len(stones)>=1:
            return stones[0]
        else:
            return 0
