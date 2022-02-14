class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        nums3 = list()
        i=0
        j=0
        k=0
        
        while i<l1 and j<l2:
            if nums1[i]< nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
         
                nums3.append(nums2[j])
                
                j+=1
        while i< l1:
          
            nums3.append(nums1[i])
            
      
            i+=1
            
        while j< l2:
        
            nums3.append(nums2[j])
       
            j+=1
            
        newl = len(nums3)
        if newl%2 != 0:
            return nums3[newl//2]
        else:
            nsum = nums3[(newl//2)-1] + nums3[newl//2]
            return nsum/2
        
    
        
        