class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 1
        maxLength = 1
        nums = sorted(list(set(nums)))
        
        if len(nums) == 0:
            return 0
       
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                length += 1
                maxLength = max(maxLength, length)
            else:
                length = 1
        return maxLength
          
            
        
                
        