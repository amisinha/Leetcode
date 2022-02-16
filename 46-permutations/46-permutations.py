class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        newList = itertools.permutations(nums)
        flist = list(newList)
        return flist
        