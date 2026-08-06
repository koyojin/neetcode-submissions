class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort(key = lambda x:x[0])
        for i in range(len(intervals)):
            if i>0 and res[-1][1]<intervals[i][0]:
                res.append(intervals[i])
            elif i>0 and res[-1][1]<=intervals[i][1]:
                res[-1]=[res[-1][0],intervals[i][1]]
                print(2)
            elif i>0 and res[-1][1]>intervals[i][1]:
                print(1)
                continue
            else:
                print(0)
                res.append(intervals[i])
            print(res)
        return res