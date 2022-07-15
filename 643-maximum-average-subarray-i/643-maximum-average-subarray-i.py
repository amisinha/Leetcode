class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        tot = 0
        maxAvg = float('-inf')
        
        for i in range(len(nums)):
            tot = tot + nums[i]
            if i >= k-1:
                avg = tot/k
                maxAvg = max(maxAvg, avg)
                tot = tot - nums[i-(k-1)]
        return maxAvg
                
                
                
            
    
        