import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap = []  # 방들의 종료시간을 최소힙으로 관리
        for i in intervals:
            if heap and heap[0] <= i.start:
                heapq.heappop(heap)  # 가장 빨리 끝난 방 재사용
            heapq.heappush(heap, i.end)
        return len(heap)