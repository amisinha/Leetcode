class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def BSearch (nums,low,high,mid):
            if high >= low:
                mid = (high+low)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid]> target:
                    return BSearch(nums,low, mid-1, target)
                else:
                    return BSearch(nums, mid+1, high, target)
            else:
                return -1
        return BSearch(nums,0, len(nums)-1, target)
        