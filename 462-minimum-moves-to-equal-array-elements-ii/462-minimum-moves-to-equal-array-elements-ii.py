class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        cnt =0
        nums.sort()
        mid = nums[len(nums)//2]
        for i in nums:
            cnt += abs(mid-i)
        return cnt
    
            
        