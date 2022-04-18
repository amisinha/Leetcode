class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i=1
        if len(nums) ==1:
            return nums[0]
        else:
            
            if nums[0] != nums[1]:
                return nums[0]
            elif nums[len(nums)-1] != nums[len(nums)-2]:
                 return nums[len(nums)-1]
            else:
                for i in range(len(nums)-1):
                    
                
                    if nums[i] != nums[i+1] and nums[i]!= nums[i-1]:
                        
                    
                        return nums[i]
                    
                
                    else:
                        i=i+1
            


              

        
                    
                    
            
                
            
        