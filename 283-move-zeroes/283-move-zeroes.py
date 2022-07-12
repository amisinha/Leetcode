class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n =[]
        z= []
        for i in nums:
            if i !=0:
                n.append(i)
            else:
                z.append(i)
        nums.clear()
        for i in n:
            nums.append(i)
        for j in z:
            nums.append(j)
   
        