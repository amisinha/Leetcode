class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = list()
        for i in range(m):
            temp.append(nums1[i])
        for j in range(n):
            temp.append(nums2[j])
        nums1.clear()
        for k in range(len(temp)):
            nums1.append(temp[k])
        nums1.sort()
        