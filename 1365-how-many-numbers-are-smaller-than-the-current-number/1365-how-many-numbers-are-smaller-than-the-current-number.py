class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c = 0
        newList =[]
        for i in nums:
            for j in nums:
                if i>j:
                    c = c+1
            newList.append(c)
            c=0
        return newList
            
        