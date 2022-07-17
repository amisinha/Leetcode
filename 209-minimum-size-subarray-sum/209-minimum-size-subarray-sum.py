class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowStart = 0
        tot = 0
        minSum = float('inf')
        
        for windowEnd in range(len(nums)):
            tot += nums[windowEnd]
            
            while tot>= target:
                minSum = min(minSum, windowEnd-windowStart+1)
                tot -= nums[windowStart]
                windowStart += 1
        if isinf(minSum):
            return 0
        else:
            return minSum
                
            
        