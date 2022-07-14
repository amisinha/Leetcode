class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newList = []
        for i in nums:
            newList.append(i*i)
        newList.sort()
        return newList
        