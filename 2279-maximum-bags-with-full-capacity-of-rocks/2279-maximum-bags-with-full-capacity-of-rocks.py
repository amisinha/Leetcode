class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        newList = []
        for i in range(len(capacity)):
            newList.append(capacity[i]-rocks[i])
        newList.sort()
        remainingRocks = additionalRocks
            
        tot = 0
        for i in newList:
            if i <= remainingRocks:
                tot +=1
                remainingRocks -= i
        return tot

  
            
        
        