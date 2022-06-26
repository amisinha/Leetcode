class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset = set()
        for i in nums:
            if i in myset:
                return i
            else:
                myset.add(i)
        