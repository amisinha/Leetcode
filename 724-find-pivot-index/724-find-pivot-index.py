class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        tot = sum(nums)
        leftSum =0
        
        if tot- nums[0] == 0:
            return 0
        else:
            for i in range(1, l):
                leftSum = leftSum+ nums[i-1]
                rightSum = tot - leftSum - nums[i]
                if leftSum == rightSum:
                    return i
            return -1
   
            
        
                
      
        
        