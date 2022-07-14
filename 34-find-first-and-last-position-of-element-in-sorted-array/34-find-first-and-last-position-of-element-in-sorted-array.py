class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        
    
        def findLeft(nums:List[int],target: int):
            start =0
            ans= -1
            end = len(nums)-1
            while start <= end:
                mid = (start+end)//2
                if nums[mid] > target:
                    end = mid -1
                elif nums[mid] < target:
                    start = mid+1
                else:
                    ans = mid
                    end = mid-1
            return ans
        def findRight(nums: List[int],target:int):
            start =0
            ans= -1
            end = len(nums)-1
            while start <= end:
                mid = (start+end)//2
                if nums[mid] > target:
                    end = mid -1
                elif nums[mid] < target:
                    start = mid+1
                else:
                    ans = mid
                    start = mid+1
            return ans
            
        left = findLeft(nums,target)
        right =findRight(nums,target)
        if left == None or right == None:
            return (-1,-1)
        else:
            return (left,right)
                

        
                
                
            
        