class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        c = 0
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if res[c][1] >= intervals[i][0]:
                res[c][1] = max(res[c][1], intervals[i][1])
            else:
                res.append(intervals[i])
                c += 1
        return res
            
        