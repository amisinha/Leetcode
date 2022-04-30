class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = sorted(set(nums))
        if len(n)< 3:
            return n[len(n)-1]
        else:
            return n[len(n)-3]
        
        
        