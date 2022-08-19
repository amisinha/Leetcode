class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minimum = float('inf')
        nums.sort()
        
        for i in range(len(nums)-2):
            j= i+1
            k = len(nums)-1
            
            while j<k:
                res = nums[i]+ nums[j] + nums[k] - target
                if abs(res) <= abs(minimum):
                    minimum = res
                if res == 0:
                    return target
                if res <0:
                    j +=1
                else:
                    k -= 1
        return minimum +target
        
        

            
            
        