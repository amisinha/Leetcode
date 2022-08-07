class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        c =0
        l = len(nums1)
        for i in range(l):
            if nums1[i] in nums2:
                res.add(nums1[i])
        return res
   
            
        