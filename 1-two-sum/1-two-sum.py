class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fl=[]
        l = len(nums)
        for i in range(l):
            f = nums[i]
            for j in range(i+1, l):
                if f+ nums[j] == target:
                    fl.append(i)
                    fl.append(j)
                else:
                    j= j+1
                    
        return fl
                    
          
        