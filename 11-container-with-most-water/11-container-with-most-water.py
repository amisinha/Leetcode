class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)-1
        start = 0
        result = 0
        while start<l:
            result= max(result, min(height[start], height[l]) * (l-start))
            if(height[start]<height[l]):
                start= start+1
            else:
                l = l-1
        return result
        
        
        
        
        
        