class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        newList = []
        if len(intervals) is not 0:
            intervals.sort(key = lambda x: x[0])
            newList.append(intervals[0])
        
            for i in range(1, len(intervals)):
                prev = intervals[i-1]
                curr = intervals[i]
                if prev[1] <= curr[0]:
                    newList.append(curr)
                else:
                    return False
        if len(newList) == len(intervals):
            return True
        else:
            return False
        
            
            
        
        