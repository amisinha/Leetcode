class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newList = []
        for i in range(len(nums)+1):
            newList.append(sum(nums[:i]))
        return newList[1:]