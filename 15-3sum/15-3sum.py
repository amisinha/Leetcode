class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            
            while j<k:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j = j+1
                    k = k-1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j = j+1
                else:
                    k = k-1
        return res
        