class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            
            while left <= right:
                pivot = (left+right) //2
                if nums[pivot] > nums[pivot +1]:
                    return pivot+1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot -1
                    else:
                        left = pivot +1
        def BSearch(left, right):
            while left <= right:
                pivot = (left+right) //2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot-1
                    else:
                        left = pivot + 1
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        rotated_index = find_rotate_index(0, len(nums)-1)
        if nums[rotated_index] == target:
            return rotated_index
        if rotated_index == 0:
            return BSearch(0, len(nums) -1)
        if target < nums[0]:
            return BSearch(rotated_index, len(nums)-1)
        return BSearch(0, rotated_index-1)
            
          
                
            
        
        