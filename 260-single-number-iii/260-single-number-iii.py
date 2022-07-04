class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nn = []
        newList = Counter(nums)
        for i in newList:
            if newList[i] == 1:
                nn.append(i)
        return nn
        