class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        totSum =0
        listSum=0
        i=0
        j=0
        totSum = l*(l+1) /2
        

            
        
        for j in range(l):
            listSum= listSum+ nums[j]
            j=j+1
        
        return int(totSum-listSum)
            
            