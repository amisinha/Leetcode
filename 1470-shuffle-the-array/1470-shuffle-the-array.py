class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array1 = nums[:n]
        array2 = nums[n:]
        newList =[]
        
        for i in range(n):
            newList.append(array1[i])
            newList.append(array2[i])
        return newList
        
       
            
        