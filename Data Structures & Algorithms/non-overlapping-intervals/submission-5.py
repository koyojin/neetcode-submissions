class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt=1
        intervals.sort(key = lambda x: (x[1]))
        end=intervals[0][1]

        for i in range(1,len(intervals)):
            print(intervals[i][1], intervals[i-1][0])

            if intervals[i][0]>=end:
                end = intervals[i][1]
                cnt+=1

        print(cnt)
        return len(intervals)-cnt

