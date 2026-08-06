class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key= lambda x: x[0])

        res=[intervals[0]]
        for j in range(1,len(intervals)):
            if res[-1][1]>=intervals[j][0]:
                res[-1]= [res[-1][0],max(res[-1][1],intervals[j][1])]
            else:
                res.append(intervals[j])
        
        return res