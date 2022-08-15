class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def BSearch(low, high, nums):
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                return BSearch(mid+1,high,nums)
            elif mid > low and nums[mid-1]< nums[mid]:
                return BSearch(low, mid-1, nums)
            else:
                return nums[mid]
        return BSearch(0, len(nums)-1, nums)
            
        