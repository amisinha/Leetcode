class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        startZero = cost[0]
        startOne = cost[1]
        
        minVal = float('inf')
        
        for i in range(2, len(cost)):
            minVal = cost[i]+min(startOne, startZero) 
            startZero = startOne
            startOne = minVal
        
        return min(startZero,startOne)
        
        
        
        
        
        