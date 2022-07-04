class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        newList = Counter(nums)
        for i in newList:
            if newList[i] ==1:
                return i
        