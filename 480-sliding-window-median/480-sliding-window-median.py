class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        newList = []
        temp = []
        for i in range(len(nums)):
            temp.append(nums[i])        
            if i >= k-1:
                if k%2 == 1:
                    newList.append(sorted(temp)[(k//2)])
                else:
                    newList.append((sorted(temp)[int(k/2)] + sorted(temp)[int(k/2)-1])/2)
                del temp[0]
                    
        return newList
        
            
            
        