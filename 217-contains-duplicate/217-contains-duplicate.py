class Solution:
    def containsDuplicate(self, nums: List[int]) ->bool:
        myset = set()
        for i in nums:
            if i in myset:
                return True
            else:
                myset.add(i)
        return False
       
    
            
      

                
    
        
    
        