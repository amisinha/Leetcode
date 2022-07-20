class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = 1
        minP = 1
        res = nums[0]
        
        for n in nums:
            maxTemp = max(n, maxP * n, minP * n)
            minP = min(n, maxP * n, minP * n)
            maxP = maxTemp
            
            res = max(res,maxP)
        return res
            
            
   
            
                
            
        