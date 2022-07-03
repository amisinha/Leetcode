class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        p =1
        n =1
        if len(nums) <= 1:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i]< nums[i-1]:
                n = p+1
            elif nums[i]> nums[i-1]:
                p = n+1
        return max(p,n)
            
        
     
            
        