class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        newList = itertools.permutations(nums)
        fList = set(newList)
        return fList
        